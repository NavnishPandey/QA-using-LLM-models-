
import streamlit as st
import os

class appselect:
    
    
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
       
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        
        
        app = st.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app: app['title'])
        api_key = st.text_input(
           "Enter Open AI Key.",
            placeholder = "sk-...",
            type="password"
            )
        
        os.environ["OPENAI_API_KEY"]=api_key

        app['function']()