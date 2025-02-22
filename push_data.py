import os
import sys 
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")

print(MONGO_DB_URL)


import pandas as pd
import pymongo
import numpy as np

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

import certifi
ca=certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            #records=list(json.loads((data.T.to_json()).values()))
            records = list(json.loads(data.T.to_json()).values())

            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records,collection,database):
        try:
            self.database=database
            self.records=records
            self.collection=collection
            
            self.momgo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.momgo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(records)
            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=="__main__":
    FILE_PATH="network_data\phisingData.csv"
    DATABASE="ronitai"
    collection="networkdata"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records=records,collection=collection,database=DATABASE)
    print(no_of_records)
    
    