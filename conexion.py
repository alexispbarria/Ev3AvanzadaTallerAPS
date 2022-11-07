from pymongo import MongoClient

def get_db():
    try:
        client = MongoClient("mongodb+srv://vdap:tallerapp@vdap.63iet4f.mongodb.net/VDAP?retryWrites=true&w=majority")
        db = client.VDAP
    except ConnectionError:
        print("Error de conexión")
    return db