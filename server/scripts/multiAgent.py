import sys

from scriptGen.multiAgentScript import MultiAgentScript

class MultiAgent:

    def run(name, description, keywords, subtopics, guest_name, api):
        model = MultiAgentScript(name, description ,keywords, subtopics, guest_name, api)
        return model.run()
    