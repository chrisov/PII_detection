# from faker import Faker

# fake = Faker()

# print("-" * 20 + "\n")
# for i in range(10):
# 	text = f"Customer {fake.name()} with email {fake.email()} lives at {fake.address()}."
# 	print(f"{i}: {text}")
# 	print("\n" + "-" * 20 + "\n")

	
import re
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
from faker import Faker

# --- 1. Setup ---
# Initialize the Presidio Analyzer for PII detection
analyzer = AnalyzerEngine()

# Initialize the Presidio Anonymizer
anonymizer = AnonymizerEngine()

# Initialize Faker for generating realistic, fake PII
fake = Faker()

# Define the original, sensitive text
original_text = (
    "Customer service received an email from John Doe at john.doe@mail.com. "
    "He lives in Seattle and his phone is 555-123-4567. "
    "He requested a refund on order #1A2B3."
)

# --- 2. Define Custom Anonymization Operators using Faker ---
# We define custom replacement functions (lambdas) that use Faker to generate
# realistic, non-real PII for the specific entity types.
operator_mapping = {
    "PERSON": OperatorConfig("custom", {"lambda": lambda x: fake.name()}),
    "EMAIL_ADDRESS": OperatorConfig("custom", {"lambda": lambda x: fake.email()}),
    "LOCATION": OperatorConfig("custom", {"lambda": lambda x: fake.city()}),
    "PHONE_NUMBER": OperatorConfig("custom", {"lambda": lambda x: fake.phone_number()}),
    # Any other detected entity not explicitly listed will be redacted by default
    "DEFAULT": OperatorConfig("redact", {"new_value": "[ANONYMIZED_ENTITY]"}),
}

# --- 3. Analysis and Anonymization (Synthetic Generation) ---

# Step A: Analyze the text to find PII
print("--- Original Text ---")
print(original_text)

print("\n--- PII Analysis Results (Start/End/Type/Confidence) ---")
analyzer_results = analyzer.analyze(text=original_text, language='en')
for result in analyzer_results:
    print(f"  Res: {result}")
    # print(f"  {result.entity_type}: {result.start}-{result.end} (Score: {result.score:.2f})")

# Step B: Anonymize the text using the custom Faker operators
anonymized_text = anonymizer.anonymize(
    text=original_text,
    analyzer_results=analyzer_results,
    operators=operator_mapping
).text

# --- 4. Output Synthetic Data ---
print("\n--- Synthetic Data Generated ---")
print(anonymized_text)

# You can run this file to see a different, fake name, email, city, and phone number
# generated every time.