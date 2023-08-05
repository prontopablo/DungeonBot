import os
import json
from elevenlabs import generate, set_api_key

# Load configuration from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

api_key = config['eleven_labs']['api_key']
chosen_voice = config['eleven_labs']['voice']

# Set Eleven Labs API key
set_api_key(api_key)

def save_audio_to_file(audio_data):
    response_number = 1  # track no. responses to name files
    while os.path.exists(os.path.join("responses", f"response_{response_number}.wav")):
        response_number += 1

    file_path = os.path.join("responses", f"response_{response_number}.wav")  # name file

    # save audio to file
    with open(file_path, "wb") as audio_file:
        audio_file.write(audio_data)

def get_eleven_labs_response(response):
    audio = generate(
    text = response,
    voice=chosen_voice,
    model="eleven_monolingual_v1"
    )
    save_audio_to_file(audio)
    return audio
