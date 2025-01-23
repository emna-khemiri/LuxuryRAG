from fastapi import FastAPI
from pydantic import BaseModel
from src.chatbot import ChatBot

# Initialize the chatbot
chat_bot = ChatBot(vector_store_path='./VectorStore/')

app = FastAPI()

# Create a Pydantic model to accept the user's query
class Query(BaseModel):
    question: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the LuxuryRAG Chatbot API!"}

@app.post("/ask")
def ask_question(query: Query):
    """
    Endpoint to ask a question to the chatbot and get an answer along with chat history
    """
    answer, history = chat_bot.process_chat(query.question)
    return {
        "answer": answer,
        "chat_history": history["chat_history"]
    }
