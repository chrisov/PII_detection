import bank_statement as bs
import json
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

def generate_htmls():
	with open("config/config.json") as f:
		config = json.load(f)
		template_dir = Path(config["templates_dir"])
	env = Environment(
		loader=FileSystemLoader(str(template_dir)),
		autoescape=select_autoescape(['html', 'xml'])
	)

	for template_file in template_dir.glob("*.html"):
		for i in range(1, config["iterations"] + 1):
			statement = bs.statement()
			person = statement._holder
			template = env.get_template(template_file.name)
			renderer = template.render(
				person=person,
				transactions=statement._history,
				statement=statement
			)
			output_dir = Path(config["results_dir"]) / template_file.stem
			output_dir.mkdir(parents=True, exist_ok=True)
			name = output_dir / f"{template_file.stem}_{i}.html"
			with open(name, "w", encoding="utf-8") as f:
				f.write(renderer)


if __name__ == "__main__":
	generate_htmls()	

	