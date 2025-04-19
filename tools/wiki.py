from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun

class wiki_tool:
    def __init__(self):
        pass

    def tool(self, top_n_results=3, max_content=300):
        wiki_wrapper = WikipediaAPIWrapper(top_k_results = top_n_results, doc_content_chars_max = max_content)
        wiki = WikipediaQueryRun(api_wrapper = wiki_wrapper)
        return wiki
    