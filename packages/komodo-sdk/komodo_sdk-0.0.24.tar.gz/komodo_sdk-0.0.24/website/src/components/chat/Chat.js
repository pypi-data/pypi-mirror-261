import React, { useContext, useEffect, useState } from "react";
import send from "../../images/send.png";
import PrimaryLayout from "../../layout/PrimaryLayout";
import profile from '../../images/profile.png'
import dots from '../../images/dots.png'
import roleContext from "../../contexts/roleContext"
import wave from '../../images/wave.png'
import EnhancedPrompt from "./EnhancedPrompt";

const Chat = () => {
    const chatContext = useContext(roleContext)
    const user = JSON.parse(localStorage.getItem('komodoUser'))
    const [prompt, setPrompt] = useState('');
    const [text, setText] = useState('');
    const [allChatData, setAllChatData] = useState([]);
    const [newDetails, setNewDetails] = useState({ gId: "", chatRes: "" });

    useEffect(() => {
        if (chatContext?.chatGuid !== "") {
            setNewDetails({ ...newDetails, gId: chatContext?.chatGuid })
        }
    }, [chatContext?.chatGuid])


    const sendPrompt = async () => {
        chatContext?.setChatHistory(true)
        if (newDetails.chatRes !== "") {
            setAllChatData(prevData => [
                ...prevData,
                { sender: chatContext?.reactSelect?.shortcode, text: newDetails.chatRes },
                { sender: user.email, text: prompt }
            ]);
            setNewDetails({ ...newDetails, chatRes: "" });
        } else {
            setAllChatData(prevData => [
                ...prevData,
                { sender: user.email, text: prompt }
            ]);
        }
        setText(prompt)
        setPrompt('')
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            sendPrompt();
        }
    };

    const getTimeOfDay = () => {
        const now = new Date();
        const hour = now.getHours();

        if (hour >= 5 && hour < 12) {
            return "Good Morning, ";
        } else if (hour >= 12 && hour < 18) {
            return "Good Afternoon, ";
        } else {
            return "Good Evening, ";
        }
    };

    return (
        <>
            <PrimaryLayout>
                <div className="h-[calc(100%-96px)]">
                    {chatContext?.chatHistory === true ?
                        <div className="flex">
                            <div className="w-full flex items-center flex-col">
                                <div className='mt-10 ms-7 pe-8 h-[calc(100vh-218px)] w-[1017px] xl:w-[900px] lg:w-[800px] overflow-auto scrollbar'>
                                    {/* <div className='mb-10'>
                                        {text && <div className='flex gap-5 items-center'>
                                            <div>
                                                <img src={profile} alt="profile" className='w-[30px] h-[30px]' />
                                            </div>
                                            <div className='text-[16px] font-cerebriregular rounded-md bg-[#497ad32b] px-4 py-3 text-[#495057]'>
                                                {text}
                                            </div>
                                        </div>
                                        }
                                        <div>
                                            <div className='mt-10 flex gap-5'>
                                                {text ? <div>
                                                    <img src={wave} alt="wave" className='w-[30px] h-[30px]' />
                                                </div> : ""}
                                                <EnhancedPrompt prompt={text} />
                                            </div>
                                        </div>
                                        {askRes !== "" ?
                                            <div>
                                                <div className="mt-10 flex gap-5">
                                                    <div>
                                                        <img src={wave} alt="wave" className='w-[30px] h-[30px]' />
                                                    </div>
                                                    <div className='w-fit text-[#495057]'>
                                                        <p
                                                            className='font-cerebriregular text-[15px] leading-[34px] text-justify'
                                                            dangerouslySetInnerHTML={{ __html: askRes }}
                                                        ></p>
                                                    </div>
                                                </div>
                                            </div>
                                            : null}
                                        <div>
                                            <div className='mt-10 flex gap-5'>
                                                {res === true ? <div>
                                                    <img src={wave} alt="wave" className='w-[30px] h-[30px]' />
                                                </div> : ""}
                                            </div>
                                        </div>
                                    </div> */}
                                    {allChatData && allChatData.length > 0 && allChatData.map((val, i) => {
                                        return (
                                            <div className='mb-10' key={i}>
                                                {val?.sender === user?.email && <div div className='flex gap-5 items-center'>
                                                    <div>
                                                        <img src={profile} alt="profile" className='w-[30px] h-[30px]' />
                                                    </div>
                                                    <div className='text-[16px] font-cerebriregular rounded-md bg-[#497ad32b] px-4 py-3 text-customBlue'>
                                                        {val?.text}
                                                    </div>
                                                </div>}
                                                {val?.sender === chatContext?.reactSelect?.shortcode && <div>
                                                    <div className='mt-10 flex gap-5'>
                                                        <div>
                                                            <img src={wave} alt="wave" className='w-[30px] h-[30px]' />
                                                        </div>
                                                        <div className='w-fit text-[#495057]'>
                                                            <p className='font-cerebriregular text-[15px] leading-[34px] text-justify' dangerouslySetInnerHTML={{ __html: val?.text.replace(/\n/g, '<br>') }}></p>
                                                        </div>
                                                    </div>
                                                </div>}
                                            </div>
                                        )
                                    })}
                                    {text !== "" && <div className='mb-10'>
                                        <div>
                                            <div className='mt-10 flex gap-5'>
                                                <div>
                                                    <img src={wave} alt="wave" className='w-[30px] h-[30px]' />
                                                </div>
                                                <div className='w-fit text-[#495057]'>
                                                    <EnhancedPrompt prompt={text} guid={newDetails?.gId} setNewDetails={setNewDetails} />
                                                </div>
                                            </div>
                                        </div>
                                    </div>}
                                </div>
                                <div className="border-t-[0.5px] border-[#CDCDCD]">
                                    <div className="flex gap-4 items-center justify-center ps-6 py-5 w-full pe-8">
                                        <div className='w-[25px]'>
                                            <img src={dots} alt="send" />
                                        </div>
                                        <input type="text" placeholder="Ask me anything..." value={prompt} onChange={(e) => setPrompt(e.target.value)} onKeyDown={handleKeyPress} className="w-[892px] h-[43px] border border-[#CFD4D8] rounded-md px-4 text-[14px] font-cerebriregular leading-[17.78px] outline-none" />
                                        <img src={send} alt="send" onClick={sendPrompt} className='cursor-pointer' />
                                    </div>
                                </div>
                            </div>
                        </div>
                        :
                        <div className="flex items-center justify-center h-full">
                            <div className="">
                                <h1 className="text-[23px] font-cerebri leading-[29.21px] text-[#495057] mb-4">{getTimeOfDay() + user?.name}</h1>
                                <div className="flex gap-4">
                                    <input type="text" placeholder="Ask me anything..." value={prompt} onChange={(e) => setPrompt(e.target.value)} onKeyDown={handleKeyPress} className="w-[892px] xxl:w-[500px] h-[43px] border border-[#CFD4D8] rounded-md px-4 text-[15px] font-cerebriregular leading-[19.05px] outline-none" />
                                    <img src={send} alt="send" onClick={sendPrompt} className='cursor-pointer' />
                                </div>
                            </div>
                        </div>
                    }
                </div>
            </PrimaryLayout>
        </>
    );
};

export default Chat;
