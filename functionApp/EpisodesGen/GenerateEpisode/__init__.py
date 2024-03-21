import logging

from azure.functions import HttpRequest, HttpResponse

from shared.singleAgentScript import OpenAISingleAgentScript, LocalSingleAgentScript
import shared.TextToSpeech as TextToSpeech
import shared.TextToImage as TextToImage
import shared.GenerateVideo as GenerateVideo
import shared.uploadEpisode as uploadEpisode
import shared.cleanUpFiles as cleanUpFiles

import os


def main(req: HttpRequest) -> HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    title = req.params.get('title')
    description = req.params.get('description')
    keywords = req.params.get('keywords')
    local = req.params.get('local')
    api = ''

    if local == 'false':
        api = str(req.params.get('api'))
        model = OpenAISingleAgentScript(api)
        text = model.run(title, keywords)
        # text ="""
        #     [Intro] hey hey! this is (example text) a test, lets see if it works or not! Hello! i'm Joe.         
        # """
        # print(text)

    else:
        model = LocalSingleAgentScript()
        text = model.run(title, keywords)
        # print(text)

    TextToSpeech.get_audio_file(text)
    TextToImage.generate_image(text)
    GenerateVideo.generate_static_video()

    uploadEpisode.run(title, description)
    cleanUpFiles.run()


    return HttpResponse(
        "This HTTP triggered function executed successfully.",
        status_code=200
    )
