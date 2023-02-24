
import csv
import pandas as pd
from nltk import tokenize

# excel_file = "D:\Projects\MSF-Search\db_data\MSF_iSearchDB_no_content.csv"
excel_file = "D:\Govind\Official\Projects\MSF\iSearch\db_data\output.xlsx"

# df = pd.read_csv(excel_file)
df = pd.read_excel(excel_file)

def extract_sentence_index(input_string, excel_file=excel_file):


    all_matched_records = []
    # all_text = " ".join(df["FileName"].astype(str))
    for index, row in df.iterrows():

        sentence = str(row["RawOCR"]).lower()
        # sentences = all_text.split(".")
        sentences = tokenize.sent_tokenize(sentence)
        for sentence in sentences:
            if input_string in sentence:
                # all_matched_records.append(index,sentence)

                selected_rows = df.iloc[index].to_dict()
                selected_rows["index"] = index
                selected_rows["match_sentence"] = sentence
                all_matched_records.append(selected_rows)
                break

                # return sentence,index
    return all_matched_records

    return None


# # tests
# input_string = "Protection CPS"
# # excel_file = "file.xlsx"
# sentence = extract_sentence_index(input_string, excel_file)
# if sentence:
#     print(f"The sentence is: {sentence}")
# else:
#     print("The input string was not found in the Excel file.")

