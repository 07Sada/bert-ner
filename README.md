---
title: BERT NER
emoji: 🐨
colorFrom: red
colorTo: indigo
sdk: streamlit
sdk_version: 1.21.0
app_file: app.py
pinned: false
---

# NER with Fine Tunned BERT 

## Application Screenshot
![application screenshot](https://github.com/07Sada/bert-ner/blob/main/images/Screenshot%202023-07-22%20175744.jpg)

## What is NER ?
**Named Entity Recognition (NER)** is a task in natural language processing (NLP) that involves **identifying and classifying named entities in text.** Named entities are words or phrases that refer to specific objects or concepts, such as people, organizations, locations, and dates.

## What is BERT ?
![BERT Architecture](https://vaclavkosar.com/images/electra-bert.png)

BERT stands for Bidirectional Encoder Representations from Transformers. The name itself gives us several clues to what BERT is all about.

BERT architecture consists of several Transformer encoders stacked together. Each Transformer encoder encapsulates two sub-layers: a self-attention layer and a feed-forward layer.

### There are two different BERT models:
- `BERT base` , which is a BERT model consists of 12 layers of Transformer encoder, 12 attention heads, 768 hidden size, and 110M parameters.

- `BERT large` , which is a BERT model consists of 24 layers of Transformer encoder,16 attention heads, 1024 hidden size, and 340 parameters.

### Reasons why BERT is a good choice for NER:
1. **Contextual Information:** BERT leverages a transformer architecture, which enables it to consider the context of each word by looking at both its left and right context in a sentence. This contextual information is crucial for accurately identifying entities, especially when the same word can be an entity in one context but not in another.
2. **Pre-trained Representations:** BERT is usually pre-trained on a large corpus of text, and the learned representations can be fine-tuned on downstream tasks like NER. Pre-training provides BERT with extensive linguistic knowledge, which often leads to improved performance on various NLP tasks, including NER.
3. **Transfer Learning:** By using pre-trained BERT models, you can leverage knowledge learned from vast amounts of text data, even if you have limited labeled data for the specific NER task. This transfer learning ability is beneficial when working with limited annotated data.
4. **State-of-the-Art Performance:** BERT has achieved state-of-the-art performance on a wide range of NLP benchmarks and competitions, including NER datasets. Its ability to handle long-range dependencies and capture subtle contextual information contributes to its success in NER.

## Model
### [BERT base model (uncased)](https://huggingface.co/bert-base-uncased)
Pretrained model on English language using a masked language modeling (MLM) objective. It was introduced in [this paper](https://arxiv.org/abs/1810.04805) and first released in [this repository](https://github.com/google-research/bert). This model is uncased: it does not make a difference between english and English.

## Dataset
### Dataset Summary
The shared task of CoNLL-2003 concerns language-independent named entity recognition. We will concentrate on four types of named entities: persons, locations, organizations and names of miscellaneous entities that do not belong to the previous three groups.

The CoNLL-2003 shared task data files contain four columns separated by a single space. Each word has been put on a separate line and there is an empty line after each sentence. The first item on each line is a word, the second a part-of-speech (POS) tag, the third a syntactic chunk tag and the fourth the named entity tag. The chunk tags and the named entity tags have the format I-TYPE which means that the word is inside a phrase of type TYPE. Only if two phrases of the same type immediately follow each other, the first word of the second phrase will have tag B-TYPE to show that it starts a new phrase. A word with tag O is not part of a phrase. Note the dataset uses IOB2 tagging scheme, whereas the original dataset uses IOB1.
[Dataset link](https://huggingface.co/datasets/conll2003)

## Deployment
The Huggingface Space's architecture is utilized for deploying the model. The code is stored in a GitHub repository and integrated into a CI/CD pipeline with the Huggingface Space. This allows the application to run smoothly and efficiently.

[Application link on huggingface](https://huggingface.co/spaces/Sadashiv/BERT-NER)

## Model Training
The model training is conducted using a free session on Google Colab.

[notebook link](notebook/Fine_tuning_BERT_NER.ipynb)

## Fine Tuned Model
The [fine-tuned](https://huggingface.co/Sadashiv/BERT-ner) BERT model is stored in Hugging Face's hub.

## Addition Resources
The Streamlit interface uses Streamlit's [st-annotated-text](https://github.com/tvst/st-annotated-text) package to highlight the recognized entity.

