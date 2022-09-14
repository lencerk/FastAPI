#Here we are doing all of our classic imports

from fastapi import FastAPI#required to use fast api u need to instatiate
from fastapi.params import Body#to be able to send json payload with a body
from pydantic import BaseModel#fast api thing required
from typing import Optional#t5o specify parameters
import pyodbc#to make connection to sql server
import pandas#data science lib
from typing import Union# -----
import uuid#GUID
from datetime import datetime
import bcrypt#secure api
from cryptography.fernet import Fernet#secure api
from passlib.context import CryptContext

app = FastAPI()
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"r"Server=LENCER-ASUS\SQLEXPRESS;""Database=Brilliware;""Trusted_Connection=yes;")
pwd_context =  CryptContext(schemes=["bcrypt"], deprecated="auto")		
class User(BaseModel):
	id : str
	username: str
	Password : str

def hash(password):
	try:
		return pwd_context.hash(password)
		
	except Exception as e:
		return {"error":str(e)}

#THIS IS THE DEFAULT ENDPOINT THAT WILL GO AND CHECK IF ALL CONNECTIONS TO THE DATABASE ARE UP AND RUNNING 
@app.get("/")
def root():
	try:

		return {"message":'API Active, waiting for requests'}
	except Exception as e:
		return {"error":str(e)}


@app.post("/add_user")
def addUser(user :User):
	try:
		new_user = User(id =str(uuid.uuid4()),
						username=user.username,
						Password=f'{hash(user.Password)}') #str(hash(user.Password)))




		# query = str("exec  BrilliwareHrRegister "+str(new_user.username)+","+str(new_user.Password))
		# cursorz = cnxn.cursor()
		# s = pandas.read_sql_query(query,cnxn)
		# cursorz.commit()
		return {"Response":new_user.Password}
	except Exception as e:
		return {"error":str(e)}

