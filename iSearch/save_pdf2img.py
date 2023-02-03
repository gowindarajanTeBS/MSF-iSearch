
#working
# from PIL import Image
# import PyPDF2
# import glob, os
#
# os.chdir("files/")
#
# for file in glob.glob("*.pdf"):
#     print(file)
#     try:
#         pdf_file_name = file
#         # Open the pdf file
#         with open(pdf_file_name, 'rb') as f:
#             # Create a pdf reader object
#             pdf_reader = PyPDF2.PdfReader(f)
#
#             # Get the number of pages in the pdf
#             num_pages = len(pdf_reader.pages)
#             # loop through first two pages
#             for i in range(min(2, num_pages)):
#                 # Get the page object
#                 page = pdf_reader.pages[i]
#
#                 # Create an XObject from the page's contents
#                 xObject = page['/Resources']['/XObject'].get_object()
#
#                 # loop through the XObjects
#                 for obj in xObject:
#                     # Extract the image
#                     if xObject[obj]['/Subtype'] == '/Image':
#                         size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
#                         data = xObject[obj].get_data()
#                         if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
#                             mode = "RGB"
#                         else:
#                             mode = "P"
#
#                         # Save the image
#                         img = Image.frombytes(mode, size, data)
#                         file_name = pdf_file_name.replace(".pdf","") + "_"f'page_{i}.jpg'
#                         img.save(file_name)
#
#     except Exception as e:
#         print(e)
#



import pdf2image
import os

class Pdf_reader():
    def _init_(self,pdf_file):
        self.pdf = pdf2image.convert_from_path(pdf_file)

    def get_data(self):
        return self.pdf,len(self.pdf)

Pdf_reader = Pdf_reader().

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