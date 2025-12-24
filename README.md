# ============================================================
# Phishing URL Detection by Using Machine Learning
# ============================================================

# ------------------------------------------------------------
# PROJECT OVERVIEW
# ------------------------------------------------------------
# - Task        : Binary Classification (Phishing vs Legitimate)
# - Domain      : Cyber Security / Web Security
# - Course      : Learning From Data
# - Approach    : Classical ML + Deep Learning
# - Labels      :
#     1 -> Phishing
#     0 -> Legitimate
# - Goal        :
#     Detect phishing URLs automatically using learned patterns
#     from real-world phishing and legitimate website data.
# ------------------------------------------------------------


# ------------------------------------------------------------
# DATASET SUMMARY
# ------------------------------------------------------------
# - Phishing URLs :
#     Source : PhishTank (API + scraping)
#     Count  : 47303
#
# - Legitimate URLs :
#     Source : Tranco Top Websites (API + local CSV)
#     Count  : 50000
#
# - Total Samples :
#     97303 URLs
#
# - Class Balance :
#     Balanced during merging step
# ------------------------------------------------------------


# ------------------------------------------------------------
# PROJECT DIRECTORY STRUCTURE
# ------------------------------------------------------------
LFD_Project
├── analysis
│   ├── model_comparison.py          # compares all model performances
│   ├── plot_learning_curve.py       # generates learning curve figures
│   └── show_learning_curves.py      # displays saved learning curves
│
├── data
│   ├── raw
│   │   ├── phishing_urls.json       # raw phishing URLs from PhishTank
│   │   ├── phishing_urls.csv
│   │   ├── legit_urls.json          # raw legit URLs from Tranco
│   │   ├── legit_urls.csv
│   │   └── tranco_top_sites.csv
│   │
│   └── processed
│       ├── final_dataset.csv        # merged & labeled dataset
│       ├── train.csv
│       ├── val.csv
│       ├── test.csv
│       └── lstm_history.pkl         # training history of LSTM
│
├── features
│   ├── BoW_Features.py              # Bag-of-Words feature extraction
│   ├── tfidf_Features.py            # TF-IDF feature extraction
│   ├── Custom_Features.py           # handcrafted URL features
│   └── __init__.py                  # makes features a Python package
│
├── models
│   ├── Logistic_Regression.py       # BoW + Logistic Regression
│   ├── Logistic_Regression_TFIDF.py # TF-IDF + Logistic Regression
│   ├── Linear_SVM.py                # BoW + Linear SVM
│   ├── Random_Forest.py             # Custom URL features + RF
│   └── LSTM_Char.py                 # Character-level LSTM
│
├── preprocessing
│   └── Split_Dataset.py             # train / val / test split
│
├── scraping
│   ├── PhishTank_Scraper.py         # phishing URL collection
│   ├── Legit_URL_Scraper.py         # legitimate URL collection
│   ├── Merge_Datasets.py            # dataset merging & balancing
│   └── fix_phishing_csv.py          # cleaning phishing URLs
│
├── figures
│   └── learning_curves
│       ├── lstm_accuracy_curve.png
│       └── lstm_loss_curve.png
│
├── results
│   └── model_comparison.csv         # final model results table
│
├── requirements.txt
└── README.md
# ------------------------------------------------------------


# ------------------------------------------------------------
# DATA COLLECTION
# ------------------------------------------------------------

# Step 1: Phishing URL Collection
# - Script  : scraping/PhishTank_Scraper.py
# - Method  :
#     - API request to PhishTank
#     - JSON parsing
# - Output  :
#     - data/raw/phishing_urls.json
#     - data/raw/phishing_urls.csv

# Step 2: Legitimate URL Collection
# - Script  : scraping/Legit_URL_Scraper.py
# - Method  :
#     - Tranco API request (if available)
#     - Local CSV fallback (tranco_top_sites.csv)
# - Output  :
#     - data/raw/legit_urls.json
#     - data/raw/legit_urls.csv


# ------------------------------------------------------------
# DATA PREPROCESSING PIPELINE
# ------------------------------------------------------------

# Step 1: Phishing URL Cleaning
# - Script  : scraping/fix_phishing_csv.py
# - Actions :
#     - remove empty URLs
#     - remove invalid entries
#     - normalize formatting

# Step 2: Dataset Merging
# - Script  : scraping/Merge_Datasets.py
# - Actions :
#     - merge phishing & legitimate URLs
#     - assign labels
#     - balance dataset
# - Output  :
#     - data/processed/final_dataset.csv

# Step 3: Train / Validation / Test Split
# - Script  : preprocessing/Split_Dataset.py
# - Ratios  :
#     - Train : 70%
#     - Val   : 15%
#     - Test  : 15%
# - Output  :
#     - train.csv
#     - val.csv
#     - test.csv


# ------------------------------------------------------------
# FEATURE EXTRACTION
# ------------------------------------------------------------

# Bag-of-Words (BoW)
# - File   : features/BoW_Features.py
# - Used by:
#     - Logistic_Regression.py
#     - Linear_SVM.py

# TF-IDF
# - File   : features/tfidf_Features.py
# - Used by:
#     - Logistic_Regression_TFIDF.py

# Custom URL Features
# - File   : features/Custom_Features.py
# - Features include:
#     - URL length
#     - number of dots
#     - number of digits
#     - number of special characters
#     - presence of IP address
#     - HTTPS usage
#     - suspicious keywords
# - Used by:
#     - Random_Forest.py


# ------------------------------------------------------------
# MODELS
# ------------------------------------------------------------

# Logistic Regression (BoW)
# - File : models/Logistic_Regression.py

# Logistic Regression (TF-IDF)
# - File : models/Logistic_Regression_TFIDF.py

# Linear Support Vector Machine
# - File : models/Linear_SVM.py

# Random Forest Classifier
# - File : models/Random_Forest.py

# Character-Level LSTM
# - File : models/LSTM_Char.py
# - Tokenization : character-based
# - Architecture :
#     - Embedding
#     - LSTM
#     - Dropout
#     - Dense (sigmoid)


# ------------------------------------------------------------
# MODEL EVALUATION
# ------------------------------------------------------------

# Metrics :
# - Accuracy
# - Precision
# - Recall
# - F1-score

# Learning Curves :
# - Accuracy curve
# - Loss curve
# - Saved in figures/learning_curves/

# Model Comparison :
# - Script : analysis/model_comparison.py
# - Output : results/model_comparison.csv


# ------------------------------------------------------------
# HOW TO RUN
# ------------------------------------------------------------

# 1) Install dependencies
#    pip install -r requirements.txt
#
# 2) Run scraping scripts
#    python scraping/PhishTank_Scraper.py
#    python scraping/Legit_URL_Scraper.py
#
# 3) Preprocess data
#    python scraping/fix_phishing_csv.py
#    python scraping/Merge_Datasets.py
#    python preprocessing/Split_Dataset.py
#
# 4) Train models
#    python -m models.Logistic_Regression
#    python -m models.Logistic_Regression_TFIDF
#    python -m models.Linear_SVM
#    python -m models.Random_Forest
#    python -m models.LSTM_Char
#
# 5) Analyze results
#    python analysis/model_comparison.py
#    python analysis/plot_learning_curve.py
# ------------------------------------------------------------