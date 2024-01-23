# Documentation: https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import apikey, url
from AudioMerger import merge_audio_files


#Setup
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

#Default voices
HOST_VOICE = 'en-US_AllisonV3Voice'
GUEST_VOICE = 'en-GB_JamesV3Voice'

#Voices
voice_dict = {
    0: {'name': 'Heidi', 'code': 'en-AU_HeidiV3Voice', 'description': 'Female, Australian'},
    1: {'name': 'Jack', 'code': 'en-AU_JackV3Voice', 'description': 'Male, Australian'},
    2: {'name': 'Allison', 'code': 'en-US_AllisonV3Voice', 'description': 'Female, American'},
    3: {'name': 'Emma', 'code': 'en-US_EmmaV3Voice', 'description': 'Female, American'},
    4: {'name': 'Lisa', 'code': 'en-US_LisaV3Voice', 'description': 'Female, American'},
    5: {'name': 'Michael', 'code': 'en-US_MichaelV3Voice', 'description': 'Male, American'},
    6: {'name': 'Charlotte', 'code': 'en-GB_CharlotteV3Voice', 'description': 'Female, British'},
    7: {'name': 'James', 'code': 'en-GB_James_3Voice', 'description': 'Male, British'},
    8: {'name': 'Kate', 'code': 'en-GB_KateV3Voice', 'description': 'Female, British'},
    # Add more voices as needed
}


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
            with open(f'./speech{count}.mp3', 'wb') as audio_file:
                res = tts.synthesize(line, accept='audio/mp3', voice=voice).get_result()
                audio_file.write(res.content)
                count += 1


# Example usage
text = """
Host: Hello, I am your host. My name is Allison.

Guest: Hi, am the guest. I am James!

Host: James, how have you been?

Guest: Good! It is nice to be here.

Host: Let's talk about ...

"""

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

if __name__ == '__main__':
    main()


