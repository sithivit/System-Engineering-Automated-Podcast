from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.llms import GPT4All
from langchain.prompts import PromptTemplate

import random
import openai

import logging
import os
from dotenv import load_dotenv
load_dotenv()


from shared.documentParser.rag_utils import similarity_search

# api = openai_api_key = os.environ.get("OPENAI_API_KEY")
api = None

class MultiAgentScript:
    def __init__(self, title, description, topic, subtopics, guest_name, api=api):

        self.podcast_title = title
        self.podcast_description = description
        self.podcast_host_name = "Joe"
        self.podcast_guest_name = guest_name
        self.podcast_topic = topic 
        self.podcast_subtopics = subtopics 
        self.podcast_language = "English"

        self.knowledge = similarity_search(title + description)

        self.HOST_PERSONALITY_PROMPT = """ 
            Your a podcast host of a conversational podcast named {podcast_title}. You're a bit of a nerd,
            but you're also very friendly and approachable. You're very interested in
            {podcast_topic} and you're excited to learn more about it. You're not an expert, but
            you're not a novice either. You're a great interviewer and you're 
            good at asking questions and keeping the conversation going.
            You always come up with thought-provoking interview questions.
            Your conversation style is informal, assertive and casual. 
        """

        self.HOST_INSTRUCTIONS_PROMPT = """
            Interview the user about their experience with {podcast_topic}. Keep questions short and 
            to the point. Ask at least two questions about each sub topics such as: {podcast_subtopics}.
            Don't present yourself to the audience or the guest, they already know who you are.
            Don't present the podcast to the audience or the guest, they already know what the podcast is about.
            Always respond in {podcast_language}.

            Always reply with '{name}: '

            Knowledge: {knowledge}
        """

        self.GUEST_PERSONALITY_PROMPT = """
            Your a complete caricature of an expert obsessed about {podcast_topic}, 
            like a character out of the show Silicon Valley. Your profession is a traditional ocuppation 
            but related to {podcast_topic}. You're overly confident 
            about your knowledge about {podcast_topic} and think that it will solve all of humanity's problems. 
            You constantly talk about how 'innovative' and 'cutting-edge' you are, 
            even if you don't really understand what you are talking about. 
            You believe that {podcast_topic} will revolutionate the entire universe and you are excited about that prospect.
        """

        self.GUEST_INSTRUCTIONS_PROMPT = """
            Entertain the user by portraying an over-the-top caricature of a {podcast_topic} expert.
            You should engage the user on subtopics such as {podcast_subtopics}.
            Your responses should always be dominated by the outsize and humorous
            personality. Err on the side of eye-rolling humor.
            Keep answers short and to the point. Don't ask questions.
            Always respond in {podcast_language}.

            Always reply with '{name}: '

            Knowledge: {knowledge}
        """

        self.KICKOFF_PROMPT = """
            Start the conversation repeating something like this:
            '{podcast_host_name}: Hello! Welcome to the podcast {podcast_title}, {podcast_description}. My name is {podcast_host_name} and today we're going to talk with {podcast_guest}. To discuss this topic, we have an expert on the subject.

            (Do not generate HTML style output)

        """

        if api != None:
            openai.api_key = api
            self.llm = openai.ChatCompletion
        else:
            local_path = os.path.join(os.getcwd(), "shared", "llm_models", "mistral-7b-openorca.gguf2.Q4_0.gguf")

            # Callbacks support token-wise streaming
            callbacks = [StreamingStdOutCallbackHandler()]

            # Verbose is required to pass to the callback manager
            self.llm = GPT4All(model=local_path, callbacks=callbacks, max_tokens=2048)
            self.memeory = ConversationBufferMemory(memory_key="chat_history")

    def generate_response(self, prompt, history):
        """
        Generates a response from the LLM based on the provided prompt.
        """
        # If using OpenAI's API
        if not isinstance(self.llm, GPT4All):
            response = self.llm.create(
                    messages=[
                        {"role": "system", "content": prompt},
                        {"role": "user", "content": history}
                    ],
                    model="gpt-3.5-turbo",
                )
            return response.choices[0].message.content

        # If using a local GPT-4 model
        else:
            response = self.llm.generate([prompt])
            return response.generations[0][0].text

    def generate_prompt(self, template, **kwargs):
        """
        Generate a prompt based on the provided template and additional context.
        """
        return template.format(**kwargs)

    def start_podcast(self):
        """
        Starts the podcast conversation using the KICKOFF_PROMPT.
        """
        kickoff_prompt = self.generate_prompt(
            self.KICKOFF_PROMPT,
            podcast_title=self.podcast_title,
            podcast_description=self.podcast_description,
            podcast_host_name=self.podcast_host_name,
            podcast_guest=self.podcast_guest_name
        )
        return self.generate_response(kickoff_prompt, "")

    def switch_role(self, role):
        """
        Switches between the host and guest roles and updates the conversation prompts accordingly.
        """
        if role.lower() == 'host':
            self.current_role = 'host'
            self.current_personality_prompt = self.HOST_PERSONALITY_PROMPT.format(podcast_title=self.podcast_title, podcast_topic=self.podcast_topic)
            self.current_instructions_prompt = self.HOST_INSTRUCTIONS_PROMPT.format(
                podcast_topic=self.podcast_topic, podcast_subtopics=self.podcast_subtopics, podcast_language=self.podcast_language, knowledge=self.knowledge, name=self.podcast_host_name)
        elif role.lower() == 'guest':
            self.current_role = 'guest'
            self.current_personality_prompt = self.GUEST_PERSONALITY_PROMPT.format(podcast_topic=self.podcast_topic)
            self.current_instructions_prompt = self.GUEST_INSTRUCTIONS_PROMPT.format(
                podcast_topic=self.podcast_topic, podcast_subtopics=self.podcast_subtopics, podcast_language=self.podcast_language, knowledge=self.knowledge, name=self.podcast_guest_name)
        else:
            raise ValueError("Invalid role. Choose 'host' or 'guest'.")

    def run(self, num_exchanges=2):
        """
        Runs through the logic to create a podcast script.
        """
        script = []
        script.append(self.start_podcast())

        # Alternate roles for each exchange
        for i in range(num_exchanges):
            speaker = None
            if i % 2 != 0:
                self.switch_role('host')
                prompt = self.HOST_PERSONALITY_PROMPT + self.HOST_INSTRUCTIONS_PROMPT
                speaker = self.podcast_host_name
            else:  
                self.switch_role('guest')
                prompt = self.GUEST_PERSONALITY_PROMPT + self.GUEST_INSTRUCTIONS_PROMPT
                speaker = self.podcast_guest_name

            # Generate conversation based on the role
            formatted_prompt = self.generate_prompt(
                prompt,
                podcast_title=self.podcast_title,
                podcast_topic=self.podcast_topic,
                podcast_subtopics=self.podcast_subtopics,
                podcast_language=self.podcast_language,
                knowledge=self.knowledge,
                name=speaker
            )

            response = self.generate_response(formatted_prompt, '\n'.join(script))
            script.append(response)

            # Include a subtopic occasionally (optional)
            #if random.random() < 0.3:  # 30% chance to include a subtopic
            #    subtopic_script = self.include_subtopic()
            #    script.append(subtopic_script)

        return '\n'.join(script)




