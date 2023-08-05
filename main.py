import pyaudio
import wave
import threading
import whisper_api
import gpt_api
import eleven_labs_api
import os
import sys
from elevenlabs import play

class DungeonBot:
    def __init__(self):
        os.system('cls') # clear the console
        self.recording = False
        self.frames = [] # list of audio frames
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=44100,
            input=True,
            frames_per_buffer=1024,
        )

    def start_recording(self):
        self.frames = []
        self.recording = True
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=44100,
            input=True,
            frames_per_buffer=1024,
        )
        print("Recording (q to stop)...")

        # Start a new thread for recording
        threading.Thread(target=self.record).start()

    def record(self):
        while self.recording:
            try:
                data = self.stream.read(1024)  # read audio data from stream in 1024 byte chunks
                self.frames.append(data)  # add audio frame to list
            except KeyboardInterrupt:
                self.stop_recording()

    def stop_recording(self):
        if self.recording:
            self.recording = False
            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()
            print("Finished recording.")

            print("Saving recording...")
            sound_file = wave.open("input_audio.wav", "wb")
            sound_file.setnchannels(1)
            sound_file.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
            sound_file.setframerate(44100)
            sound_file.writeframes(b"".join(self.frames))
            sound_file.close()

    def transcribe(self):
        print("Transcribing...")
        result = whisper_api.get_whisper_response()
        text = result["text"].lstrip() # Remove leading whitespace
        print(text)  # Print the transcription result

        while True:
            answer = input("Is the transcription correct? (y/n): ")
            if answer.lower() == "y":
                print("Generating response...")
                response = gpt_api.get_gpt_response(result["text"])
                print(response)

                print("Generating audio...")
                audio = eleven_labs_api.get_eleven_labs_response(response)
                print("Playing audio...")
                play(audio)
                print("Finished playing audio.")

                while True:
                    inp = input("Press p to start recording, r to hear the audio again, and q to quit\n")
                    if inp.lower() == "p":
                        self.start_recording()
                        return  # Exit the transcribe method and let it start over
                    elif inp.lower() == "r":
                        play(audio)
                    elif inp.lower() == "q":
                        # exit the program
                        print("Exiting...")
                        sys.exit()
                    else:
                        print("Invalid input. Try again.")

            elif answer.lower() == "n":
                self.start_recording()  # Start recording again
                break

    def update(self):
        self.update()

def main():
    bot = DungeonBot()
    print("Press p to start recording")
    while True:
        inp = input("")

        if inp.lower() == "p":
            bot.start_recording()
        elif inp.lower() == "q":
            bot.stop_recording()
            bot.transcribe()
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()