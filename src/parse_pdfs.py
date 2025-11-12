import pdfplumber
import logging
import json
from pathlib import Path

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
		for page in pdf.pages:
			page_text = page.extract_text()
			if page_text:
				text_content += page_text + "\n"
	
	return text_content

def extract_text():
	try:
		CONFIG_PATH = "../config/config.json"
		with open(CONFIG_PATH) as f:
			config = json.load(f)
		input_dir = Path(config.get("input_dir", "../data/pdfs"))

		for path in input_dir.rglob("*"):
			if path.is_dir():
				output_dir = Path(config.get("output_dir", "extraction")) / path.name
				output_dir.mkdir(parents=True, exist_ok=True)
				for file in path.rglob("*"):
					with open(output_dir / (file.name).replace(".pdf", ""), "w", encoding="utf-8") as f:
						f.write(extract_text_from_pdf(file))
	except:
		raise FileNotFoundError(f"Config file not found. Tried: {CONFIG_PATH}")

if __name__ == "__main__":
	extract_text()

