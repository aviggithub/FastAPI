# FastAPI
Learn How to Create RESTful API in python using FastAPI


### Run the following command in terminal to 
install FastAPI, Uvicorn, Gunicorn and databases packages
pip install fastapi uvicorn gunicorn databases[postgresql] pydantic
### Run the FastAPI app:-
uvicorn --port 8000 --host 127.0.0.1 app5:app --reload

### post url :- http://127.0.0.1:8000/postdata/

### add cors enbale in fastapi
make async to request

### add background task
http://127.0.0.1:8000/doc :- documentation

### add main menu for run file uvicorn server(ASGI) - done run file python app.py
 integrate socket.io with your FastAPI app
 uvicorn app:app --reload
