web:gunicorn -w 4 -k uvicorn.workers.uvicornWorker main:app
heroku ps:scale web=1
