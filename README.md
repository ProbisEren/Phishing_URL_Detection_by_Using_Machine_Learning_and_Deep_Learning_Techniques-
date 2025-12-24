Phishing URL Detection using Machine Learning
=============================================

Course        : Learning from Data
Task          : Binary Classification (Phishing vs Legitimate)
Approach      : Classical Machine Learning + Deep Learning
Labels        :
    1 -> Phishing
    0 -> Legitimate

Goal:
    Detect phishing URLs automatically by learning patterns
    from real-world phishing and legitimate website data.

------------------------------------------------------------

Dataset Description
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

Project Structure
-----------------

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

Data Collection
---------------

Step 1: Collect phishing URLs
    Source : PhishTank
    Script : scraping/PhishTank_Scraper.py
    Output :
        data/raw/phishing_urls.json
        data/raw/phishing_urls.csv

Step 2: Collect legitimate URLs
    Source : Tranco Top Sites
    Script : scraping/Legit_URL_Scraper.py
    Output :
        data/raw/legit_urls.json
        data/raw/legit_urls.csv

------------------------------------------------------------

Data Preprocessing
------------------

Steps:
    1. Merge phishing and legitimate datasets
    2. Assign labels (1 = phishing, 0 = legitimate)
    3. Shuffle and balance the dataset
    4. Split dataset into:
        - Training set
        - Validation set
        - Test set

Script used:
    preprocessing/Split_Dataset.py

------------------------------------------------------------

Feature Extraction
------------------

Classical ML features:
    - Bag of Words (BoW)
    - TF-IDF

Custom URL-based features:
    - URL length
    - Number of digits
    - Number of special characters
    - Number of subdomains
    - Presence of IP address
    - Suspicious keywords

Deep Learning features:
    - Character-level tokenization
    - Fixed-length padded character sequences

------------------------------------------------------------

Models Implemented
------------------

Classical Machine Learning:
    - Logistic Regression (BoW)
    - Logistic Regression (TF-IDF)
    - Linear Support Vector Machine
    - Random Forest

Deep Learning:
    - Character-level LSTM
        * Embedding layer
        * LSTM layer
        * Dropout for regularization
        * Sigmoid output layer

------------------------------------------------------------

Evaluation
----------

Metrics used:
    - Accuracy
    - Precision
    - Recall
    - F1-score

Additional analysis:
    - Learning curves for LSTM model
    - Model performance comparison

Results saved in:
    results/model_comparison.csv

------------------------------------------------------------

How to Run (Step-by-step)
=========================

0) Go to project folder
-----------------------
cd /Users/metinerenuzun/PycharmProjects/LFD_Project

1) Create & activate virtual environment
----------------------------------------
python3 -m venv .venv
source .venv/bin/activate

2) Install dependencies
-----------------------
pip install --upgrade pip
pip install -r requirements.txt

3) Data Collection (Scraping)
-----------------------------

3.1) Collect phishing URLs (PhishTank)
--------------------------------------
python scraping/PhishTank_Scraper.py

Expected outputs:
    data/raw/phishing_urls.json
    data/raw/phishing_urls.csv

3.2) Collect legitimate URLs (Tranco)
-------------------------------------
python scraping/Legit_URL_Scraper.py

Expected outputs:
    data/raw/legit_urls.json
    data/raw/legit_urls.csv

4) Merge datasets (50/50 balance)
--------------------------------
python scraping/Merge_Datasets.py

Expected output:
    data/processed/final_dataset.csv

5) Split into train / val / test
--------------------------------
python preprocessing/Split_Dataset.py

Expected outputs:
    data/processed/train.csv
    data/processed/val.csv
    data/processed/test.csv

6) Train & Evaluate Models
--------------------------

IMPORTANT:
    Always run models with "-m" (module mode)

6.1) Logistic Regression (BoW)
------------------------------
python -m models.Logistic_Regression

6.2) Logistic Regression (TF-IDF)
---------------------------------
python -m models.Logistic_Regression_TFIDF

6.3) Linear SVM (BoW)
---------------------
python -m models.Linear_SVM

6.4) Random Forest (Custom URL Features)
----------------------------------------
python -m models.Random_Forest

6.5) LSTM (Character-level)
---------------------------
python -m models.LSTM_Char

Expected extra output:
    data/processed/lstm_history.pkl

7) Analysis (Plots + Comparison)
--------------------------------

7.1) Create learning curve figures (LSTM)
-----------------------------------------
python analysis/plot_learning_curve.py

Expected outputs:
    figures/learning_curves/lstm_accuracy_curve.png
    figures/learning_curves/lstm_loss_curve.png

7.2) Show learning curves (open both images)
--------------------------------------------
python analysis/show_learning_curves.py

7.3) Create model comparison table
----------------------------------
mkdir -p results
python analysis/model_comparison.py

Expected output:
    results/model_comparison.csv

------------------------------------------------------------

Notes
-----

Large datasets and generated files are excluded from version control
using .gitignore.
