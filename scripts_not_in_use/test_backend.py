import sys

class TestBackend:
    def run(name, keywords):
        # Do the generation work here
        return 'generated ' + name + ' ' + keywords
    
if __name__ == "__main__":
    args = sys.argv[1:]
    name = str(args[0])
    keywords = str(args[1])
    print(TestBackend.run(name, keywords))