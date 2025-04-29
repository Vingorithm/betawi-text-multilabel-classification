# Betawi Multilabel Text Classification

## 📋 Overview
This project focuses on multilabel sentiment classification for sentences in the **Betawi dialect**, a local language variant spoken in Jakarta, Indonesia. The dataset includes sentiments across six vehicle-related categories:
- **fuel**
- **machine**
- **others**
- **part**
- **price**
- **service**

Each category has one of three possible sentiment labels: `positive`, `negative`, or `neutral`.

This project performs:
- Data preprocessing and cleaning
- Exploratory data analysis (EDA)
- Implementation and evaluation of machine learning models (Naive Bayes, SVM, KNN)

---

## 🎯 Objectives
- Clean and preprocess Betawi text data for consistent input
- Analyze sentiment distributions and patterns through EDA
- Develop multilabel classification models using Binary Relevance and Classifier Chain
- Evaluate model performance and visualize results
- Support automated sentiment analysis for Betawi vehicle-related texts

---

## 🧾 Dataset
The dataset is divided into:
- `train_preprocess.csv`: 810 rows
- `valid_preprocess.csv`: 90 rows
- `test_preprocess.csv`: 180 rows

Each file contains:
- `sentence`: Input text (e.g., *"Kenapa sih Avanza jadi boros bensin gini?"*)
- Sentiment labels for: `fuel`, `machine`, `others`, `part`, `price`, `service`

✅ **No missing values** were detected.

⚠️ **Note**: The dataset is relatively small, which may limit generalization performance.

---

## 📁 Project Structure
The core implementation is in the Jupyter notebook:
- `betawi-text-multilabel-classification.ipynb`

### Notebook Sections:
1. **Library Imports**: `pandas`, `sklearn`, `skmultilearn`, `matplotlib`, `seaborn`, `altair`, `plotly`, `missingno`
2. **Data Loading & Summary**
3. **Data Cleansing**
4. **EDA & Visualization**
5. **Modeling**: Binary Relevance & Classifier Chain with Naive Bayes, SVM, and KNN
6. **Evaluation**: Confusion matrices, classification reports
7. **Output**: Predictions saved in `hasil_prediksi_semua_model.csv`

---

## 📊 Model Evaluation

### Metrics Used:
- **Accuracy**
- **Precision / Recall / F1-Score**
- **Confusion Matrices**

### Results Summary:
| Model        | Strengths                                                   | Limitations                                                 |
|--------------|-------------------------------------------------------------|-------------------------------------------------------------|
| **Naive Bayes** | Simple, effective with TF-IDF                             | May underperform on overlapping sentiment categories        |
| **SVM**         | Best accuracy, handles sparse text well                  | Computationally expensive; struggles with ambiguity         |
| **KNN**         | Conceptually simple                                       | Sensitive to small dataset and high-dimensional features    |

---

## 📎 Additional Features
- 📊 Label Distribution Visualizations
- 🧾 Bag of Words & N-gram Feature Representations
- ✅ Clean and ready-to-use dataset splits
- 📈 Comparative model performance insights

---

## 📌 Installation & Usage
Clone the repo and run the Jupyter notebook:

```bash
git clone https://github.com/yourusername/betawi-multilabel-text-classification.git
cd betawi-multilabel-text-classification
jupyter notebook betawi-text-multilabel-classification.ipynb
