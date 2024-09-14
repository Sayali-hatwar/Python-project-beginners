from PyPDF2 import PdfReader , PdfWriter

## Read the existing file
pdf = PdfReader('test.pdf')

# create reference 
pdfwriter = PdfWriter()

# Add pages with loop
for page_num in range(len(pdf.pages)):
    page = pdf.pages[page_num]
    pdfwriter.add_page(page)
   
# encrypt the file
password = '12345'
pdfwriter.encrypt(password)

# create new file
with open('test1.pdf','wb') as f:
    pdfwriter.write(f)
    
# close the file
f.close()    
    