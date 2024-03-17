import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from pathlib import Path
import uuid

# from .load_multiple_faiss_db import get_faiss_multipdf_knowledge_base_db
from .load_faiss_embeddings import load_faiss_embeddings_file
from .chatbot import Chatbot

from app.config import Settings
# chat_store_db_url = Settings().database_url


chatbot_router = APIRouter()

embeddings_folder_path = os.path.join(Path(__file__).parent.parent, "Embeddings")
global session_id_temp 
session_id_temp = None 

def get_chatbot_for_user_selected_file(file_path:str):
    """
    Args:
        file_path(str): e.g., "document.pdf"
    """
    filename = file_path.split(".")[0]
    file_embeddings_path = filename+".pkl"
    embeddings_path = os.path.join(embeddings_folder_path, file_embeddings_path)
    db = load_faiss_embeddings_file(embeddings_path=embeddings_path)
    
    chatbot = Chatbot(model_name="gpt-3.5-turbo", temperature=0, vectors=db)
    # create a session_id
    session_id = uuid.uuid4()
    return chatbot, session_id


@chatbot_router.post("/prepare_chatbot", description="Prepare the chatbot over user uploaded file")
async def prepare_chatbot_over_subset(uploaded_filepath: str) -> dict:

    global session_id_temp
    if uploaded_filepath=="":
        raise HTTPException(status_code=402, detail="Select a file for chatting..")
    
    # Load the FAISS embeddings
    chatbot, session_id = get_chatbot_for_user_selected_file(file_path=uploaded_filepath)
    if not chatbot:
        raise HTTPException(status_code=405, detail="Chatbot not loaded..")

    # Store the chatbot instance as a property of the router
    chatbot_router.chatbot = chatbot
    session_id_temp = session_id
    return {"status":"Chatbot is ready..!!", "session_id":session_id}

class Response(BaseModel):
    result: str | None

@chatbot_router.post("/chat", description="Chat with the prepared chatbot",response_model = Response)
async def chat_with_bot(query: str) -> dict:
    conversation_id = uuid.uuid4()
    # Check if chatbot is prepared
    if not hasattr(chatbot_router, 'chatbot'):
        raise HTTPException(status_code=405, detail="Chatbot not prepared. Use /prepare_chatbot first.")
    
    # Get the response from the chatbot
    response = chatbot_router.chatbot.conversational_chat(query, conversation_id, session_id_temp)
    
    return {"result": response}

@chatbot_router.get("/chat_history")
async def get_chat_history():
    if not hasattr(chatbot_router, 'chatbot'):
        raise HTTPException(status_code=405, detail="Chatbot not prepared. Use /prepare_chatbot first.")

    # Access the conversation history from the memory
    chat_history = chatbot_router.chatbot.chat_history

    return {"chat_history": chat_history}