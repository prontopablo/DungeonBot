# DungeonBot

<img align="left" width="400" height="400" src="https://github.com/prontopablo/DungeonBot/assets/55544101/896df0e9-c9b5-4f4a-aa9a-9b95a28b6106">

## Introduction

DungeonBot is a little program designed to enhance your roleplaying game (D&D) experience. This is ideal for NPCs/Narrators as you can interact with an AI (GPT-3.5-Turbo) using mic input and it provides you with tailored responses with all the details of your world. DungeonBot uses the ElevenLabs voice of your choice to bring the AI's responses to life, making your sessions even more engaging and often (unintentionally) funny.

You give the AI context and instructions such as "You are in Middle Earth and are a cocky, aggressive dwarf", use your mic and get a spoken response in character from the AI (You can choose from many voices from ElevenLabs). It also keeps a chat history so the AI can remember things you've previously said (full_chat_history.json)

<br>
<br>

## Demo


https://github.com/prontopablo/DungeonBot/assets/55544101/90df9374-af0d-49f2-a4c2-bcd11b140bdd

_(Sound on)_

## Installation

_Note: Hopefully this is accessible for non-technical people, but if not, you can copy/paste these instructions into ChatGPT and have it guide you through the install!_

Follow these steps to set up DungeonBot:


1. **Download this project:**
Download this project by clicking the green code button in the top right and clicking "Download ZIP":

![image](https://github.com/prontopablo/DungeonBot/assets/55544101/0dc711b9-2ef8-48f8-8cb8-1c4a7145785d)

<br>

2. **Install Python:**
Download Python (https://www.python.org/downloads/) (any recent version will do).
When installing, check the "Add to Path" option in the installer.

![image](https://github.com/prontopablo/DungeonBot/assets/55544101/9ee3ac3e-72dd-46ab-abf5-77cfe2079d75)

<br>

3. **Install Dependencies:**
Open command prompt in the project folder and install the required dependencies:
   ```sh
   cd DungeonBot
   pip install -r requirements.txt
   ```

<br> 

4. **Get API Keys:** To interact with the AI (GPT-3.5-Turbo) and use the AI voice (ElevenLabs), you need API keys (you can think of these as personal account keys). You can obtain these keys by signing up to [GPT-3.5-Turbo](https://beta.openai.com/signup/) and [ElevenLabs](https://elevenlabs.io/). Here you can choose the voice you want to use.

<br>

5. **Configure API Keys:** Edit the "config.json" file using a text editor and add your API keys (Once you've added a voice to your voice library you can also change it to that here):
   ```env

    "GPT": {
      "api_key": "Your API key here"
    },
    "eleven_labs": {
      "api_key": "Your API key here",
      "voice": "Victoria"
    }

   ```
<br>

6. **Edit your system prompt:** Now you can give the AI context! The system prompt is the initial instructions that the AI will always bear in mind. Edit the prompt to whatever you want in the gpt_api.py file:

![image](https://github.com/prontopablo/DungeonBot/assets/55544101/3a324c65-d383-4377-8aac-30839cfb73b6)
   
<br>

7. **Run the Program:** Now you're ready to run DungeonBot. Launch the program using the following command:
   ```sh
   cd DungeonBot
   python main.py
   ```

## Usage

1. **Start the Program:** Run the program using the above command.

2. **Microphone Input:** DungeonBot will listen to your microphone input. Say your context, question, or prompt.

3. **AI Response:** The program will send your input to GPT-3.5-Turbo and retrieve an in-character response.

4. **Voice Playback:** The AI-generated response is played back using ElevenLabs' voice (remember you can choose any voice!). 

## Contributing

I welcome contributions from the community to make DungeonBot better. If you have any suggestions, bug fixes, or new features to add, feel free to create a pull request.

## Responses
Some examples of the responses provided by DungeonBot:


https://github.com/prontopablo/DungeonBot/assets/55544101/6ce943c0-4d20-45fc-a54a-d15f4e9633c0

## Credit
This project uses the GPT-3.5-Turbo API to generate text responses and the ElevenLabs API to generate the audio for those responses.

## License
This project is licensed under the MIT License.
