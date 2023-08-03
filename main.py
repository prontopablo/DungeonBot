import tkinter as tk
import pyaudio
import wave
import whisper_api
import gpt_api
import eleven_labs_api
import os
from elevenlabs import play


class DungeonBot:
    def __init__(self, master):
        self.master = master
        self.master.title("DungeonBot")

        self.recording = False
        self.frames = []

        self.record_button = tk.Button(
            master, text="Start Recording", command=self.start_recording
        )
        self.record_button.pack(pady=20)

        self.stop_button = tk.Button(
            master, text="Stop Recording", command=self.stop_recording
        )
        self.stop_button.pack(pady=10)
        os.system('cls')

    def start_recording(self):
        self.audio = pyaudio.PyAudio()  # create audio object for mic input
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=44100,
            input=True,
            frames_per_buffer=1024,
        )  # open audio stream
        self.frames = []  # list to store audio frames
        self.recording = True

        print("Recording...")

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

            print("Transcribing...")
            result = whisper_api.get_whisper_response()
            print(result["text"])

            print("Generating response...")
            response = gpt_api.get_gpt_response(result["text"])
            print(response)

            print("Generating audio...")
            audio = eleven_labs_api.get_eleven_labs_response(response)
            print("Playing audio...")
            play(audio)

    def update(self):
        if self.recording:
            try:
                data = self.stream.read(1024)  # read audio data from stream in 1024 byte chunks
                self.frames.append(data)  # add audio frame to list
            except KeyboardInterrupt:
                self.stop_recording()

        self.master.after(10, self.update)


if __name__ == "__main__":
    root = tk.Tk()
    app = DungeonBot(root)
    root.after(10, app.update)
    root.mainloop()
