from sentence_transformers import SentenceTransformer
import numpy as np
from config.settings import EMBEDDING_MODEL


class EmbeddingModel:
    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def encode(self, text):
        if not text or str(text).lower() == "nan":
            text = ""
        return self.model.encode(text).astype(np.float32)
