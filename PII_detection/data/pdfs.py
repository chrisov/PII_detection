from pathlib import Path as _Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from playwright.sync_api import sync_playwright
from PII_detection.config import ensure_directory

def generate_pdfs(account, i, config):

	template_dir = ensure_directory(_Path(config.get("INPUT_DIR", "data/samples/html")))
	output_dir = ensure_directory(_Path(config.get("OUTPUT_DIR", "data/synthetic")))

	env = Environment(
		loader=FileSystemLoader(str(template_dir)),
		autoescape=select_autoescape(["html", "xml"])
	)

	with sync_playwright() as p:
		browser = p.chromium.launch()
		page = browser.new_page()
		try:
			template = env.get_template(account._name + ".html")
			renderer = template.render(
				iban=account._iban,
				bic=account._bic,
				person=account._holder,
				transactions=getattr(account._statement, "_history", []),
				statement=account._statement
			)

			template_output_dir = output_dir / account._name
			template_output_dir.mkdir(parents=True, exist_ok=True)
			name = template_output_dir / f"{account._name}_{i}.html"
			with open(name, "w", encoding="utf-8") as f:
				f.write(renderer)

			pdf_file = name.with_suffix(".pdf")
			page.goto(name.resolve().as_uri(), wait_until="networkidle", timeout=30_000)
			page.pdf(path=str(pdf_file), format="A4", print_background=True)
			try:
				name.unlink()
			except Exception:
				raise FileNotFoundError("Failed to remove intermediate HTML %s", name)
		finally:
			try:
				browser.close()
			except Exception:
				raise KeyError("Failed to close browser")

	