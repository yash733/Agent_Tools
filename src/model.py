from langchain_groq import ChatGroq
from langchain_ollama import OllamaLLM

class model:
    def groq_llm(self,model_name:str):
        print('***Gorq model_name',model_name)
        model = ChatGroq(model = model_name)
        return model

    def ollama_llm(self,model_name:str):
        print('***Ollama model_name',model_name)
        model = OllamaLLM(model = model_name)
        return model