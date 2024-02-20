# Documentation: https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import apikey, url, elevenlabs_api
from AudioMerger import merge_audio_files, add_music_based_on_sentiment #add_background_music_to_audio
from textblob import TextBlob

import time
from elevenlabs.api.error import APIError
from elevenlabs import generate


#Setup
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

#Default voices
HOST_VOICE = 'en-US_AllisonV3Voice'
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
    9: {'name': 'Joe Rogan', 'code': 'BkUZzkMAAPP1NeOSx3Gz', 'description': 'Joe Rogan, American'}, #SFqBacV9QmTgExZ0UzU4
    #10: {'name': 'AT', 'code': 'gJIoR7EUWm3sBsEIIFEr', 'description': 'at, American'}
    # Add more voices as needed
}

# Example usage
text = """
Host: Hello, I am your host. My name is Joe.

Guest: Hi, I am the guest. I am James!

Host: James, how have you been?

Guest: Good! It is nice to be here.

Host: Let's talk about your career! 

"""


def voice_choice(person):
    print(f"Available {person} Voices:")
    for key, voice_info in voice_dict.items():
        print(f"{key}: {voice_info['name']} - {voice_info['description']}")

    choice = int(input(f"Choose the {person} voice by entering the corresponding number: "))

    if choice not in voice_dict:
        print("Invalid choice. Please enter a valid number.")
        choice = voice_choice(person)

    selected_voice = voice_dict[choice]['code']
    return selected_voice


def duo_podcast(text, host_voice, guest_voice):
    # Split the text into lines
    lines = text.split('\n')
    count = 0
    # Iterate through each line
    for line in lines:
        # Check if the line contains host or guest speech
        if line.startswith("Host:"):
            line = line[6:].strip()
            voice = host_voice
        elif line.startswith("Guest:"):
            voice = guest_voice
            line = line[7:].strip()
        #Ignore if it is empty
        if line == '':
            pass
        #Make an audio file for each line
        else:
            if voice.startswith("en-"):
                with open(f'./speech{count}.mp3', 'wb') as audio_file:
                    res = tts.synthesize(line, accept='audio/mp3', voice=voice).get_result()
                    audio_file.write(res.content)
                    count += 1
            #ElevenLabs Voice Cloning
            else:
                generate_with_elevenlabs(line, voice, count)
                count +=1


#ElevenLabs is a great Text To Speech tool for cloning real voices
def generate_with_elevenlabs(text, voice, count):
        try:
            # Generate audio
            audio = generate(
                text=text,
                voice=voice,
                api_key=elevenlabs_api,
            )

            # Save the audio to a file
            with open(f'./speech{count}.mp3', 'wb') as audio_file:
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


def main():
    change_voices = str(input(("Would you like to choose the voices for the host and the guest? Enter 'Yes' or 'No': "))).capitalize()
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

    duo_podcast(text, host_voice, guest_voice)
    merge_audio_files()

    sentiment = analyze_sentiment(text)
    add_music_based_on_sentiment("final_speech.mp3", sentiment)


if __name__ == '__main__':
    main()


