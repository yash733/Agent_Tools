import os, sys
from dotenv import load_dotenv
load_dotenv()
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from langchain.agents import initialize_agent, AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
import streamlit as st
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from pydantic import BaseModel 
from typing import Annotated 
from langchain.agents import initialize_agent


from config import Config
from tools.arxiv import arxive_tool
from tools.duck import duck_go
from tools.wiki import wiki_tool
from model import model

os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = 'TOOLS INTEGRATION'
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

if 'user_config' not in st.session_state:
    st.session_state.user_config = {}

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [{"role":"assisstant","content":"Hi,I'm a chatbot who can search the web. How can I help you?" }]

model_ = model()
config = Config()
# print(config.get_title())
st.title(config.get_title())

st.text("""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
""")

st.session_state.user_config['config_store'] = False

with st.sidebar:
    llm = st.selectbox(label='Choose Model', options= config.get_model(), key='LLM')

    if llm == 'Groq':
        llm_version = st.selectbox(label='Select Model Type', options= config.get_groq_model(), key='GROQ')
        st.session_state.user_config['api'] = st.text_input(label='Enter API KEY', type='password')
        if st.session_state.user_config['api']:
            os.environ['GROQ_API_KEY'] = st.session_state.user_config['api']
        else:  
            st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")

    elif llm == 'Ollama':
        llm_version = st.selectbox(label='Select Model Type', options= config.get_ollama_model(), key='Ollama')
    
    if not st.session_state.user_config['config_store']:
        if st.button('Start'):
            st.session_state.user_config['config_store'] = True
            st.session_state.user_config.update({'llm': llm, 'llm_version': llm_version})

prompt = {"role":"system","content":"You are an helpfull assistant, helping by solving user query. Gathering data by using tools." }

input = st.chat_input('Enter Your query')

for msg in st.session_state.chat_history:
    st.chat_message(msg['role']).write(msg['content'])


if input:
    st.session_state.chat_history.append({'role':'user', 'content':f'{input}'})
    st.chat_message("user").write(input)

    if st.session_state.user_config.get('llm') == 'Groq':
        inferance_model = model_.groq_llm(st.session_state.user_config.get('llm_version'))
    else:
        inferance_model = model_.ollama_llm(st.session_state.user_config.get('llm_version'))
    
    tools = [arxive_tool().tool(), wiki_tool().tool(), duck_go().tool()]

    agent = initialize_agent(tools=tools, llm = inferance_model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)

    with st.chat_message('assistant'):
        st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response = agent.run(st.session_state.chat_history,callbacks=[st_cb])
        st.session_state.chat_history.append({'role':'assistant',"content":response})
        st.write(response)