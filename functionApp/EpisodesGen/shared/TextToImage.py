import os
import base64
import requests
from dotenv import load_dotenv

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

load_dotenv()

api_key = os.getenv('STABILITY_API_KEY')
api_host = "https://api.stability.ai"
engine_id = "stable-diffusion-v1-6"

# Comment this out once downloaded
nltk.download("punkt")
nltk.download("stopwords")

def extract_keywords(text, num_keywords=7):
    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

    # Calculate word frequencies
    word_freq = Counter(filtered_tokens)

    # Extract top keywords
    keywords = [word for word, _ in word_freq.most_common(num_keywords)]

    return keywords

def generate_image(text):
    if api_key is None:
        raise Exception("Missing Stability API key.")

    keywords = extract_keywords(text)

    #==============================================================
    response = requests.post(f"{api_host}/v1/generation/{engine_id}/text-to-image", headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        }, json={
            "text_prompts": [
                {
                    "text": f"Generate a realistic image with a central object representing {', '.join(keywords)}. "
                            f"Please ensure there is only one central object, and do not include any text in the image."

                }
            ],
            "cfg_scale": 5,
            "clip_guidance_preset": "FAST_BLUE",
            "height": 512,
            "width": 512,
            "samples": 1,
            "steps": 15,
    })
    #==============================================================
    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))
    data = response.json()
    image = data["artifacts"][0]  # Take the first image

    # Construct the path to save the image in the 'tmp' folder
    tmp_folder = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'tmp')
    image_path = os.path.join(tmp_folder, 'text_to_image.png')

    with open(image_path, "wb") as f:
        f.write(base64.b64decode(image["base64"]))


# Example usage: Change it to the text variable
# text = "Cats are fluffy. I like to watch cats play."
# text = """"[Intro] hey hey! this is (example text) a test, lets see if the music works or not! Hello! i'm Elon
#         Cats are fluffy. I like to watch cats play."""


 # if __name__ == '__main__':
 #      generate_image(text)
