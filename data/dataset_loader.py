from datasets import load_dataset


def load_product_dataset(limit=None):
    dataset = load_dataset(
        "wdc/products-2017",
        split="train+test+validation",
        trust_remote_code=True
    )

    print(dataset.features)
    print(dataset[0]) # Show first item's structure

    if limit:
        actual_limit = min(limit, len(dataset))
        if actual_limit != limit:
            print(f"Warning: Reduced limit from {limit} to {actual_limit}")
        return dataset.shuffle(seed=42).select(range(actual_limit))
    return dataset
