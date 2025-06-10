from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from agent.memory import get_memory
import os

API_KEY = os.environ["OPENAI_API_KEY"]

def create_agent():
    llm = ChatOpenAI(model="gpt-3.5-turbo",
                     openai_api_key= API_KEY,
                     max_tokens=1000,
                     temperature=0.5,
                     top_p=0.9)
    memory = get_memory()
    return ConversationChain(llm=llm, memory=memory, verbose=True)
