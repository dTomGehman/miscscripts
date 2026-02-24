#usage:  python pdfsplice.py [file1, file2,...]
#pdfs are joined in the order that they are listed.  
#if none are specified, all pdfs found in the folder are spliced together.  
#output is out.pdf

from PyPDF2 import PdfReader, PdfWriter
from sys import argv
import os

pdf_writer = PdfWriter()
if len(argv)>1:
  for path in argv[1:]:
    pdf_reader = PdfReader(path)
    for page in pdf_reader.pages:
        # Add each page to the writer object
        pdf_writer.add_page(page)
else:
    for file in os.listdir("."):
        filename = os.fsdecode(file)
        if filename.endswith(".pdf"):
            pdf_reader = PdfReader(filename)
            for page in pdf_reader.pages:
                # Add each page to the writer object
                pdf_writer.add_page(page)

# Write out the merged PDF
with open("out.pdf", 'wb') as out:
    pdf_writer.write(out)
