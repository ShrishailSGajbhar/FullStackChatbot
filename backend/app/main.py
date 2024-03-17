from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import upload_file
from app.api import prepare_chatbot

origins = ["*"]

def create_application() -> FastAPI:
    application = FastAPI()

    # Enable CORS with specific origins, methods, and headers
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Update this list with your frontend's actual origin(s)
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(upload_file.upload_router)
    application.include_router(prepare_chatbot.chatbot_router)

    return application

app = create_application()
