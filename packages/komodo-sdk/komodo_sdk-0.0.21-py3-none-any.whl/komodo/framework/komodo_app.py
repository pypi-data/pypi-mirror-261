import json

from komodo.framework.komodo_agent import KomodoAgent, data_agent
from komodo.framework.komodo_datasource import KomodoDataSource
from komodo.framework.komodo_tool import KomodoTool
from komodo.framework.komodo_tool_registry import KomodoToolRegistry
from komodo.framework.komodo_vectorstore import KomodoVectorStore
from komodo.store.collection_store import CollectionStore


class KomodoApp:
    def __init__(self, shortcode, name, purpose, agents=None, tools=None, sources=None):
        self.shortcode = shortcode
        self.name = name
        self.purpose = purpose
        self.agents: [KomodoAgent] = []
        self.tools: [KomodoTool] = []
        self.data_sources: [KomodoDataSource] = sources or []
        self.vector_stores: [KomodoVectorStore] = []
        for agent in agents or []:
            self.add_agent(agent)
        for tool in tools or []:
            self.add_tool(tool)

    def add_agent(self, agent):
        self.agents += [agent]

    def add_tool(self, tool):
        if isinstance(tool, str):
            tool = KomodoToolRegistry.get_tool_by_shortcode(tool)
        elif isinstance(tool, dict):
            tool = KomodoTool(**tool)
        if isinstance(tool, KomodoTool):
            self.tools.append(tool)
            return
        raise ValueError(f"Invalid tool: {tool}")

    def search_data_definition(self):
        return {
            "type": "function",
            "function": {
                "name": "komodo_data_search",
                "description": "Search available data sources",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Search across all available data using vector search"
                        }
                    },
                    "required": ["query"]
                }
            }
        }

    def get_data_as_tool_action(self, args):
        text = args['query']
        store: KomodoVectorStore = self.get_vector_store()
        result = store.search(text, top_k=3)
        if len(result) > 0:
            return json.dumps(result)
        return "No results found for: {}".format(args['query'])

    def search_data_tool(self):
        return KomodoTool(shortcode="komodo_data_search",
                          name="Appliance Data Search Tool",
                          definition=self.search_data_definition(),
                          action=self.get_data_as_tool_action)

    def add_vector_store(self, store: KomodoVectorStore):
        self.vector_stores.append(store)
        if store.shortcode == 'default':
            self.tools = [self.search_data_tool()] + self.tools
            self.agents = [data_agent(self.search_data_tool())] + self.agents

    def get_vector_store(self, shortcode='default'):
        for a in self.vector_stores:
            if a.shortcode == shortcode:
                return a
        return None

    def get_collection(self, shortcode='default'):
        store = CollectionStore()
        collection = store.get_or_create_collection(shortcode, "Default Collection", "Default Appliance Collection")
        return collection
