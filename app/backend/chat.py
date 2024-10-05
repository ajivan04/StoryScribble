from openai import OpenAI
from dotenv import load_dotenv
import os
from IPython.display import Image, display, Audio, Markdown
import base64

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
    
def image_splicer(images):
    return None
    
def create_story(age, images):
    #storyboard = image_splicer(images)
    image = process_image(images)

    messages = [
        {'role': 'system', 'content': "You are writing children's stories for young children based on drawing that they give you. Please use the appropiate vocabulary and only output the story you make."},
        {'role': 'user', 'content': [
            {'type': 'text', 'text': 'Based on these images, can you create a story that is easy for a 5 year old to read and will help me them to learn how to get better at reading. Note that the black bars represent different frames of the story. Note that the vocabulary used should be appropriate for a 5 year old to understand. Only output the story and nothing else.'},
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


print(create_story(5, "assets/combined_image.png"))




