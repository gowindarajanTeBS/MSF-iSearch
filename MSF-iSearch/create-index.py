from txtai.embeddings import Embeddings
import json

embeddings = Embeddings({"path": "sentence-transformers/all-MiniLM-L6-v2"})

with open("vol7.json", "r") as f:
    data = json.load(f)["descriptions"][-100:]
len(data)

txtai_data = []
i = 0
for text in data:
    txtai_data.append((i, text, None))
    i = i + 1
print(len(txtai_data))
txtai_data[0]

embeddings.index(txtai_data)
res = embeddings.search("arson", 10)

res = embeddings.search("knife", 10)
for r in res:
    print(f"Text: {data[r[0]]}")
    print(f"Similarity: {r[1]}")
    print()

embeddings.save("models/vol7_index_v2")
