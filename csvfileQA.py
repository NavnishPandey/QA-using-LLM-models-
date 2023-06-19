from langchain.agents import create_csv_agent, create_pandas_dataframe_agent 
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd



def csv_tool(filename : str):

    df = pd.read_csv(filename)
    return df

def app():

    st.header("Ask your CSV 📈")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    
    if csv_file is not None:
        data=csv_tool(csv_file)
        user_question = st.text_input("Ask a question about your csv file:")
        llm= OpenAI(temperature=0)
        
        agent= create_pandas_dataframe_agent(llm, data, verbose=True)
        response = agent.run(user_question)

        st.write(response)

        


if __name__ == "__main__":
    app()