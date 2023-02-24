

from qdrant_client import QdrantClient
from qdrant_client.http import models

client = QdrantClient(host="localhost", port=6333)

client.recreate_collection(
    collection_name="MSF_iSearch_Collection",
    vectors_config=models.VectorParams(size=768, distance=models.Distance.COSINE),
)



# # create index
#
# client.create_payload_index(
#     collection_name="msf_text_collection",
#     field_name="raw_ocr",
#     field_schema=models.TextIndexParams(
#         type="text",
#         tokenizer=models.TokenizerType.WORD,
#         min_token_len=1,
#         max_token_len=15,
#         lowercase=True,
#     )
# )