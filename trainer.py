from parlai.core.teachers import register_teacher, DialogTeacher
from parlai.scripts.display_data import DisplayData
import os

@register_teacher("joe_rogan")
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


from parlai.scripts.train_model import TrainModel

TrainModel.main(
    task="joe_rogan",
    model='transformer/generator',
    model_file='model/model', 

    init_model='zoo:tutorial_transformer_generator/model',
    n_heads=16, n_layers=8, n_positions=512, text_truncate=512,
    label_truncate=128, ffn_size=2048, embedding_size=512,
    activation='gelu', variant='xlm',
    dict_lower=True, dict_tokenizer='bpe',
    dict_file='zoo:tutorial_transformer_generator/model.dict',
    learn_positional_embeddings=True,
    
    # some training arguments, specific to this fine-tuning
    # use a small learning rate with ADAM optimizer
    lr=1e-5, optimizer='adam',
    warmup_updates=100,
    # early stopping on perplexity
    validation_metric='ppl',
    # train at most 10 minutes, and validate every 0.25 epochs
    max_train_time=600, validation_every_n_epochs=0.25,
    
    # depend on your gpu. If you have a V100, this is good
    batchsize=12, fp16=True, fp16_impl='mem_efficient',
    
    # speeds up validation
    skip_generation=True,
    
    # helps us cram more examples into our gpu at a time
    dynamic_batching='full',
)