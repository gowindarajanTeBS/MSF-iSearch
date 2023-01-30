

import pdf2image
import os

class Pdf_reader():
    def __init__(self,pdf_file):
        self.pdf = pdf2image.convert_from_path(pdf_file)

    def get_data(self):
        return self.pdf,len(self.pdf)


def get_paged_from_pdf(pdf_path):
    pdf_instance = Pdf_reader(pdf_path)
    # print(pdf_path)
    doc, page_count = pdf_instance.get_data()
    # file_name = pdf_path.name
    file_name = os.path.basename(pdf_path)
    file_name = str(file_name).replace('.pdf','')
    for idx,img in enumerate(doc):
        img.save(f"{file_name}_{idx+1}.png")


get_paged_from_pdf("files/Construction_2.pdf")