from langchain_community.tools import DuckDuckGoSearchRun

class duck_go:
    def __init__(self):
        pass    

    def tool(self):
        return DuckDuckGoSearchRun(name='Search')