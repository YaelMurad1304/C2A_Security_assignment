
import fitz

# Function to read text from pdf file
def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(pdf_file)
    for page in doc:
        text += page.get_text()
    return text

# PDF files paths
pdf_file1 = 'pdf_1.pdf'
pdf_file2 = 'pdf_2.pdf'

# Extract text from both PDF files
text1 = extract_text_from_pdf(pdf_file1)
text2 = extract_text_from_pdf(pdf_file2)

# Compare the text
if text1 == text2:
    print("The PDFs have the same text.")
else:
    print("The PDFs have different text.")