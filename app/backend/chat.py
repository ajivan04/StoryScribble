from openai import OpenAI
from dotenv import load_dotenv
import os
from IPython.display import Image
import base64
from imgsplicer import image_splicer

load_dotenv()

org_key = os.environ.get('ORGANIZATION')
open_ai_api_key = os.environ.get('OPEN_AI_KEY')
model = os.environ.get('MODEL')

client = OpenAI(
  organization=org_key,
  api_key=open_ai_api_key
)

def process_image(image_url):
    with open(image_url, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    
def create_story(age, frames):
    storyboard = image_splicer(frames)
    image = process_image(storyboard)

    messages = [
        {'role': 'system', 'content': "You are writing children's stories for young children based on drawing that they give you. Please use the appropiate vocabulary and only output the story you make."},
        {'role': 'user', 'content': [
            {'type': 'text', 'text': f'Based on this image, can you create a story that is easy for a {age} year old to read and will help them learn how to get better at reading. Note that in this story there is {frames} amount of frames. Because this is supposed to represent a picture book, it should only be one sentence per frame (so if we specify and say that there is only one frame then there should only be one description). So that means that you have to output {frames} description(s). Additionally, separate the description of each frame by a new line. At the beginning of your answer say the title of the story then a new line, then go into all the descriptions. Note that the vocabulary used should be appropriate for a {age} year old to understand. Even though it is a story it is possible for the story to be one sentece long because there is only one frame therefore only one description.'},
            {'type': 'image_url', 'image_url': {
                'url': f"data:image/png;base64, {image}"
            }}
        ]}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content


