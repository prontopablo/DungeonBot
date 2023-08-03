import whisper

def get_whisper_response():
    # Set the model (tiny is faster, but less accurate)
    model = whisper.load_model("base")
    # Transcribe the audio file
    result = model.transcribe("input_audio.wav", fp16=False, language='English')
    
    # Return the transcribed text
    return result

