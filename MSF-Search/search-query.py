
from txtai.embeddings import Embeddings
import json
embeddings = Embeddings({"path": "sentence-transformers/all-MiniLM-L6-v2"})


embeddings.load("models/vol7_index")

with open("vol7.json", "r") as f:
    data = json.load(f)["descriptions"][:100]
len(data)














search_term = "explosion at india"

res = embeddings.search(search_term, 10)
for r in res:
    print(f"Text: {data[r[0]]}")
    print(f"Similarity: {r[1]}")
    print()

