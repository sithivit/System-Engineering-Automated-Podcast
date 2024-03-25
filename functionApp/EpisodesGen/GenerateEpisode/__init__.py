import logging

from azure.functions import HttpRequest, HttpResponse

from shared.singleAgentScript import OpenAISingleAgentScript, LocalSingleAgentScript
from shared.multiAgentScript import MultiAgentScript
import shared.TextToSpeech as TextToSpeech
import shared.TextToImage as TextToImage
import shared.GenerateVideo as GenerateVideo
import shared.uploadEpisode as uploadEpisode
import shared.cleanUpFiles as cleanUpFiles

import os


def main(req: HttpRequest) -> HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        return HttpResponse("Invalid JSON format", status_code=400)
    
    # SingleAgentScript
    if str(req_body.get('single')).capitalize() == 'True':

        title = req_body.get('title')
        description = req_body.get('description')
        keywords = req_body.get('keywords')
        local = req_body.get('local')
        api = ''

        # OpenAI Model
        if str(local).capitalize() == 'False':
            api = str(req_body.get('api'))
            model = OpenAISingleAgentScript(api)
            text = model.run(title, keywords)
            # text ="""
            #     [Intro] hey hey! this is (example text) a test, lets see if it works or not! Hello! i'm Joe.         
            
            # """
            # print(text)

        # Local Model
        else:
            model = LocalSingleAgentScript()
            text = model.run(title, keywords)
            # print(text)

        

    # MultiAgentScript
    else:
        title = req_body.get('title')
        description = req_body.get('description')
        topics = req_body.get('keywords')
        guest_name = req_body.get('guestName')
        subtopics = req_body.get('subkeywords')
        local = req_body.get('local')
        api = None

        if str(local).capitalize() == 'False':
            api = str(req_body.get('api'))

        model = MultiAgentScript(title, description, topics, subtopics, guest_name, api)
        text = model.run()


    # Execute the python scripts to generate the episode
    TextToSpeech.get_audio_file(text)
    TextToImage.generate_image(text)
    GenerateVideo.generate_static_video()

    # Upload and clean up local files
    uploadEpisode.run(title, description)
    cleanUpFiles.run()


    return HttpResponse(
        "This HTTP triggered function executed successfully.",
        status_code=200
    )


