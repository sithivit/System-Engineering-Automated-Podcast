from pymongo import MongoClient
from bson import Binary

def run(title):
    
    # Connect to MongoDB
    client = MongoClient('mongodb+srv://team2:gSbSMx9UfrLg70ng@cluster0.bw9vipj.mongodb.net/?retryWrites=true&w=majority')
    db = client['podcastdb']
    collection = db['Episode']

    # Read the audio file in binary mode
    with open('final_speech.mp3', 'rb') as f:
        audio_data = f.read()

    # Convert the binary data to BSON
    binary_data = Binary(audio_data)

    # Insert the audio data into the collection
    collection.insert_one({
        'title': title,
        'description': '',
        'audio': binary_data
    })