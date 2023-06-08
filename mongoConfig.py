from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = os.getenv('MONGO_URI')
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
   message = print("MongoDB Connected Successfully!")
   # Create the database for our example (we will use the same database throughout the tutorial
#    return client['user_shopping_list']
   return message
  
   
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()



