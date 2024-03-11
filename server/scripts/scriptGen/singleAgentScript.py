from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import GPT4All
from langchain.prompts import PromptTemplate
from documentParser.rag_utils import similarity_search
import os
import sys
import openai

from ..audioGen import TextToSpeech

class LocalSingleAgentScript:
    def __init__(self):

        # local_path = "/models/gpt4all-falcon-q4_0.gguf"  
        local_path = os.getcwd()+"\\scripts\\scriptGen\\models\\mistral-7b-openorca.gguf2.Q4_0.gguf"

        callbacks = [StreamingStdOutCallbackHandler()]

        self.llm = GPT4All(model=local_path, callbacks=callbacks, max_tokens=1024)
        self.memeory = ConversationBufferMemory(memory_key="chat_history")

        self.tts = TextToSpeech


    def enrich_brainstorm_with_rag(self, specific_topics):
        # Example function to query RAG system and retrieve relevant content
        # This is a placeholder - actual implementation would query the RAG system
        result = similarity_search(specific_topics)
        relevant_docs = ["Document content relevant to " + result]  # This should be replaced with actual RAG query results
        return relevant_docs
        
        
    def brain_storm(self, podcast_name, specific_topics):
        relevant_docs = self.enrich_brainstorm_with_rag(specific_topics)
        enriched_context = " ".join(relevant_docs)
        brain_storming_template = """ 
            
            The scripts should also be related to the following topics {topics}
            Based on our research, here is some relevant information: {enriched_context}
            Please expand on this idea and write a brief paragraph in the form of a premise: {name}
            """

        prompt = PromptTemplate(template=brain_storming_template, input_variables=["name", "topics", "enriched_context"])
        
        llm_chain = LLMChain(prompt=prompt, llm=self.llm)
        brain_storm = llm_chain.run({
            "name": podcast_name, 
            "topics": specific_topics
            })

        return brain_storm

    def expand_premises(self, brain_storm):
        template = """
            Please write 3 podcast segement ideas for an episode based on this premise: {premise}
        """

        prompt = PromptTemplate(template=template, input_variables=["premise"])
        llm_chain = LLMChain(prompt=prompt, llm=self.llm)
        three_para = llm_chain.run({"premise": brain_storm})

        segments = three_para.strip().split('\n')
        return segments[0], segments[1], segments[2]

    def expand_segments(self, segment):
        template = """
            Act as a solo podcast scriptwriter. 
            Don't write Host and Segment.
            Don't write this as a conversation between two people.
            
            Talk more on the points

            Expand this point into a podcast script: {segment}
        """

        prompt = PromptTemplate(template=template, input_variables=["segment"])
        llm_chain = LLMChain(prompt=prompt, llm=self.llm)

        expanded_para = llm_chain.run({"segment": segment})
        return expanded_para

    def run(self, name, specific_topics):
        brain_storm = self.brain_storm(name, specific_topics)
        segment1, segment2, segment3 = self.expand_premises(brain_storm)

        para1 = self.expand_segments(segment1)
        para2 = self.expand_segments(segment2)
        para3 = self.expand_segments(segment3)

        full_text = para1 + para2 + para3
        return full_text

class OpenAISingleAgentScript():
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def enrich_brainstorm_with_rag(self, specific_topics):
        # Example function to query RAG system and retrieve relevant content
        # This is a placeholder - actual implementation would query the RAG system
        result = similarity_search(specific_topics)
        relevant_docs = ["Document content relevant to " + result]  # This should be replaced with actual RAG query results
        return relevant_docs

    def brain_storm(self, podcast_name, specific_topics):
        relevant_docs = self.enrich_brainstorm_with_rag(specific_topics)
        enriched_context = " ".join(relevant_docs)
        brain_storming_template = f""" 
            The scripts should also be related to the following topics: {specific_topics}
            Based on our research, here is some relevant information: {enriched_context}
            Please expand on this idea and write a brief paragraph in the form of a premise: {podcast_name}
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125", 
            messages=[{"role": "system", "content": brain_storming_template}]
        )
        return response.choices[0].message['content']

    def expand_premises(self, brain_storm):
        template = f"""
            Please write 3 podcast segment ideas for an episode based on this premise: {brain_storm}
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[{"role": "system", "content": template}]
        )

        segments = response.choices[0].message['content'].strip().split('\n')
        return segments[0], segments[1], segments[2]

    def expand_segments(self, segment):
        template = f"""
            Act as a solo podcast scriptwriter. 
            Don't write Host and Segment.
            Don't write this as a conversation between two people.
            
            Talk more on the points

            Expand this point into a podcast script: {segment}
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[{"role": "system", "content": template}]
        )

        return response.choices[0].message['content']

    def run(self, name, specific_topics):
        brain_storm = self.brain_storm(name, specific_topics)
        segment1, segment2, segment3 = self.expand_premises(brain_storm)

        para1 = self.expand_segments(segment1)
        para2 = self.expand_segments(segment2)
        para3 = self.expand_segments(segment3)

        full_text = para1 + para2 + para3
        return full_text

if __name__ == "__main__" :

    args= sys.argv[1:]

    title = args[0]
    keywords = args[1]
    local = args[2]
    api = ''

    if local == 'false':
        api = str(args[3])
        model = OpenAISingleAgentScript(api)
        print(model.run(title, keywords))
        # text = model.run(title, keywords)
        # TextToSpeech.main(text)

    else:
        model = LocalSingleAgentScript()
        print(model.run(title, keywords))