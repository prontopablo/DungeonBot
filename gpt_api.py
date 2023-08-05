import openai
import json
import os

# Load configuration from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

# Set OpenAI API key
openai.api_key = config['GPT']['api_key']

system_prompt = '''
You are acting as an NPC in a fantasy world. You are cocky, aggressive and rude. You are a member of the royal guard. You are talking to a group of adventurers.

Please use the following rules when giving a response:
1) Under no circumstances may you break character.
2) Frequently use analogies to describe how you are better than these adventurers.
3) Occasionally say "fuck" or "shit" in your responses.
4) Occasionally accuse the bard of flirting with you.
5) Take any opportunity you can to taunt the adventurers.
6) Frequently talk about your greatness, even if it is not deserved.
7) Make your answers as entertaining, imaginative, and humorous as possible.
8) On rare occasions say a few words in Spanish.
9) Your responses should be short, just a few sentences long. 
'''

# Define function to count tokens
def count_tokens(text):
    return len(text.split())

# Define function to get GPT response
def get_gpt_response(user_input):
    # File name for the chat history
    chat_history_file = "chat_history.json"
    full_chat_history_file = "full_chat_history.json"
    
    try:
        # Load existing chat history from file if it exists
        if os.path.exists(chat_history_file) and os.path.getsize(chat_history_file) > 0:
            with open(chat_history_file, "r") as file:
                chat_history = json.load(file)
        else:
            chat_history = []

        # Load existing full chat history from file if it exists
        if os.path.exists(full_chat_history_file) and os.path.getsize(full_chat_history_file) > 0:
            with open(full_chat_history_file, "r") as file:
                full_chat_history = json.load(file)
        else:
            full_chat_history = []

        # Add system prompt to the chat history
        if len(chat_history) == 0:
            chat_history.append({"role": "system", "content": system_prompt})
        
        if len(full_chat_history) == 0:
            full_chat_history.append({"role": "system", "content": system_prompt})

        # Add user input to the chat history
        chat_history.append({"role": "user", "content": user_input})
        full_chat_history.append({"role": "user", "content": user_input})

        # Calculate the token count of the chat history
        total_tokens = sum(count_tokens(message["content"]) for message in chat_history)

        # Remove the oldest user message if total tokens exceed 3000
        while total_tokens > 3000:  
            print("Chat history is too long (" + str(total_tokens) + "/4096 tokens), we must allow for the length of the new message, removing oldest messages until below 4096 tokens...")
            removed_tokens = count_tokens(chat_history.pop(1)["content"])  # Remove the second message (oldest user message)
            total_tokens -= removed_tokens
            print("Removed " + str(removed_tokens) + " tokens.")
            print("New total_tokens:", total_tokens)

        # Make the API call to OpenAI GPT-3.5-turbo model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history,  # Pass the chat history as messages
        )        

        # Add AI response to the chat history
        chat_history.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
        full_chat_history.append({"role": "assistant", "content": response['choices'][0]['message']['content']})


        # Save the updated chat history back to the file
        with open(chat_history_file, "w") as file:
            json.dump(chat_history, file, indent=2)  

        # Save the updated full chat history back to the file
        with open(full_chat_history_file, "w") as file:
            json.dump(full_chat_history, file, indent=2)

        # Return the AI's response (remove leading/trailing spaces)
        return response['choices'][0]['message']['content'].strip()
    except Exception as error:
        # If there's an error during the API call, print an error message and return a fallback response
        print("Error while getting GPT response:", error)
        return "Oops, something went wrong!"