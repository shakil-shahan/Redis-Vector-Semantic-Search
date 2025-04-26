from redis_db.client import get_redis_client
from models.embeddings import EmbeddingModel
from search.semantic import semantic_search


def main():
    r = get_redis_client()
    model = EmbeddingModel()

    while True:
        query = input("Enter search query (or 'quit' to exit): ").strip()
        if query.lower() == 'quit':
            break

        results = semantic_search(r, model, query=query, top_k=3)

        print(f"\nResults for '{query}':")
        for i, doc in enumerate(results.docs):
            print(f"{i+1}. {doc.category} (Score: {float(doc.score):.3f})")
            print(f"   Brand: {doc.brand}")
            print(f"   Price: {doc.price}")
            print(f"   {doc.description[:100]}...\n")


if __name__ == "__main__":
    main()
