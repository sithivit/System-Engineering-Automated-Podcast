from parlai.core.teachers import register_teacher, DialogTeacher
from parlai.scripts.display_data import DisplayData
import os

@register_teacher("my_teacher")
class MyTeacher(DialogTeacher):
    def __init__(self, opt, shared=None):
        # opt is the command line arguments.
        
        # What is this shared thing?
        # We make many copies of a teacher, one-per-batchsize. Shared lets us store 
        
        # We just need to set the "datafile".  This is boilerplate, but differs in many teachers.
        # The "datafile" is the filename where we will load the data from. In this case, we'll set it to
        # the fold name (train/valid/test) + ".txt"
        opt['datafile'] = opt['datatype'].split(':')[0] + ".txt"
        super().__init__(opt, shared)
    
    def setup_data(self, datafile):
        # filename tells us where to load from.
        # We'll just use some hardcoded data, but show how you could read the filename here:

        for file in os.listdir("dataset"):
            new_episode = True
            with open('dataset\\' + file, 'r') as f:
                readlines = f.readlines()
                first, second = None, None
                length = len(readlines)
                counter = 1
                while counter < length:
                    if first == None:
                        first = readlines[counter]
                    elif second == None:
                        second = readlines[counter]
                    counter += 3
                    if first != None and second != None:
                        if new_episode:
                            yield (first, second), True
                            new_episode = False
                            first, second = None, None
                        else:
                            yield (first, second), False
                            first, second = None, None


DisplayData.main(task="my_teacher", num_examples=5)