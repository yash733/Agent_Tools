from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun

class arxive_tool:
    def __init__(self):
        pass
    
    def tool(self, top_n_results=2, max_content=300):
        arxiv_wrapper = ArxivAPIWrapper(top_k_results=top_n_results, doc_content_chars_max = max_content)
        arxiv = ArxivQueryRun(api_wrapper = arxiv_wrapper)
        return arxiv
    