
import csv
import pandas as pd
from nltk import tokenize

excel_file = "D:\Govind\Official\Projects\MSF iSearch\MSF-iSearch\db_data\output.xlsx"

def extract_sentence_index(input_string, excel_file=excel_file):
    # df = pd.read_csv(excel_file)
    df = pd.read_excel(excel_file)
    # all_text = " ".join(df["FileName"].astype(str))
    for index, row in df.iterrows():
        sentence = str(row["RawOCR"])
        # sentences = all_text.split(".")
        sentences = tokenize.sent_tokenize(sentence)
        for sentence in sentences:
            if input_string in sentence:
                return sentence,index
    return None


# # tests
# input_string = "OAuth"
# # excel_file = "file.xlsx"
# sentence = extract_sentence_index(input_string, excel_file)
# if sentence:
#     print(f"The sentence is: {sentence}")
# else:
#     print("The input string was not found in the Excel file.")

