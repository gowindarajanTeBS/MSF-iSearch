import json
import base64

# Open the JSON file
with open('your_table.json', 'r') as f:
    json_data = json.load(f)

# Loop through all the objects in the JSON
for data in json_data:
    file_content = data["FileContent"]
    file_name = data["FileName"]

    # Decode the "FileContent" from base64
    decoded_file = base64.b64decode(file_content)

    # Save the decoded "FileContent" as a pdf file with "FileName" as the filename
    filename = "files/"+file_name #+ '.pdf'
    with open(filename, 'wb') as f:
        f.write(decoded_file)

