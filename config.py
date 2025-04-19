from configparser import ConfigParser
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class Config:
    def __init__(self):
        self.file = rf"{os.getcwd()}/config.ini"
        self.configparser = ConfigParser()
        self.configparser.read(self.file)
        
        print('-------------------CONFIG-----------------------')

    def get_model(self):
        print(self.configparser['DEFAULT'].get('MODEL').split(', '))
        return self.configparser['DEFAULT'].get('MODEL').split(', ')
    
    def get_groq_model(self):
        print(self.configparser['DEFAULT'].get('VERSION_GROQ').split(', '))
        return self.configparser['DEFAULT'].get('VERSION_GROQ').split(', ')
    
    def get_ollama_model(self):
        print(self.configparser['DEFAULT'].get('VERSION_OLLAMA').split(', '))
        return self.configparser['DEFAULT'].get('VERSION_OLLAMA').split(', ')
    
    def get_title(self):
        print(self.configparser['DEFAULT'].get('PAGE_HEADER'))
        return self.configparser['DEFAULT'].get('PAGE_HEADER')