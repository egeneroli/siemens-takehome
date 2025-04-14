import os
from langchain.chains import ConversationChain, LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from app.config import Env

class ChatService:
    def __init__(self) -> None:
        """
        Initialize the ChatService with an optional API key.
        If api_key is not provided, we try to read from environment var.
        """
        if not Env.GOOGLE_API_KEY:
            raise ValueError("Google Gemini API key not found in environment.")

        # create chain components
        self.prompt: PromptTemplate = PromptTemplate(
            input_variables=["input", "history"],
            template="History: {history}\nUser: {input}\nAssistant:"
        )
        self.llm: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(model=Env.LANGUAGE_MODEL, temperature=0.7)
        self.memory: ConversationBufferMemory = ConversationBufferMemory()

        # create chain
        self.chain: ConversationChain = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            prompt=self.prompt
        )
        #self.chain: LLMChain = LLMChain(llm=self.llm, prompt=self.prompt)


    def get_reply(self, prompt: str) -> str:
        """
        Takes user prompt and returns an LLM response using LangChain.
        """
        if not prompt:
            return "No prompt provided."

        return self.chain.run(input=prompt)
