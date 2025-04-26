from redis_db.client import get_redis_client
from redis_db.index import create_product_index
from data.dataset_loader import load_product_dataset
from models.embeddings import EmbeddingModel


def index_dataset(limit=None):
    r = get_redis_client()
    print(r.keys("product:*"))

    try:
        r.ft("products").dropindex(delete_documents=True)
    except:
        pass
    create_product_index(r)

    dataset = load_product_dataset(limit)
    model = EmbeddingModel()

    pipe = r.pipeline()
    for i, item in enumerate(dataset):
        # Combine title and description for embedding
        text = f"{item['category_left']} {item.get('description_left', '')}"
        embedding = model.encode(text).tobytes()

        product_data = {
            "category": str(item["category_left"]),
            "description": str(item.get("description_left", "")),
            "brand": str(item.get("brand_left", "")),
            "price": str(item.get("price_left", "")),
            "embedding": embedding
        }

        pipe.hset(f"product:{i}", mapping=product_data)

        if i % 1000 == 0 and i > 0:
            pipe.execute()
            print(f"Indexed {i} items")

    pipe.execute()
    print(f"Finished indexing {len(dataset)} products")


if __name__ == "__main__":
    index_dataset(limit=9000)  # Adjust limit as needed
