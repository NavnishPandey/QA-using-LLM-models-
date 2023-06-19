import streamlit as st
from Appselect import appselect
import PdfQA, csvfileQA, YotubeQA, Text_summarizer

app = appselect()


# Add all your application here
app.add_app("PDF Q/A", PdfQA.app)
app.add_app("CSV Q/A", csvfileQA.app)
app.add_app("Youtube Q/A", YotubeQA.app)
app.add_app("Text Summarizer", Text_summarizer.app)

# The main app
app.run()