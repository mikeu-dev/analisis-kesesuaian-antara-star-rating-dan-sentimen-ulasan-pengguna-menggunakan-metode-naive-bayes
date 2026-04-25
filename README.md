# Analisis Kesesuaian antara Star Rating dan Sentimen Ulasan Pengguna menggunakan Metode Naive Bayes

Proyek ini bertujuan untuk menganalisis apakah rating bintang (star rating) yang diberikan oleh pengguna aplikasi di Google Play Store sesuai dengan sentimen yang tertuang dalam teks ulasan mereka. Analisis ini menggunakan algoritma **Multinomial Naive Bayes** dan teknik **TF-IDF Vectorization** untuk klasifikasi teks.

## Fitur Utama
- **Automated Dataset Loading**: Mengunduh dataset terbaru dari Kaggle menggunakan `kagglehub`.
- **Text Preprocessing**: Membersihkan teks ulasan (lowercase, pembersihan karakter non-huruf, dan penghapusan stopwords).
- **Sentiment Mapping**: Mengonversi star rating (1-5) menjadi kategori sentimen (Positive, Neutral, Negative).
- **Machine Learning Pipeline**: Implementasi end-to-end dari ekstraksi fitur hingga evaluasi model.
- **Evaluation Metrics**: Menghitung akurasi, presisi, recall, dan F1-score.

## Dataset
Dataset yang digunakan berasal dari Kaggle: [Google Play App Reviews Dataset](https://www.kaggle.com/datasets/hassaanmustafavi/google-play-app-reviews-dataset).
Dataset ini berisi ribuan ulasan aplikasi dengan kolom utama:
- `review_description`: Teks ulasan asli.
- `rating`: Rating bintang (1 hingga 5).

## Persyaratan Sistem
- Python 3.10+
- Library: `pandas`, `numpy`, `scikit-learn`, `nltk`, `kagglehub`.

## Cara Menjalankan
1. Pastikan Anda telah menginstal dependensi:
   ```bash
   pip install pandas numpy scikit-learn nltk kagglehub
   ```
2. Jalankan Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
3. Buka file `analisis_kesesuaian_rating_dan_sentimen_naive_bayes.ipynb` dan jalankan semua sel.

## Metodologi
1. **Data Cleaning**: Menghapus baris dengan teks ulasan kosong.
2. **Preprocessing**: Tokenisasi dan pembersihan teks untuk meningkatkan kualitas fitur.
3. **Feature Engineering**: Menggunakan TF-IDF untuk merepresentasikan teks dalam bentuk numerik.
4. **Classification**: Menggunakan Naive Bayes yang dikenal efektif untuk klasifikasi teks berskala besar.
5. **Validation**: Membandingkan hasil prediksi model dengan label sentimen yang diturunkan dari rating bintang.

---
**Kontributor:** [Nama Anda/Mikeudev]
**Lisensi:** MIT
