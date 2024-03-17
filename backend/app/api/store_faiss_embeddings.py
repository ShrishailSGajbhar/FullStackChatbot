import os
import pickle
from langchain.document_loaders.pdf import PyPDFLoader
from langchain.document_loaders.word_document import Docx2txtLoader
from langchain.document_loaders.text import TextLoader
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores.faiss import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings

from app.config import Settings
openai_api_key = Settings().openai_api_key
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())

def save_faiss_embeddings_file(file_path: str, embeddings_folder_path:str):
    """
    This function stores the FAISS embeddings for the filetypes containing text i.e., pdf, doc(x) and txt in the local folder named "Embeddings"

    """
    # Get the filename from filepath
    filename = os.path.basename(file_path)
    if filename.endswith('.pdf'):
        loader = PyPDFLoader(file_path=file_path)
    elif filename.endswith('.txt'):
        loader = TextLoader(file_path=file_path)
    elif filename.endswith('.docx') or filename.endswith('.doc'):
        loader = Docx2txtLoader(file_path=file_path)
    elif filename.endswith('.csv'):
        loader = CSVLoader(file_path=file_path)

    document = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    splits = text_splitter.split_documents(document)
    embeddings = OpenAIEmbeddings(openai_api_key = openai_api_key)

    if filename.endswith('.csv'):
        splits = document
    
    db = FAISS.from_documents(documents=splits, embedding=embeddings)

    pkl = db.serialize_to_bytes()

    # save the pickle file
    # first get the pdf name
    filename = os.path.basename(file_path).split(".")[0]
    savepath = os.path.join(embeddings_folder_path, filename+".pkl")
    with open(savepath, "wb") as f:
        pickle.dump(pkl, f)

