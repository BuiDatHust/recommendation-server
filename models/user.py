from pymilvus import (FieldSchema, DataType, CollectionSchema,Collection )

fields = [
    FieldSchema(name="id", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=50),
    FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=8)
]

schema = CollectionSchema(fields, "user")

user = Collection("user", schema, consistency_level="Strong")

def createIndex():
    index = {
    "index_type": "IVF_FLAT",
    "metric_type": "L2",
    "params": {"nlist": 128},
    }
    user.create_index("embeddings", index)