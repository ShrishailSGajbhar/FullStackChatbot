from datetime import datetime
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI

from app.config import Settings
openai_api_key = Settings().openai_api_key

class Chatbot:

    def __init__(self, model_name, temperature, vectors):
        self.model_name = model_name
        self.temperature = temperature
        self.vectors = vectors
        self.chat_history = []

    def conversational_chat(self, query, conversation_id, session_id):
        """
        Starts a conversational chat with a model via Langchain
        """
        self.chat_history.extend([{"session_id":session_id, "conversation_id":conversation_id, "role": "user", "content": query, "timestamp":datetime.utcnow().isoformat()}])
        chain = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(model_name=self.model_name, 
                           temperature=self.temperature, 
                           openai_api_key=openai_api_key),
            memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True),
            retriever=self.vectors.as_retriever(),
        )

        result = chain({"question": query, "chat_history": self.chat_history})
        answer = result["answer"]

        self.chat_history.extend([{"session_id":session_id, "conversation_id":conversation_id, "role": "assistant", "content": result["answer"], "timestamp":datetime.utcnow().isoformat()}])
        return answer
        
