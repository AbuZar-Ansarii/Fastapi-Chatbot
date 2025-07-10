from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


class ChatBot:
    def __init__(self):
        self.llm_model = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            api_key=api_key,
            temperature=0.7  # optional: adjust creativity
        )
        self.parser = StrOutputParser()
        self.system_template = "You are a helpful Ayurveda assistant. Solve the patient's query: {query}"

        self.prompt = PromptTemplate(
            template=self.system_template,
            input_variables=["query"]
        )

        # Create LangChain pipeline
        self.llm_chain = self.prompt | self.llm_model | self.parser

    def query_response(self, question: str) -> dict:
        response = self.llm_chain.invoke({"query": question})
        return {
            "question": question,
            "answer": response
        }


# Instantiate chatbot
bot_system = ChatBot()
