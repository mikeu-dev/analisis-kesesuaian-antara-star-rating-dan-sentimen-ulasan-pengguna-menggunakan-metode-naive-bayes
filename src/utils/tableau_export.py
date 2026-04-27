import pandas as pd
import numpy as np

def prepare_for_tableau(df, y_true, y_pred, probs=None, output_path="tableau_sentiment_analysis.csv"):
    """
    Menyiapkan dataframe untuk visualisasi di Tableau dengan menambahkan metadata penting.
    """
    print(f"Menyiapkan data untuk Tableau...")
    
    # Ambil index data test
    test_df = df.iloc[y_true.index].copy()
    
    # Tambahkan hasil prediksi
    test_df['predicted_sentiment'] = y_pred
    test_df['is_mismatch'] = test_df['sentiment'] != test_df['predicted_sentiment']
    
    # Kategori Mismatch (misal: Negative diprediksi Positive)
    def categorize_mismatch(row):
        if not row['is_mismatch']:
            return "Correct"
        return f"{row['sentiment']} as {row['predicted_sentiment']}"
    
    test_df['mismatch_type'] = test_df.apply(categorize_mismatch, axis=1)
    
    # Tambahkan Confidence Score
    if probs is not None:
        test_df['confidence_score'] = np.max(probs, axis=1)
    else:
        test_df['confidence_score'] = 1.0
        
    # Tambahkan fitur teks tambahan untuk analisis di Tableau
    test_df['review_char_length'] = test_df['review'].apply(len)
    test_df['review_word_count'] = test_df['review'].apply(lambda x: len(str(x).split()))
    
    # Export
    test_df.to_csv(output_path, index=False)
    print(f"Berhasil mengekspor {len(test_df)} baris ke {output_path}")
    return test_df

if __name__ == "__main__":
    print("Script ini dirancang untuk diimport ke dalam Notebook atau dijalankan sebagai modul.")
