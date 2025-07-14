import os,sys,json
from dotenv import load_dotenv
import certifi
import pandas as pd
import numpy as np
import pymongo
from  network_security.exceptions.exceptions import networksecurityexception
from network_security.logging.logger import logging

load_dotenv()
MONGO_DB_URL=os.getenv("URL")
ca=certifi.where()
class NetworkDataExt():

    def __init__(self):
        try:
            pass
        except Exception as e:
            raise networksecurityexception(e,sys)
        
    def cv_to_json(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=json.loads((data.to_json(orient="records")))
            return records
        except Exception as e:
            raise networksecurityexception(e,sys)
    
    def insert_data_mongo(self,records,database,collection):
        try:
            self.database=database
            self.records=records
            self.collection=collection
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise networksecurityexception(e,sys)
        
if __name__=='__main__':
    File_path="Network_data\phisingData.csv"
    DATABASE="AP"
    collection="NetworkData"
    Networkobj=NetworkDataExt()
    records= Networkobj.cv_to_json(File_path)
    print(records)
    no_of_records=Networkobj.insert_data_mongo(records,DATABASE,collection)
    print(no_of_records)
