# Documentation: https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# from config import apikey, url, elevenlabs_api
from dotenv import load_dotenv
#add_background_music_to_audio
from shared.AudioMerger import merge_audio_files, add_music_based_on_sentiment #add_background_music_to_audio
from textblob import TextBlob

import time
from elevenlabs.api.error import APIError
from elevenlabs import generate

import re
import os

load_dotenv()

#Setup
apikey = os.getenv('apikey')
url = os.getenv('url')
elevenlabs_api = os.getenv('elevenlabs_api')

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

#Default voices
# HOST_VOICE = 'en-US_AllisonV3Voice'
HOST_VOICE = 'WYq8XiuI3ZWCHlgYJyXd'
GUEST_VOICE = 'en-GB_JamesV3Voice'


#Voices
voice_dict = {
    0: {'name': 'Heidi', 'code': 'en-AU_HeidiExpressive', 'description': 'Female, Australian'},
    1: {'name': 'Jack', 'code': 'en-AU_JackExpressive', 'description': 'Male, Australian'},
    2: {'name': 'Allison', 'code': 'en-US_AllisonV3Voice', 'description': 'Female, American'},
    3: {'name': 'Emma', 'code': 'en-US_EmmaExpressive', 'description': 'Female, American'},
    4: {'name': 'Lisa', 'code': 'en-US_LisaV3Voice', 'description': 'Female, American'},
    5: {'name': 'Michael', 'code': 'en-US_MichaelV3Voice', 'description': 'Male, American'},
    6: {'name': 'Charlotte', 'code': 'en-GB_CharlotteV3Voice', 'description': 'Female, British'},
    7: {'name': 'James', 'code': 'en-GB_James_3Voice', 'description': 'Male, British'},
    8: {'name': 'Kate', 'code': 'en-GB_KateV3Voice', 'description': 'Female, British'},
    9: {'name': 'Joe Rogan', 'code': 'YzVShEvNmXgfimrPg5hS', 'description': 'Joe Rogan, American'},
    10: {'name': 'Rowan Atkinson', 'code': '63QpnmWLWLkcsADaIjJL', 'description': 'Rowan Atkinson, British'},
    11: {'name': 'Lebron James', 'code': 'S7FPaLv9KoU8avlTGzdg', 'description': 'Lebron James, American'},
    12: {'name': 'Elon Musk', 'code': 'WYq8XiuI3ZWCHlgYJyXd', 'description': 'Elon Musk, American'},
    13: {'name': 'Dwayne Johnson', 'code': 'X6koFsdijBDKfhLTEoej', 'description': 'Dwayne Johnson, American'},
    14: {'name': 'Mark Zuckerberg', 'code': 'YC1myRnOQZlmLW2UCmdS', 'description': 'Mark Zuckerberg, American'},
    15: {'name': 'Steve Jobs', 'code': 'gXIAlgQovuFD9m9tkI3i', 'description': 'Steve Jobs, American'},
    16: {'name': 'Leonardo DiCaprio', 'code': 'keIYVYqLXT1lmkzMY8Ck', 'description': 'Leonardo DiCaprio, American'},
    17: {'name': 'Tom Holland', 'code': 'zU7OYQgpIH2kTwJbxAMi', 'description': 'Tom Holland, British'},
    # Add more voices as needed
}

#Default voices
# HOST_VOICE = 'en-US_AllisonV3Voice'
HOST_VOICE = voice_dict[9]['code']
# GUEST_VOICE = 'en-GB_JamesV3Voice'
GUEST_VOICE = voice_dict[12]['code']

# Example usage
text_1 = """
Host: Hello, I am your host. My name is Joe.

Guest: Hi, I am the guest. I am James!

Host: James, how have you been?

Guest: Good! It is nice to be here.

Host: Let's talk about your career! 

"""


def voice_choice(person, number):
    if number in range(17):
        print(f"Available {person} Voices:")
        for key, voice_info in voice_dict.items():
            print(f"{key}: {voice_info['name']} - {voice_info['description']}")

        selected_voice = voice_dict[number]['code']
        return selected_voice
    else:
        NotImplementedError


def remove_brackets(text):
    # Remove content inside square brackets and parentheses
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\(.*?\)', '', text)
    return text.strip()

def duo_podcast(text, host_voice, guest_voice, person1_name=None, person2_name=None):
    # Split the text into lines
    lines = text.split('\n')
    count = 0
    # Iterate through each line
    for line in lines:
        # Check if the line contains host or guest speech
        if person1_name and line.startswith(f"{person1_name}:"):
            line = line[len(person1_name) + 1:].strip()
            voice = host_voice
        elif person2_name and line.startswith(f"{person2_name}:"):
            line = line[len(person2_name) + 1:].strip()
            voice = guest_voice
        elif line.startswith("Host:"):
            line = line[6:].strip()
            voice = host_voice
        elif line.startswith("Guest:"):
            voice = guest_voice
            line = line[7:].strip()
        else:
            voice = host_voice

        # Ignore if it is empty
        if line == '':
            pass
        else:
            # Remove content inside brackets
            line = remove_brackets(line)

            if voice.startswith("en-"):
                with open(f'./speech{count}.mp3', 'wb') as audio_file:
                    res = tts.synthesize(line, accept='audio/mp3', voice=voice).get_result()
                    audio_file.write(res.content)
                    count += 1
            # ElevenLabs Voice Cloning
            else:
                generate_with_elevenlabs(line, voice, count)
                count += 1



#ElevenLabs is a great Text To Speech tool for cloning real voices
def generate_with_elevenlabs(text, voice, count):
    try:
        # Generate audio
        audio = generate(
            text=text,
            voice=voice,
            api_key=elevenlabs_api,
        )

        # Define the relative path to the tmp folder
        tmp_folder = os.path.join(os.getcwd(), "tmp")

        # Create the tmp folder if it doesn't exist
        os.makedirs(tmp_folder, exist_ok=True)

        # Save the audio to a file in the tmp folder
        with open(os.path.join(tmp_folder, f'speech{count}.mp3'), 'wb') as audio_file:
            audio_file.write(audio)
    except APIError as e:
        print(f"API Error: {e}")
        if "User not found, it is likely still being created" in str(e):
            print("Waiting for user creation to complete. Retrying in 1 minute...")
            time.sleep(60)
            generate_with_elevenlabs(text, voice)


def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    if sentiment_polarity > 0.5:
        return "Positive"
    elif sentiment_polarity < -0.5:
        return "Negative"
    else:
        return "Neutral"

# def getAudioFile(script, host_voice_number, guest_voice_number):
#     host_voice, guest_voice = voice_choice('Host', host_voice_number), voice_choice('Guest', guest_voice_number)
#     duo_podcast(script, host_voice, guest_voice)
#     merge_audio_files()
#     add_music_based_on_sentiment("final_speech.mp3", analyze_sentiment(script))

def get_audio_file(text, person1_name=None, person2_name=None):
    # change_voices = str(input(("Would you like to choose the voices for the host and the guest? Enter 'Yes' or 'No': "))).capitalize()
    change_voices = "No"
    while change_voices not in ["Yes", "No"]:
        print(change_voices)
        change_voices = str(input(
            ("Would you like to choose the voices for the host and the guest? Enter 'Yes' or 'No': "))).capitalize()

    if change_voices == "Yes":
        host_voice = voice_choice('Host')
        guest_voice = voice_choice('Guest')
    elif change_voices == "No":
        host_voice = HOST_VOICE
        guest_voice = GUEST_VOICE

    duo_podcast(text, host_voice, guest_voice, person1_name=person1_name, person2_name=person2_name)
    merge_audio_files()

    sentiment = analyze_sentiment(text)
    tmp_folder = os.path.join(os.getcwd(), "tmp")
    add_music_based_on_sentiment(os.path.join(tmp_folder, 'final_speech.mp3'), sentiment)

# if __name__ == '__main__':
#     text = '''
# Host: example script text
# '''
#     get_audio_file(text)

