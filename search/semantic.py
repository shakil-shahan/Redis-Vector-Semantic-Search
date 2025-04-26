from redis.commands.search.query import Query
import numpy as np
from config.settings import INDEX_NAME


def semantic_search(r, model, query, top_k=5, filters=None):
    query_embedding = model.encode(query).astype(np.float32).tobytes()

    base_query = f"*=>[KNN {top_k} @embedding $vec AS score]"
    if filters:
        filter_parts = [f"@{k}:{v}" for k, v in filters.items() if v]
        if filter_parts:
            base_query = f"({' '.join(filter_parts)})=>[KNN {top_k} @embedding $vec AS score]"

    q = (
        Query(base_query)
        .return_fields("category", "description", "brand", "price", "score")
        .sort_by("score")
        .paging(0, top_k)
        .dialect(2)
    )

    return r.ft(INDEX_NAME).search(q, query_params={"vec": query_embedding})
