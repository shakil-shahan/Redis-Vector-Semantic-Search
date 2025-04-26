from redis.commands.search.field import TextField, VectorField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from config.settings import INDEX_NAME, DOCUMENT_PREFIX, VECTOR_DIM


def create_product_index(r):
    schema = (
        TextField("category"),
        TextField("description"),
        TextField("brand"), 
        TextField("price"),
        VectorField(
            "embedding",
            "HNSW",
            {
                "TYPE": "FLOAT32",
                "DIM": VECTOR_DIM,
                "DISTANCE_METRIC": "COSINE",
                "INITIAL_CAP": 100000,
                "M": 40,
                "EF_CONSTRUCTION": 200
            }
        )
    )

    try:
        r.ft(INDEX_NAME).create_index(
            schema,
            definition=IndexDefinition(
                prefix=[DOCUMENT_PREFIX],
                index_type=IndexType.HASH
            )
        )
        return True
    except Exception as e:
        print(f"Index creation error: {e}")
        return False
