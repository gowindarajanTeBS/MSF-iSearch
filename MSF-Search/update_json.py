
import json
import pytesseract
from PIL import Image

# Set the path of the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open the JSON file
with open('your_table.json', 'r') as f:
    json_data = json.load(f)

# Loop through all the objects in the JSON
for data in json_data:
    file_name = data["FileName"]

    # Open the pdf file from the "files" folder
    file_path = "files/" + file_name #+ ".pdf"
    with Image.open(file_path) as img:
        # Use Pytesseract to extract the OCR text from the pdf
        ocr_text = pytesseract.image_to_string(img)

    # Remove the "FileContent" field from the JSON object
    data.pop("FileContent", None)
    # Add the "RawOCR" field with the OCR text
    data["RawOCR"] = ocr_text

# Write the updated JSON object to a file
with open('your_table.json', 'w') as f:
    json.dump(json_data, f)
