# Analisis Komparatif Algoritma Klasifikasi Sentimen untuk Mengukur Kesesuaian Star Rating dan Ulasan Pengguna

Proyek ini bertujuan untuk menganalisis tingkat kesesuaian antara rating bintang (*star rating*) yang diberikan oleh pengguna aplikasi di Google Play Store dengan sentimen yang tertuang dalam teks ulasan mereka. Proyek ini melakukan **Studi Komparatif** antara tiga algoritma klasifikasi populer untuk menemukan model yang paling akurat dalam mendeteksi *mismatch*.

## Fitur Utama
- **Comparative Study**: Membandingkan performa **Multinomial Naive Bayes**, **Linear SVM**, dan **Logistic Regression**.
- **Large Scale Dataset**: Menggunakan 12.495 ulasan ulasan aplikasi asli dari Google Play Store.
- **Advanced NLP Pipeline**: Mencakup *TF-IDF Vectorization* (Unigram & Bigram) dan **Lemmatization** (WordNet).
- **Tableau Integration**: Ekspor hasil analisis ke format `.csv` yang dioptimasi untuk visualisasi analitik di Tableau.
- **Handling Data Imbalance**: Implementasi **RandomOverSampler** (ROS) untuk menyeimbangkan kelas sentimen.
- **Visualisasi Mendalam**: EDA (Exploratory Data Analysis), N-Gram Analysis, dan Confusion Matrix komparatif.

## Dataset
Dataset yang digunakan berasal dari Kaggle: [Google Play Store Reviews](https://www.kaggle.com/datasets/prakharrathi25/google-play-store-reviews).
- **Total Data**: 12.495 ulasan.
- **Kolom Utama**: `content` (Teks ulasan) dan `score` (Rating 1-5).

## Persyaratan Sistem
- Python 3.10+
- Library Utama: `pandas`, `scikit-learn`, `nltk`, `kagglehub`, `matplotlib`, `seaborn`, `imblearn`.

## Cara Menjalankan
1. Instal dependensi:
   ```bash
   pip install pandas scikit-learn nltk kagglehub matplotlib seaborn imbalanced-learn
   ```
2. Jalankan Jupyter Notebook:
   ```bash
   jupyter notebook analisis_kesesuaian_rating_dan_sentimen_naive_bayes.ipynb
   ```

## Metodologi
1. **Data Preparation**: Labeling sentimen otomatis berdasarkan rating (1-2: Negatif, 3: Netral, 4-5: Positif).
2. **Text Preprocessing**: Cleaning, Case Folding, Stopwords Removal, dan Lemmatization.
3. **Feature Engineering**: Ekstraksi fitur menggunakan TF-IDF (1,2 n-grams).
4. **Balancing**: Menyamakan jumlah sampel tiap kelas menggunakan ROS.
5. **Model Training & Comparison**: Melatih tiga model dan membandingkan metrik akurasi serta F1-Score.
6. **Mismatch Analysis**: Identifikasi ketidaksesuaian antara prediksi sentimen dan rating asli.
