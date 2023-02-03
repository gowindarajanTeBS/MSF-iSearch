# import pytesseract
# import pandas as pd
# from PIL import Image
#
# # Load the CSV file into a pandas DataFrame
# df = pd.read_csv("db_data/MSF_iSearchDB_no_content.csv")
#
# # Loop through each row in the DataFrame
# for index, row in df.iterrows():
#     file_name = row["FileName"]
#     file_path = f"files/{file_name}"
#
#     # Perform OCR on the PDF file
#     raw_text = pytesseract.image_to_string(Image.open(file_path))
#
#     # Save the raw text to the "RawOCR" field in the DataFrame
#     df.at[index, "RawOCR"] = raw_text
#
# # Save the updated DataFrame to a new CSV file
# df.to_csv("db_data/output.csv", index=False)


import pytesseract
import pandas as pd
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("db_data/MSF_iSearchDB_no_content.csv")

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    file_name = row["FileName"]
    file_path = f"files/{file_name}"

    # Convert the PDF file to a list of images
    images = convert_from_path(file_path,poppler_path="D:/Govind/Official/Projects/MSF iSearch/poppler-23.01.0/Library/bin")

    # Initialize an empty string to store the raw text
    raw_text = ""

    # Loop through each page in the PDF file
    for image in images:
        # Perform OCR on the page
        page_text = pytesseract.image_to_string(image)

        # Add the page text to the raw text
        raw_text += page_text

    # Save the raw text to the "RawOCR" field in the DataFrame
    df.at[index, "RawOCR"] = raw_text

# Save the updated DataFrame to a new CSV file
df.to_csv("db_data/output.csv", index=False)
df.to_excel("db_data/output.xlsx", index=False)