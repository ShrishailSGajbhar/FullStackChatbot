import pickle
import os
from dotenv import find_dotenv, load_dotenv
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import openai
# Load the envionment variables
# load_dotenv()
from app.config import Settings
openai_api_key = Settings().openai_api_key

# The embeddings function is needed!!
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

def load_faiss_embeddings_file(embeddings_path:str):
    """
    This function returns the FAISS db vectorstore for the selected file
    """
    with open(embeddings_path, "rb") as f:
        pkl = pickle.load(f)

    # Load from the saved index
    db = FAISS.deserialize_from_bytes(
        embeddings=embeddings, serialized=pkl
    ) 
    return db 