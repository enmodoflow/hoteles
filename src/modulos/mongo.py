# Mongodb
from pymongo import MongoClient

# Mongo URL Atlas
MONGO_URL_ATLAS = 'mongodb+srv://lolo:root@cluster0-nqj9e.mongodb.net/test?retryWrites=true&w=majority'

client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)
db = client['examen_final']
collection = db['examen_final']

