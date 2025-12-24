```text
PHISHING URL DETECTION BY USING MACHINE LEARNING AND DEEP LEARNING TECHNIQUES

Course       : Learning from Data
Approach     : Classical Machine Learning + Deep Learning
Labels       :
    1 -> Phishing
    0 -> Legitimate

Goal:
    Detect phishing URLs automatically using learned patterns
    from real-world phishing and legitimate website data.

------------------------------------------------------------

DATASET DESCRIPTION
-------------------
Data sources:
    - Phishing URLs   : PhishTank platform
    - Legitimate URLs : Tranco Top Sites list (via API and CSV)

Dataset statistics:
    - Phishing URLs   : ~47,000
    - Legitimate URLs : ~50,000
    - Total samples   : ~97,000
    - Class balance   : ~50% phishing, ~50% legitimate

------------------------------------------------------------

PROJECT STRUCTURE
----------------
LFD_Project/
|
|-- analysis/
|   |-- model_comparison.py
|   |-- plot_learning_curve.py
|   |-- show_learning_curves.py
|
|-- data/
|   |-- raw/
|   |   |-- phishing_urls.json
|   |   |-- phishing_urls.csv
|   |   |-- legit_urls.json
|   |   |-- legit_urls.csv
|   |   |-- tranco_top_sites.csv
|   |
|   |-- processed/
|       |-- final_dataset.csv
|       |-- train.csv
|       |-- val.csv
|       |-- test.csv
|       |-- lstm_history.pkl
|
|-- features/
|   |-- BoW_Features.py
|   |-- tfidf_Features.py
|   |-- Custom_Features.py
|   |-- __init__.py
|
|-- models/
|   |-- Logistic_Regression.py
|   |-- Logistic_Regression_TFIDF.py
|   |-- Linear_SVM.py
|   |-- Random_Forest.py
|   |-- LSTM_Char.py
|
|-- preprocessing/
|   |-- Split_Dataset.py
|
|-- scraping/
|   |-- PhishTank_Scraper.py
|   |-- Legit_URL_Scraper.py
|   |-- Merge_Datasets.py
|   |-- fix_phishing_csv.py
|
|-- figures/
|   |-- learning_curves/
|       |-- lstm_accuracy_curve.png
|       |-- lstm_loss_curve.png
|
|-- results/
|   |-- model_comparison.csv
|
|-- requirements.txt
|-- .gitignore
|-- README.md

------------------------------------------------------------

DATA COLLECTION
---------------
Step 1:
    Collect phishing URLs
    Source : PhishTank
    Script : scraping/PhishTank_Scraper.py
    Output :
        data/raw/phishing_urls.json
        data/raw/phishing_urls.csv

Step 2:
    Collect legitimate URLs
    Source : Tranco Top Sites
    Script : scraping/Legit_URL_Scraper.py
    Output :
        data/raw/legit_urls.json
        data/raw/legit_urls.csv

------------------------------------------------------------

DATA PREPROCESSING
-----------------
Steps:
    1) Merge phishing and legitimate datasets
    2) Assign labels (1 = phishing, 0 = legitimate)
    3) Shuffle and balance the dataset
    4) Split into train / validation / test sets

Script:
    preprocessing/Split_Dataset.py

------------------------------------------------------------

FEATURE EXTRACTION
-----------------
Text-based features:
    - Bag of Words (BoW)
    - TF-IDF

Custom URL features:
    - URL length
    - Number of digits
    - Number of special characters
    - Number of subdomains
    - Presence of IP address
    - Suspicious keywords

Deep learning features:
    - Character-level tokenization
    - Fixed-length padded sequences

------------------------------------------------------------

MODELS
------
Classical ML:
    - Logistic Regression (BoW)
    - Logistic Regression (TF-IDF)
    - Linear SVM
    - Random Forest

Deep Learning:
    - Character-level LSTM with dropout

------------------------------------------------------------

EVALUATION
----------
Metrics:
    - Accuracy
    - Precision
    - Recall
    - F1-score

Additional analysis:
    - Learning curves (loss & accuracy)
    - Model comparison table

------------------------------------------------------------

HOW TO RUN
----------
1) Install dependencies:
    pip install -r requirements.txt

2) Collect data:
    python scraping/PhishTank_Scraper.py
    python scraping/Legit_URL_Scraper.py

3) Merge datasets:
    python scraping/Merge_Datasets.py

4) Split dataset:
    python preprocessing/Split_Dataset.py

5) Train models:
    python -m models.Logistic_Regression
    python -m models.Logistic_Regression_TFIDF
    python -m models.Linear_SVM
    python -m models.Random_Forest
    python -m models.LSTM_Char
```
