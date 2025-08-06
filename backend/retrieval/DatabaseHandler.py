import chromadb
from chromadb.utils import embedding_functions

COLLECTIONS_PATH = "/Users/jakobschiller/Desktop/Projekte/AI_Uni_Agent/backend/retrieval/collections"
EMBED_MODEL = "all-MiniLM-L6-v2"

class DatabaseHandler():
    def __init__(self):
        self.persistent_client = chromadb.PersistentClient(
            path=COLLECTIONS_PATH
        )
        self.distance_function = "cosine" # Alternativen wäre z.B. Skalarprodukt
        self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBED_MODEL)

    def create_collection(self, collection_id) -> chromadb.Collection:
        collection_name = collection_id
        return self.persistent_client.create_collection(
            name= collection_name,
            metadata={"hnsw:space": self.distance_function},
            embedding_function=self.embedding_function
        )
    
    def add_to_collection(self, collection: chromadb.Collection, chunks):
        collection.add(
            documents=chunks,
            ids=[f"id_{i}" for i in range(0, len(chunks))]
        )
        
    def get_collection(self, collection_id) -> chromadb.Collection:
        try:
            return self.persistent_client.get_collection(collection_id)
        except ValueError as e:
            return None