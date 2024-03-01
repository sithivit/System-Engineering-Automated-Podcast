import sys

from scriptGen.singleAgentScript import LocalSingleAgentScript, OpenAISingleAgentScript

class SingleAgent:

    def run(name, keywords, api):
        if not api:
            return SingleAgent.runLocal(name, keywords)
        else:
            return SingleAgent.runOpenAI(name, keywords, api)
    
    def runLocal(name, keywords):
        # Do the generation work here
        script = LocalSingleAgentScript().run(name, keywords)
        return script
    
    def runOpenAI(name, keywords, api):
        # Do the generation work here
        script = OpenAISingleAgentScript(api).run(name, keywords)
        return script
    

if __name__ == "__main__":

    args = sys.argv[1:]
    name = str(args[0])
    keywords = str(args[1])
    local = args[2]
    api = ''
    
    if local == 'false':
        api = str(args[3])
    
    print(SingleAgent.run(name, keywords, api))

    # print(SingleAgent.run(name, keywords, api))