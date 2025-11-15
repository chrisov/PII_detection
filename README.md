<a name="top"></a>

<div align="center">
  <img src="https://raw.githubusercontent.com/chrisov/PII_detection/resources/Logo.png" width="400" alt="Logo"/>
</div>

<div align="center">

### 🛠 Python (NumPy, Pandas)
### 🛠 AWS Services
### 🛠 Docker

</div>

# Financial Services Document Compliance

## 1. Introduction

### 1.1 General

In an era of stringent data protection regulations and increasing cybersecurity threats, the handling of *Personally Identifiable Information* (PII) has become a critical concern for organizations across all sectors. Financial institutions, in particular, process vast quantities of sensitive documents containing PII, from bank statements and loan applications to tax returns and credit reports. Manual redaction of this information is time-consuming, error-prone, and scales poorly as document volumes increase.

This project presents a **cloud-deployed end-to-end machine learning** system for automated detection and redaction of PII in financial documents. By leveraging state-of-the-art *Natural Language Processing* (NLP) techniques, specifically **BERT**-based *Named Entity Recognition* (NER), the system identifies sensitive information with high accuracy, enabling organizations to protect customer privacy while streamlining document processing workflows.

### 1.2 Problem Statement

Financial services companies face mounting pressure from regulatory frameworks (*PCI-DSS*, *GDPR*, *CCPA*, *SOC2*). A single unredacted PII element in a shared document can result in regulatory violations costing anywhere from $100 to $50,000 per exposed record, plus reputational damage and potential lawsuits. Manual PII redaction presents significant operational challenges, such as  **time-pressure**, **error-proneness**, **non-scalability**, **inconsistency**. Financial institutions routinely need to share documents with *Credit bureaus* and underwriters for loan origination, *external auditors* for compliance reviews, *third-party analytics providers* for risk modeling and more. Each sharing instance requires comprehensive PII removal, creating a bottleneck in business processes. For example:

- <u>A digital lending platform</u> processes 1,000+ loan applications monthly, each containing 15-25 pages of financial documents (bank statements, pay stubs, tax returns).

	**ROI**: For a platform processing $50M in annual loan volume, saving 500 hours monthly at $40/hour = $240,000 annual savings, plus reduced compliance risk.

- <u>A fintech company</u> undergoes SOC 2 Type II audit requiring sample customer transaction records.

	**IMPACT**: Reduces audit preparation time from 3 weeks to 3 days, maintains data utility for auditors while ensuring privacy.

- <u>A bank</u>'s data science team wants to analyze customer transaction patterns to improve fraud detection models.
	
	**IMPACT**: Unlocks valuable data for analytics while maintaining GDPR/CCPA compliance, enabling data-driven decision making without privacy violations.

<div align="right">
  <a href="#top">⬆️ Return to top</a>
</div>

<br>

## 2. Technical approach

The system implements a two-stage machine learning pipeline with human-in-the-loop validation:

<u>**Stage 1**</u>: The first stage targets common entities such as *names*, *emails*, *addresses*, and *account numbers*. PDFs are ingested, text is extracted via OCR (*Optical Character Recognition*) or parsing, and the model identifies sensitive information to produce a redacted output. This establishes the core functionality of PII detection and redaction in a controlled environment.

To ensure iterative improvement, a continuous retraining pipeline is implemented. Synthetic data generation allows for expanding entity coverage and testing edge cases, while user feedback is incorporated into new training cycles (**Human-in-the-Loop**). Evaluation metrics such as precision, recall, and F1-score are tracked to measure the model’s accuracy and reliability on unseen financial documents, forming the foundation for more advanced stages.

<u>**Stage 2**</u>: It enhances the system by introducing adaptability to previously unseen PII patterns and more complex document formats. The model leverages techniques like *embedding-based anomaly detection* and *semi-supervised learning* to flag novel or unusual PII types, such as newly formatted account identifiers or transaction-specific codes. This allows the system to handle real-world variability in financial documents that the original training data might not cover.

The focus of this stage is robustness and generalization. By continuously incorporating new document formats and anomalous PII patterns into the retraining loop, the model improves over time and becomes more resilient to errors. Test cases are designed to challenge the system, ensuring it maintains high accuracy while expanding its entity coverage, preparing the project for deployment at scale.

<a id="pic1"></a>

```
Stage 1 (MVP): Supervised Named Entity Recognition
├── Document Ingestion (PDF, images, text)
├── Text Extraction (OCR for scanned docs)
├── BERT-based NER Model						<------ Currently here
├── Entity Classification (PERSON, SSN, ACCOUNT_NUMBER, etc.)
├── Human Review Queue
└── Redaction Engine

Stage 2: Active Learning Enhancement
├── Uncertainty Detection (model confidence scoring)
├── Human Validation Interface
├── Incremental Model Retraining
└── New Entity Type Adaptation
```

<div align=center>
	Picture 1: Technical approach per Stage.
</div>


### 2.1 Stage 1 (MVP): Continuous Retraining PII Model

Every step of Stage 1, as defined in [Picture 1](#pic1), are explained in the following:

- <u>**Document Ingestion**</u>: The Training Dataset is consisted of a plethora of different ***synthetic*** Bank Statements in PDF mode:
  
  - **Jinja2** Library to generate PDFs out of html templates.
  - **Faker** Library to populate the generated PDFs with synthetic PII.

- <u>**Text Extraction**</u>: An automatic identification of document type is used (text-based PDFs vs image-based PDFs vs plain text) and the appropriate extraction method is executed:

  - **pdfplumber** Library for layout-preserving text extraction in text-based PDFs.
  - **Tesseract OCR** for image-to-text conversion in image-based PDFs.

- <u>**BERT-based NER Model**</u>: The model in use is a distilled BERT-based NER model:
  - **BERT-based model** because it is already pretrained in massive text corpora and can already achieve >95% *F1 Score* in standard PII types.
  - **distilled** because it achieves faster inference than the Base BERT.

- <u>**Entity Classification**</u>: NER is framed as a token-level sequence classification task. Given input text tokenized into words/subwords, the model assigns each token a label in the *IBO* format, such  as ***PERSON***, ***SSN***, ***ACCOUNT_NUMBER***, ***ROUTING_NUMBER***, ***CREDIT_CARD***, and more. Example:
  
	```
	Input:  Account holder: John Smith SSN: 123-45-6789
	Labels: O       O       B-PERSON I-PERSON B-SSN I-SSN I-SSN
  	```

- <u>**Human Review Queue**</u>: 

- <u>**Redaction Engine**</u>: 

### Stage 2

### Deployment

## Dataset

## Pipeline