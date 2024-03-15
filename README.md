# ProtonDatalabs AI developer Assignment - Chatbot application

## Preface

At ProtonDatalabs, we leverage cutting-age gen-AI solutions to deliver buisness value to our clients. We are able to do this by combining aspects from AI modelling to full-stack developement.

In this assignment, your task is to build a chatbot application which takes a file as an input and answers user's query. The goal of this application is to accurately provide answers based on the uploaded file. This application could be used as an assistant to quickly answer questions or summarize facts from files containing large amounts of text data, making our lives easier.

## Project structure

In this project you find 2 directories

1. `backend` containing the server side **python** code
2. `frontend` containing the client side **typescript** code.\
   In both these directories, it is your job to complete the missing modules and add necessary functionalities to make the app fully functional.

### Backend

**Requirements**: Python 3.10 or above. We will test your submission against Python 3.10.

1. `main.py` which is the entry point to our server
2. This project has a few Python packages as dependencies, you can install them in your virtual environment using `requirements.txt`. If you were to use other dependencies, then please add them to `requirements.txt`.
3. We will be using [`conda`](https://docs.conda.io/projects/conda/en/stable/) package manager to create a virtual environment `chatbot` using `conda create -n chatbot python=3.10` and then `conda activate chatbot` to activate the environment.
4. Then install the python packages using `pip install -r requirements.txt`

#### Running the backend server

To launch the server, navigate to the `backend` directory and run:

##### `uvicorn main:app --reload`

This will start the server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Frontend

The project structure within the `frontend` directory follows the official `create-react-app` structure as in the [docs](https://create-react-app.dev/docs/folder-structure). Some of the files have been removed for convenience & brevity.

**Requirements**: We are using `node V20.11.1` and `npm 10.2.4`. They can be downloaded via [installer](https://nodejs.org/en). For more information check [here](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

#### How to launch the react app

1. Navigate to the `frontend` directory and run `npm install`
2. Then you can run:

   ##### `npm start`

   This will launch the app in development mode.\
   Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits. You will also see any lint errors in the console.

## The assignment

### Backend

1. Currently, the server returns `hello world!` everytime user makes a query, which needs to be changed. Modify the `/predict` endpoint to acheive this. You are free to use any architecture here: API based or open-source LLMs. The end goal in either case is to have a meaningful result based on the user query and uploaded file.
2. Implement the storage and handling of the incoming files from the frontend. You can use any database management system like MongoDB or MySQL for this.

### Frontend

1. Add a pop up which notifies that the file has been uploaded properly.
2. Extend the app's functionality to accept `.txt`,`.docx` & `.pdf` files in addition to `.csv` files.
3. Add some styling to the bare bones app structure. You are free to use any popular CSS frameworks like Tailwind or UI libraries like Material or Chakra UI. Bonus points for creative and innovative designs.

## Note

1. We expect that the app behaves similar to real world applications we interact with everyday. So think from the point of view of a user and handle all the possible edge cases which may occur while running the app. For instance, you can think of cases when the user has uploaded a very large file (>100mb) or a unsupported file type like video/mp3.
2. **Important** We want you to uphold your best programming practices (SOLID, OOPs, type hints) for the completion of this assignment, as if your code would end up in production and interact with other software components. A robust solution which covers fewer points will be judged more favourably than a complete solution that cuts corners.
3. We will check your assignment by doing a full run of your app with all possible edge cases and see how the results look. Please ensure the program is in a finished state so that we can execute even though you might not have
   completed it in full.
4. Finally, be sure to provide a `README` document detailing your approach to completing the assignment, including the decisions you took and the reasons behind them.
