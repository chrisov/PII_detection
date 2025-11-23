# from transformers import AutoTokenizer, AutoModelForTokenClassification
# from transformers import pipeline

# # 1. Define the input text
# sample_text = (
#     "Throughout this review period, Alex demonstrated exceptional proficiency in leading the Q3 implementation initiative, successfully steering the project to completion two weeks ahead of schedule. Their proactive approach to identifying and resolving logistical bottlenecks significantly contributed to the team's overall efficiency and minimized potential cross-departmental delays. Furthermore, Alex consistently exhibits a high degree of collaborative spirit, serving as a reliable and valued resource for their peers. Moving forward, a key area for development will be to refine strategic communication when interacting with executive leadership to ensure maximum clarity on project status and resource needs."
# )

# # 2. Load the NER pipeline
# # We specify the 'ner' task and use a pre-trained model based on DistilBERT.
# # This particular model (dslim/distilbert-base-cased-NER-v1) is optimized
# # for the standard CoNLL-2003 entity types: PER, ORG, LOC, MISC.
# try:
# 	tokenizer = AutoTokenizer.from_pretrained("dslim/distilbert-NER")
# 	model = AutoModelForTokenClassification.from_pretrained("dslim/distilbert-NER")
# 	# Using a known, fast DistilBERT-based NER model
# 	ner_pipeline = pipeline(
# 		"ner",
# 		model=model,
# 		tokenizer=tokenizer,
# 		aggregation_strategy="simple"
# 	)

# 	print("--- Input Text ---")
# 	print(sample_text)
# 	print("\n--- NER Results (Aggregated) ---")

# 	# 3. Process the text and get the entities
# 	entities = ner_pipeline(sample_text)

# 	# 4. Print the results clearly
# 	for entity in entities:
# 		print(f" 	Word: '{entity['word']}'")
# 		print(f"	Type: {entity['entity_group']}")
# 		print(f"	Score: {entity['score']:.4f}")
# 		print("-" * 20)

# except ImportError:
#     print("Error: The 'transformers' library is not installed.")
#     print("Please run: pip install transformers")
# except Exception as e:
#     print(f"An error occurred: {e}")


from PII_detection.data import synthetic_gen
if __name__ == "__main__":
	synthetic_gen.synthetic_gen()