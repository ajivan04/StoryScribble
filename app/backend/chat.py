from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

org_key = os.environ.get('ORGANIZATION')
open_ai_api_key = os.environ.get('OPEN_AI_KEY')
model = os.environ.get('MODEL')

client = OpenAI(
  organization=org_key,
  api_key=open_ai_api_key
)


completion = client.chat.completions.create(
  model=model,
  messages=[
    {"role": "system", "content": "You are a helpful assistant. Help me with my math homework!"}, # <-- This is the system message that provides context to the model
    {"role": "user", "content": "Hello! Could you solve 2+2?"}  # <-- This is the user message for which the model will generate a response
  ]
)

print(completion.choices[0].message.content)
