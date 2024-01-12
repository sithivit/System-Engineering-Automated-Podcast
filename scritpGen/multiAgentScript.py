from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.llms import GPT4All
from langchain.prompts import PromptTemplate
from langchain import OpenAI

class MultiAgentScript:
    def __init__(self, title, description, topic, subtopics, guest_name, api=None):

        self.podcast_title = title
        self.podcast_description = description
        self.podcast_host_name = "Joe"
        self.podcast_guest_name = guest_name
        self.podcast_topic = topic 
        self.podcast_subtopics = subtopics 
        self.podcast_language = "English"

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
            Always respond in {podcast_language}."
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
        """

        self.KICKOFF_PROMPT = """
            Start the conversation repeating something like this:
            ¡Hello! Welcome to the podcast '{podcast_title}', '{podcast_description}'. 
            My name is '{podcast_host_name}' and today we're going to talk with {podcast_guest}. 
            To discuss this topic, we have an expert on the subject.
            What is your name and what do you do?
        """

        if api != None:
            self.llm = OpenAI(
                temperature=0,
                openai_api_key=api,
                model_name="text-davinci-003"
            )
        else:
            local_path = "./models/gpt4all-falcon-q4_0.gguf"  

            # Callbacks support token-wise streaming
            callbacks = [StreamingStdOutCallbackHandler()]

            # Verbose is required to pass to the callback manager
            self.llm = GPT4All(model=local_path, callbacks=callbacks, max_tokens=1024)
            self.memeory = ConversationBufferMemory(memory_key="chat_history")


    def start_conversation(self):
        conversation_buf = ConversationChain(llm=self.llm, memory=ConversationBufferMemory())


agent = MultiAgentScript("AI", "AI revolution", "Technology", "computer science", "Elon Musk", "")




