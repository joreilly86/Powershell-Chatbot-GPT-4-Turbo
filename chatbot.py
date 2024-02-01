from dotenv import load_dotenv
import os
from openai import OpenAI
import pyperclip

"""
Interactive Chatbot using OpenAI's GPT-4-turbo Model (gpt-4-0125-preview)

This script creates an interactive chatbot that uses OpenAI's GPT-4-turbo model to generate responses based on user input.
It maintains a conversation history to provide context for each new message, making the interaction more coherent.
The chatbot's responses are automatically copied to the clipboard using the pyperclip library for convenience.

Prerequisites:
- An OpenAI API key set as an environment variable named OPENAI_API_KEY.
- python-dotenv installed to load environment variables from a .env file.
- pyperclip installed to copy text to the clipboard.

Usage:
- Run the script in a terminal.
- Type your messages after the prompt "You: ".
- The AI's response will be printed and copied to the clipboard.
- Type 'quit' to end the conversation.

Environment Setup:
- Create a .env file in the root directory of your project with your OpenAI API key:
  OPENAI_API_KEY='your_api_key_here'
- Ensure pyperclip and python-dotenv are added to your project via Poetry or pip.

"""

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.environ.get("OPENAI_API_KEY")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Initialize an empty list to keep track of the conversation
conversation_history = []

while True:
    # Get input from the user
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break  # Exit the loop if the user types 'quit'
    
    # Append the user's message to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Create a chat completion request including the conversation history
    completion = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": "You are a professional civil and structural engineering assistant, skilled in drafting technical reports and solving complex design issues. Your responses should be succinct, professional, and highly technical but explained in a manner that is clear and precise."},
            *conversation_history
        ]
    )

    # Retrieve the AI's response and extract the content as a string
    ai_response_content = completion.choices[0].message.content
    print(f"AI: {ai_response_content}")

    # Append the AI's response (as a plain string) to the conversation history
    conversation_history.append({"role": "system", "content": ai_response_content})

    # Copy the AI's response content to the clipboard
    pyperclip.copy(ai_response_content)