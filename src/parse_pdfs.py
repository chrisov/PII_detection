import pdfplumber
import logging

logging.getLogger("pdfminer").setLevel(logging.ERROR)

def extract_text_from_pdf(pdf_path):
	"""
	Extract text from PDF, preserving layout somewhat
	
	Returns:
		text: Plain text string
		metadata: Character positions (for mapping back to PDF)
	"""
	
	text_content = ""
	with pdfplumber.open(pdf_path) as pdf:
		for page_num, page in enumerate(pdf.pages):
			page_text = page.extract_text()
			
			if page_text:
				text_content += page_text + "\n"
	
	return text_content

if __name__ == "__main__":
	text = extract_text_from_pdf("../data/pdfs/Bank_of_Austria/Bank_of_Austria_1.pdf")
	print(f"\n{text}")
