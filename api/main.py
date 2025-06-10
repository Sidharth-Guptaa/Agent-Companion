from fastapi import FastAPI
from pydantic import BaseModel
from agent.core import create_agent

app = FastAPI()
agent = create_agent()

class Message(BaseModel):
    input: str

@app.post("/chat")
def chat(msg: Message):
    response = agent.run(msg.input)
    return {"response": response}