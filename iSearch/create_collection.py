

from qdrant_client import QdrantClient
from qdrant_client.http import models

client = QdrantClient(host="localhost", port=6333)

client.recreate_collection(
    collection_name="MSF_iSearch_Collection",
    vectors_config=models.VectorParams(size=100, distance=models.Distance.COSINE),
)