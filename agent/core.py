from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from agent.memory import get_memory
import os

openai_api_key=os.environ["OPENAI_API_KEY"]

def create_agent():
    llm = ChatOpenAI(model="gpt-3.5-turbo",
                     openai_api_key="openai_api_key" )
    memory = get_memory()
    return ConversationChain(llm=llm, memory=memory, verbose=True)
