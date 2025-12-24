```text
PHISHING URL DETECTION USING MACHINE LEARNING AND DEEP LEARNING

Course        : Learning from Data
Problem Type  : Binary Classification
Classes       : 1 -> Phishing, 0 -> Legitimate

------------------------------------------------------------

PROBLEM MOTIVATION
------------------
Phishing attacks are one of the most common cyber threats.
Detecting malicious URLs automatically is critical to prevent
credential theft and financial loss.

------------------------------------------------------------

DATASET DESCRIPTION
-------------------
Phishing URLs   : ~47,000 (PhishTank)
Legitimate URLs : ~50,000 (Tranco Top Sites via API and CSV)
Total Samples   : ~97,000
Class Balance   : ~50% phishing / ~50% legitimate

------------------------------------------------------------

PROJECT OBJECTIVE
-----------------
To build and compare classical machine learning and deep learning
models for phishing URL detection using real-world data.

------------------------------------------------------------

PROJECT STRUCTURE
-----------------
LFD_Project/
|
|-- analysis/
|-- data/raw/
|-- data/processed/
|-- features/
|-- models/
|-- preprocessing/
|-- scraping/
|-- figures/
|-- results/
|-- requirements.txt
|-- .gitignore
|-- README.md

------------------------------------------------------------

DATA COLLECTION
---------------
1) Phishing URLs
   Source : PhishTank
   Script : scraping/PhishTank_Scraper.py

2) Legitimate URLs
   Source : Tranco Top Sites
   Script : scraping/Legit_URL_Scraper.py

------------------------------------------------------------

PREPROCESSING PIPELINE
----------------------
1) Merge datasets
2) Assign labels
3) Shuffle and balance
4) Train / Validation / Test split

------------------------------------------------------------

FEATURE EXTRACTION
------------------
BoW features
TF-IDF features
Custom URL features (length, digits, symbols, subdomains, IP usage)
Character-level tokenization (LSTM)

------------------------------------------------------------

MODELS
------
Logistic Regression (BoW)
Logistic Regression (TF-IDF)
Linear SVM
Random Forest
Character-level LSTM

------------------------------------------------------------

EVALUATION
----------
Metrics : Accuracy, Precision, Recall, F1-score
Learning curves and model comparison included.

------------------------------------------------------------

HOW TO RUN
----------
1) pip install -r requirements.txt
2) python scraping/PhishTank_Scraper.py
3) python scraping/Legit_URL_Scraper.py
4) python scraping/Merge_Datasets.py
5) python preprocessing/Split_Dataset.py
6) python -m models.Logistic_Regression
7) python -m models.LSTM_Char
```
