
from pymilvus import ( 
    connections,
)
from config.environment import AppConfig
from utils.backofRetry import retryBackof 

def connect():
    connections.connect("default", host=getattr(AppConfig, "MILVUS_HOST", "localhost"), port=getattr(AppConfig, "MILVUS_PORT", "19530"))

def connectMilvus():
    print("Connect to milvus...")

    try:
        retryBackof(connect)
    except:
        print("Connect milvus fail")
        return

    print("Connect milvus successful")
    from models.user import createIndex
    createIndex()
