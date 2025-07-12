import os
import sys
import json
from dotenv import load_dotenv
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

load_dotenv()

MONGO_URL = os.getenv("MONGO_DB_URL")

ca= certifi.where()

class NetworkDataExtractor:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_converter(self, file_path):
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"The file {file_path} does not exist.")
            
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            json_data = df.to_json(orient='records')
            return json.loads(json_data)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_to_mongo(self, data, db, collection_name):
        try:
            if not data:
                raise ValueError("No data to insert into MongoDB.")
            
            client = pymongo.MongoClient(MONGO_URL, tlsCAFile=ca)
            database = client[db]
            collection = database[collection_name]
            result = collection.insert_many(data)
            logging.info(f"Data inserted successfully into {collection_name} collection in {db} database.")
            return result.inserted_ids
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

if __name__ == "__main__":
    try:
        extractor = NetworkDataExtractor()
        file_path = "/Users/MU20414673/Krish_Naik_Project/NETWORKSECURITY/Network_Data/phisingData.csv"  
        json_data = extractor.csv_to_json_converter(file_path)
        
        db_name = "network_security_db"  # Replace with your database name
        collection_name = "network_data"  # Replace with your collection name
        
        inserted_ids = extractor.insert_data_to_mongo(json_data, db_name, collection_name)
        logging.info(f"Inserted IDs: {inserted_ids}")
    except NetworkSecurityException as e:
        logging.error(f"An error occurred: {e}")