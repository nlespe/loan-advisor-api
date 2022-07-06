
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:39:04 2020
@author:
"""
import uvicorn
from fastapi import FastAPI
import numpy as np
import pickle
import pandas as pd
from processing_functions import add_variable, get_client
from pydantic import BaseModel


# 2. Create the app object /  Initialize an instance of FastAPI
app = FastAPI()

#import model 
pickle_in = open("pipeline_bank.pkl","rb")
pipeline_process=pickle.load(pickle_in)

#data_train = pd.read_csv('application_train.csv')

#add_variable(data_train)

#get_client(id,data_train)
@app.get('/')
def index():
    return {'Welcome to this API for loan advisor'}

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)