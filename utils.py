import requests
from dotenv import load_dotenv
import os

# load the .env file
load_dotenv()

API_KEY = os.getenv("API")

API_URL = "https://api-inference.huggingface.co/models/Sadashiv/BERT-ner"
headers = {"Authorization": f"Bearer {API_KEY}"}

tag_color_combination = {'O': '#FF5733',
                        'PER': '#35B7FF',
                        'ORG': '#00FF00',
                        'LOC': '#FFA500',
                        'MISC': '#BA55D3'}


class ner_extraction:
  def __init__(self, input_text):
    self.input_text = input_text

  def query(self):
    response = requests.post(API_URL, headers=headers, json=self.input_text)
    return response.json()

  def entity_position_locator(self):
    output = self.query()
    entity_position = {}

    for i in range(len(output)):
      entity_position[i]={}
      entity_position[i]["start"]=output[i]['start']
      entity_position[i]["end"]=output[i]['end']

    return entity_position 
  
  def entity_update(self):
    entity_list = []
    output = self.query()

    for i in range(len(output)):
      entity_list.append(
          (
              output[i]['word'],
              output[i]['entity_group'],
              tag_color_combination.get(output[i]['entity_group'])
          )
      )

    return entity_list

  def text_list(self):

    input_text = self.input_text
    entity_position = self.entity_position_locator()

    split_text = [] 

    for i in entity_position:
      split_text.append(input_text[entity_position[i]['start']:entity_position[i]['end']])
      
      if entity_position[i]['end']!=len(input_text):
        
        if i+1<len(entity_position):
            split_text.append(input_text[entity_position[i]['end']:entity_position[i+1]['start']])
        
        else:
          split_text.append(input_text[entity_position[i]['end']:])

    return split_text


  def entity_position(self):
    split_text = self.text_list()
    entity_list = self.entity_update()
    for i in range(len(split_text)):
      for j in range(len(entity_list)):
        if type(split_text[i])!= tuple:
          if split_text[i].lower()==entity_list[j][0]:
            split_text[i]=entity_list[j]

    return tuple(split_text)
