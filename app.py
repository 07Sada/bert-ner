import streamlit as st
from annotated_text import annotated_text
from utils import ner_extraction

st.title('NER with Fined-Tuned BERT model')

input_text = st.text_area("Please Enter the text..")

ner_extraction = ner_extraction(input_text)

if st.button('Submit'):
    annotated_text(ner_extraction.entity_position())
