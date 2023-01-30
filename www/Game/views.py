from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

import pymongo

client = pymongo.MongoClient('mongodb+srv://username:password@HOSTNAME/DATABASE_NAME?authSource=admin&tls=true&tlsCAFile=<PATH_TO_CA_FILE>')

#Define Db Name
dbname = client['admin']

#Define Collection
collection = dbname['mascot']

mascot_1={
    "name": "Sammy",
    "type" : "Shark"
}

collection.insert_one(mascot_1)

mascot_details = collection.find({})

for r in mascot_details:
    print(r['name'])