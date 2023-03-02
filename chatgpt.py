#!/usr/bin/env python3
#remove env if testing
import openai
import os

TOKEN = os.environ.get('OPENAI_API_KEY')
if not TOKEN:
    print('Error: OPENAI_API_KEY environment variable is not set')
    exit(1)
    

# Initialize the OpenAI API client
openai.api_key = TOKEN

# Initialize the conversation
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nUser: Hello, who are you?\nAI:",
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response["choices"][0]["text"])

# Enter the conversation loop
while True:
    # Get user input
    user_input = input("Ray: ")

    # Send the input to the API and get a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"User: {user_input}\nAI:",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    print("Bote: " + response["choices"][0]["text"])

    # End the conversation if the user types 'exit'
    if user_input.lower() == 'exit':
        break
