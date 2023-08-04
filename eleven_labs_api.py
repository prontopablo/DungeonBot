import os
from elevenlabs import generate, set_api_key

# Set Eleven Labs API key
set_api_key("Your API key")

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
    voice="King Henry",
    model="eleven_monolingual_v1"
    )
    save_audio_to_file(audio)
    return audio
