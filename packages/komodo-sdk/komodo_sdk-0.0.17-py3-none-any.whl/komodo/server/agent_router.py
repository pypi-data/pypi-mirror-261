import base64
from typing import AsyncGenerator

from fastapi import Depends, APIRouter, HTTPException, Request
from starlette.responses import StreamingResponse

from komodo.framework.komodo_agent import KomodoAgent
from komodo.framework.komodo_app import KomodoApp
from komodo.models.framework.runners import run_agent, run_agent_streamed, get_agent
from komodo.proto.model_pb2 import Message
from komodo.server.globals import get_appliance, get_email_from_header
from komodo.store.conversations_store import ConversationStore

router = APIRouter(
    prefix='/api/v1/agent',
    tags=['Agent']
)


@router.api_route('/ask', methods=['POST'])
async def ask_agent(request: Request, email=Depends(get_email_from_header), appliance=Depends(get_appliance)):
    # Parse the request body as JSON
    body = await request.json()
    # Extract the message and agent_info fields from the JSON body
    message = body.get("message")
    agent_shortcode = body.get("agent_shortcode")
    if not message or not agent_shortcode:
        raise HTTPException(status_code=400, detail="Missing 'message or agent_shortcode' in request body")

    # Get Agent Info based on short code
    agent = get_agent(appliance, agent_shortcode)
    if agent is None:
        raise HTTPException(status_code=400, detail="Respective Agent is not available")

    store = ConversationStore()
    conversation = setup_conversation(agent_shortcode, email, body.get("guid"), message, store)
    reply = run_agent(appliance, agent, message)
    store.add_message(conversation, sender=agent_shortcode, sender_type=Message.SenderType.AGENT, text=reply.text)
    return {"reply": reply.text, "message": message}


@router.get("/ask-streamed")
async def ask_agent_streamed(email: str, agent_shortcode: str, prompt: str, guid: str = None,
                             appliance=Depends(get_appliance)):
    print("email: ", email, "agent_shortcode: ", agent_shortcode, "prompt: ", prompt)

    # Get Agent Info based on short code
    agent = get_agent(appliance, agent_shortcode)
    if agent is None:
        raise HTTPException(status_code=400, detail="Respective Agent is not available")

    store = ConversationStore()
    conversation = await setup_conversation(agent_shortcode, email, guid, prompt, store)
    history = await get_history(conversation)

    def store_callback(message):
        store.add_message(conversation, sender=agent_shortcode, sender_type=Message.SenderType.AGENT, text=message)

    return StreamingResponse(komodo_async_generator(appliance, agent, prompt, history, store_callback),
                             media_type='text/event-stream')


async def setup_conversation(agent_shortcode, email, guid, prompt, store):
    if guid is None or guid == "":
        title = prompt
        conversation = store.create_conversation(email, agent_shortcode, title)
    else:
        conversation = store.get_conversation(guid)
    store.add_message(conversation, sender=email, sender_type=Message.SenderType.USER, text=prompt)
    return conversation


async def get_history(conversation):
    history = []
    for message in conversation.messages:
        role = "user"
        if message.sender_type == Message.SenderType.AGENT:
            role = "assistant"
        history.append({'role': role, "content": message.text})
    return history


async def komodo_async_generator(appliance: KomodoApp, agent: KomodoAgent, prompt: str, history: [Message],
                                 store_callback) -> \
        AsyncGenerator[str, None]:
    reply = ""
    exception_occurred = False  # Flag to indicate an exception occurred
    exception_message = ""  # To store the exception message
    for part in run_agent_streamed(appliance, agent, prompt, history):
        reply += part
        if exception_occurred:
            break  # Stop processing if an exception has occurred

        try:
            encoded = base64.b64encode(part.encode('utf-8')).decode('utf-8')
            yield f"data: {encoded}\n\n"
        except Exception as e:
            exception_occurred = True
            exception_message = str(e)

    store_callback(reply)

    if exception_occurred:
        print("Error while streaming: " + exception_message)
    else:
        print("stream complete")
        yield "event: stream-complete\ndata: {}\n\n"
