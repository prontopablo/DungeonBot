import openai
import json
import os

# Set OpenAI API key
openai.api_key = "Your API key"

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

        # A system prompt is an optional context to provide instructions or initial context for the AI model
        system_prompt = "You are a dungeons and dragons narrator. Always respond in character. Be lighthearted and funny. Please respond to the situations I describe to you."

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