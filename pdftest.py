import os
import fitz

# specify the path to the PDF file
pdf_path = "TestPaperGut.pdf"

# open the PDF file
doc = fitz.open(pdf_path)
meta = doc.metadata
toc = doc.get_toc()
i = 0
for page in doc:
  x = page.get_text('html')
  i += 1
  if i == 3:
    print(x)
    break


