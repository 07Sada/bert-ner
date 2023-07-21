import streamlit as st
from annotated_text import annotated_text
from utils import ner_extraction


input_text = 'Bill Gates lives in USA'

ner_extraction = ner_extraction(input_text)

print(ner_extraction.entity_position())