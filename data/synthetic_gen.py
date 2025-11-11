import bank_statement as bs
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from playwright.sync_api import sync_playwright
import logging

# Resolve config path - try a few common locations (repo root ./config and ./data/config)
candidate_paths = [
	Path(__file__).resolve().parent.parent / "config" / "config.json",  # repo_root/config/config.json
	Path(__file__).resolve().parent / "config" / "config.json",         # data/config/config.json (next to this script)
]

CONFIG_PATH = None
for p in candidate_paths:
	if p.exists():
		CONFIG_PATH = p
		break

if CONFIG_PATH is None:
	tried = ", ".join(str(p) for p in candidate_paths)
	raise FileNotFoundError(f"Config file not found. Tried: {tried}")

with open(CONFIG_PATH) as f:
	config = json.load(f)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_pdfs():
	# Resolve templates and results dirs relative to the repository root when paths are relative
	repo_root = CONFIG_PATH.parent.parent
	template_dir = Path(config.get("templates_dir", "templates/html"))
	if not template_dir.is_absolute():
		template_dir = (repo_root / template_dir).resolve()

	results_dir = Path(config.get("results_dir", "results"))
	if not results_dir.is_absolute():
		results_dir = (repo_root / results_dir).resolve()

	env = Environment(
		loader=FileSystemLoader(str(template_dir)),
		autoescape=select_autoescape(["html", "xml"])
	)

	iterations = int(config.get("iterations", 1))

	# Ensure deterministic ordering of templates
	template_files = sorted(template_dir.glob("*.html"))

	with sync_playwright() as p:
		browser = p.chromium.launch()
		page = browser.new_page()
		try:
			for template_file in template_files:
				for i in range(1, iterations + 1):
					logger.info("Rendering template %s (iteration %d)", template_file.name, i)
					statement = bs.statement()
					person = getattr(statement, "_holder", None)

					template = env.get_template(template_file.name)
					renderer = template.render(
						person=person,
						transactions=getattr(statement, "_history", []),
						statement=statement
					)

					output_dir = results_dir / template_file.stem
					output_dir.mkdir(parents=True, exist_ok=True)
					name = output_dir / f"{template_file.stem}_{i}.html"
					with open(name, "w", encoding="utf-8") as f:
						f.write(renderer)

					pdf_file = name.with_suffix(".pdf")
					# Use file:// URI and wait for network idle to ensure assets are loaded
					page.goto(name.resolve().as_uri(), wait_until="networkidle", timeout=30_000)
					page.pdf(path=str(pdf_file), format="A4", print_background=True)
					# Remove the intermediate HTML file now that the PDF has been created
					try:
						name.unlink()
						logger.info("Removed intermediate HTML %s", name)
					except Exception:
						logger.exception("Failed to remove intermediate HTML %s", name)
		finally:
			try:
				browser.close()
			except Exception:
				logger.exception("Failed to close browser")

if __name__ == "__main__":
	generate_pdfs()

	