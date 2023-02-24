#
# # Import client library
from qdrant_client import QdrantClient

qdrant_client = QdrantClient(host='localhost', port=6333)
# qdrant_client.recreate_collection(
#     collection_name='startups',
#     vector_size=768,
#     distance="Cosine"
# )
#
# import numpy as np
# import json
#
# fd = open('./startups.json')
#
# # payload is now an iterator over startup data
# payload = map(json.loads, fd)
#
# # Here we load all vectors into memory, numpy array works as iterable for itself.
# # Other option would be to use Mmap, if we don't want to load all data into RAM
# vectors = np.load('./startup_vectors.npy')
#
#
# qdrant_client.upload_collection(
#     collection_name='startups',
#     vectors=vectors,
#     payload=payload,
#     ids=None,  # Vector ids will be assigned automatically
#     batch_size=256  # How many vectors will be uploaded in a single request?
# )
#




# medium script

# qdrant_client.recreate_collection(
#   collection_name='startups',
#   vectors_config=models.VectorParams(size=768, distance="Cosine")
# )
#

import numpy as np
import json, re

fd = open('db_data/msf_isearch.json')

# payload is now an iterator over startup data
payload = map(json.loads, fd)


def remove_whitespaces(json_file):
  with open(json_file, 'r') as f:
    data = json.load(f)

  for i, item in enumerate(data):
    # Replace newline characters and tabs with a single space
    item['RawOCR'] = re.sub(r'[\n\t]+', ' ', item['RawOCR'])
    # Remove extra spaces
    item['RawOCR'] = re.sub(r' +', ' ', item['RawOCR'])
    data[i] = item

  return data

cleaned_json = remove_whitespaces('db_data/msf_isearch.json')

# Here we load all vectors into memory, numpy array works as iterable for itself.
# Other option would be to use Mmap, if we don't want to load all data into RAM
vectors = np.load('db_data/msf_vectors.npy')

# And the final step - data uploading
qdrant_client.upload_collection(
  collection_name='MSF_iSearch_Collection',
  vectors=vectors,
  payload=cleaned_json,
  ids=None,  # Vector ids will be assigned automatically
  batch_size=256  # How many vectors will be uploaded in a single request?
)

