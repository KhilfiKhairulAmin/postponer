import os
import openai

openai.api_key_path = '.pyenv'
model = 'text-davinci-003'

while True:
  prompt = str(input('User: '))
  response = openai.Completion.create(
    model=model,
    prompt=prompt,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  print(f'{model}: {response.choices[0].text[1:]} \n')
