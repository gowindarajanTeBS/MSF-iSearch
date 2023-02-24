
from transformers import pipeline
import pandas as pd
import requests


data = {"Actors": ["Brad Pitt", "Leonardo Di Caprio", "George Clooney"], "Number of movies": ["87", "53", "69"]}

table = pd.DataFrame.from_dict(data)
question = "how many movies does Leonardo Di Caprio have?"

tqa = pipeline(task="table-question-answering", model="google/tapas-large-finetuned-wtq")

print("TEST RESPONSE",tqa(table=table, query=question)['cells'][0])
print()


def download_csv(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        with open("../datasets/table_data.csv", "wb") as f:
            f.write(response.content)
    else:
        raise Exception("Failed to download the CSV file")


def table_predict(csv_url,question):
    download_csv(csv_url)
    return_dict = {}
    df = pd.read_csv("../datasets/table_data.csv")
    df = df.astype(str)
    table_result = tqa(table=df, query=question)
    return_dict.update(table_result)
    table_result_dict = df.iloc[table_result['coordinates'][0][0]].to_dict()
    return_dict.update(table_result_dict)
    return return_dict

# tests
# df = pd.read_csv("datasets/table_data.csv", sep=',', header=0)
# print(tqa(table=df, query=question))

