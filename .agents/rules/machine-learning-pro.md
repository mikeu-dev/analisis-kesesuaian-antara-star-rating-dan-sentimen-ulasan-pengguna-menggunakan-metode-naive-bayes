---
trigger: always_on
---

# Machine-Learning-Pro AI Agent Skill (Antigravity)

Machine-Learning-Pro AI Agent Skill adalah workflow terstruktur untuk membangun sistem machine learning yang sistematis, reproducible, dan dapat dipertanggungjawabkan secara teknis maupun akademik.

---

## 1. PRINCIPLE UTAMA

WAJIB:

- Data-driven > asumsi
- Reproducibility > eksperimen acak
- Evaluasi objektif > klaim subjektif
- Pipeline jelas > script berantakan

---

## 2. CONTEXT AWARENESS

AI HARUS:

- Mendeteksi:
  - Jenis problem:
    - classification
    - regression
    - clustering
    - NLP / CV

- Menentukan:
  - algoritma yang relevan
  - metrik evaluasi yang sesuai

---

## 3. PIPELINE WAJIB (END-TO-END)

WAJIB mengikuti alur:

1. Data Collection
2. Data Understanding
3. Data Preprocessing
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Validation
8. Deployment (opsional)

---

## 4. DATA HANDLING (KRITIS)

WAJIB:

- Dataset harus:
  - jelas sumbernya (misal Kaggle)
  - dapat diakses

- Pisahkan:
  - train
  - validation
  - test

DILARANG:

- Data leakage
- Menggunakan test data saat training

---

## 5. DATA PREPROCESSING

WAJIB:

- Cleaning:
  - missing value
  - duplicate

- Encoding:
  - categorical → numeric

- Normalisasi / scaling jika perlu

Untuk NLP:

- case folding
- tokenization
- stopword removal
- stemming / lemmatization

---

## 6. FEATURE ENGINEERING

WAJIB:

- Transformasi data relevan
- Gunakan:
  - TF-IDF (NLP)
  - normalization
  - feature selection

---

## 7. MODEL SELECTION

AI HARUS:

- Menyesuaikan model dengan problem:

Contoh:

- Naive Bayes → text classification
- Logistic Regression → baseline
- Random Forest → general purpose
- SVM → high-dimensional

---

## 8. TRAINING (WAJIB TERSTRUKTUR)

WAJIB:

- Gunakan:
  - pipeline (sklearn pipeline)

- Pisahkan:
  - training logic
  - evaluation logic

---

## 9. EVALUATION (KRITIS)

WAJIB:

- Gunakan metrik sesuai problem:

Classification:

- accuracy
- precision
- recall
- F1-score

WAJIB:

- Gunakan confusion matrix

---

## 10. VALIDATION

WAJIB:

- Gunakan:
  - cross-validation

- Hindari:
  - overfitting
  - underfitting

---

## 11. REPRODUCIBILITY

WAJIB:

- Set random seed
- Dokumentasikan:
  - parameter
  - dataset

- Gunakan:
  - notebook (.ipynb) atau script terstruktur

---

## 12. CODE STRUCTURE

Pisahkan:

```id="ml9k2p"
project/
 ├── data/
 ├── notebooks/
 ├── src/
 │    ├── preprocessing/
 │    ├── features/
 │    ├── models/
 │    ├── evaluation/
 │    └── utils/
 ├── outputs/
 └── config/
```

---

## 13. OUTPUT RULES UNTUK AI

AI HARUS:

- Menyediakan:
  - langkah pipeline
  - alasan pemilihan model

- Tidak asal memilih algoritma
- Menjelaskan hasil evaluasi

---

## 14. ANTI-PATTERN (DILARANG)

- Tidak ada train/test split
- Evaluasi hanya accuracy
- Tidak ada preprocessing
- Tidak ada validasi
- Overclaim hasil tanpa bukti

---

## 15. INTEGRASI DENGAN SKRIPSI

WAJIB:

- Semua langkah ML:
  → HARUS bisa ditulis ke BAB III & IV
- Output:
  - tabel hasil
  - grafik evaluasi

---

## 16. TOOLS REKOMENDASI

- Python
- pandas
- scikit-learn
- matplotlib
- seaborn (opsional)
- nltk / sastrawi (untuk NLP Indonesia)

---

## 17. PRINSIP UTAMA

- Pipeline > script random
- Evaluasi > asumsi
- Reproducible > sekali jalan
- Interpretasi > angka mentah

---

Gunakan skill ini untuk menghasilkan sistem machine learning yang valid secara akademik, terstruktur secara engineering, dan siap digunakan dalam skripsi maupun pengembangan lanjutan.
