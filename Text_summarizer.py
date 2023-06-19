from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.mapreduce import MapReduceChain
from langchain.docstore.document import Document
from transformers import AutoTokenizer, T5ForConditionalGeneration
import streamlit as st

tokenizer = AutoTokenizer.from_pretrained("t5-small")
model= T5ForConditionalGeneration.from_pretrained("t5-small",return_dict=True)

def app():
    st.header("Summarization")
    text= st.text_area("Enter text to summarize")
   
    if text is not None:
        input_text="summarize: " + str(text)
        tokenized_text=tokenizer.encode_plus(input_text,return_attention_mask=True,return_tensors="pt")

        generated_tokens= model.generate(input_ids= tokenized_text['input_ids'],attention_mask=tokenized_text['attention_mask'],max_length=250,num_beams=2,use_cache=True,early_stopping=True)

        summary= [tokenizer.decode(token_ids=ids,skip_special_tokens=True) for ids in generated_tokens]

        st.write("".join(summary))

if __name__=='__main__':
    app()

