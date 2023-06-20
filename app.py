import os
import openai

openai.api_key_path = '.pyenv'

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Hi, how are you?",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].text)
