import sys

class SingleAgent:

    def run(name, keywords, api):
        if not api:
            return SingleAgent.runLocal(name, keywords)
        else:
            return SingleAgent.runOpenAI(name, keywords, api)
    
    def runLocal(name, keywords):
        # Do the generation work here
        return 'Local model results'
    
    def runOpenAI(name, keywords, api):
        # Do the generation work here
        return 'OpenAI results'
    

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