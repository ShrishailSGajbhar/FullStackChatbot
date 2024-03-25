# Full Stack Chatbot application

## Technology Stack

* Frontend: React (with TypeScript)
* Backend: FastAPI (Python)
* Deployment: Docker & Docker Compose

In this project, we build a chatbot application which takes a document file (pdf, txt, docx, csv) as an input and answers user's query. The goal of this application is to accurately provide answers based on the uploaded file. This application could be used as an assistant to quickly answer questions or summarize facts from files containing large amounts of text data, making our lives easier.

## Project structure

In this project you find 2 directories

1. `backend` containing the server side **python** code
2. `frontend` containing the client side **typescript** code.

## How to run using local virtual environment 
### Backend

**Requirements**: 

* Python 3.10 or above.
* OpenAI API key 

1. `main.py` which is the entry point to our server
2. This project has a few Python packages as dependencies, you can install them in your virtual environment using `requirements.txt`.
3. We will be using [`conda`](https://docs.conda.io/projects/conda/en/stable/) package manager to create a virtual environment `chatbot` using `conda create -n chatbot python=3.10` and then `conda activate chatbot` to activate the environment.
4. Then install the python packages using `pip install -r requirements.txt`

**Important:** Make sure to rename the `.env.template` file in `backend/app` directory to `.env` and add your openai api key for error free deployment. 

#### Running the backend server

To launch the server, navigate to the `backend` directory and run:

##### `uvicorn main:app --reload`

This will start the server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Frontend

The project structure within the `frontend` directory follows the official `create-react-app` structure as in the [docs](https://create-react-app.dev/docs/folder-structure). 

**Requirements**: We are using `node V20.11.1` and `npm 10.2.4`. They can be downloaded via [installer](https://nodejs.org/en). For more information check [here](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

#### How to launch the react app

1. Navigate to the `frontend` directory and run `npm install`
2. Then you can run:

   ##### `npm start`

   This will launch the app in development mode.\
   Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits. You will also see any lint errors in the console.

## How to run using docker compose

* Run the command `docker-compose up -d` to start the frontend and backend containers. 
* Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the Swagger UI
* Open [http://localhost:3000](http://localhost:3000) to access the frontend UI

## Demo

Click on the image below to see the demo 👇

[![Click here to see the demo](https://img.youtube.com/vi/bHc8UxhjPog/0.jpg)](https://www.youtube.com/watch?v=bHc8UxhjPog)

## TODO

1. Handle edge cases when the user has uploads a very large file (>100mb) or a unsupported file type like video/mp3.