# Aplikasi Prediksi Penyakit

## Deskripsi Proyek

Aplikasi ini adalah sebuah sistem berbasis web yang bertujuan untuk membantu pengguna dalam melakukan prediksi dini terhadap beberapa jenis penyakit umum berdasarkan data masukan pengguna. Saat ini, aplikasi mendukung prediksi untuk penyakit Diabetes, Hipertensi, dan Stroke. Proyek ini dikembangkan sebagai bagian dari Capstone Project Dicoding.

## Fitur Utama

-   **Prediksi Diabetes**: Memprediksi kemungkinan seseorang menderita diabetes berdasarkan parameter kesehatan seperti kadar glukosa, tekanan darah, indeks massa tubuh, dll.
-   **Prediksi Hipertensi**: Memprediksi kemungkinan seseorang menderita hipertensi berdasarkan parameter seperti usia, jenis kelamin, tekanan darah sistolik dan diastolik, dll.
-   **Prediksi Stroke**: Memprediksi kemungkinan seseorang terkena stroke berdasarkan faktor risiko seperti usia, riwayat penyakit jantung, status pernikahan, jenis pekerjaan, dll.
-   **Antarmuka Pengguna Intuitif**: Desain antarmuka yang sederhana dan mudah digunakan.
-   **Tombol Clear Form**: Memudahkan pengguna untuk mengatur ulang input pada formulir.
-   **Tooltips/Teks Bantuan**: Memberikan penjelasan untuk setiap kolom input, terutama untuk istilah medis.

## Teknologi yang Digunakan

-   **Backend**: Python (Flask)
-   **Frontend**: HTML, CSS, JavaScript
-   **Machine Learning**: Scikit-learn, TensorFlow/Keras (untuk model yang disimpan)
-   **Deployment (Lokal)**: Flask development server

## Struktur Proyek

```
├── app.py                  # File utama aplikasi Flask
├── diabetes.csv            # Dataset diabetes 
├── diabetes.ipynb          # Notebook Jupyter untuk eksplorasi/pemodelan diabetes
├── diabetes_data.csv       # Dataset diabetes yang sudah diproses 
├── hypertension.ipynb      # Notebook Jupyter untuk eksplorasi/pemodelan hipertensi
├── hypertension_data.csv   # Dataset hipertensi yang sudah diproses 
├── stroke.ipynb            # Notebook Jupyter untuk eksplorasi/pemodelan stroke
├── stroke_data.csv         # Dataset stroke yang sudah diproses 
├── saved_models/           # Direktori untuk menyimpan model machine learning 
│   ├── diabetes_model/     # Model untuk prediksi diabetes
│   ├── diabetes_scaler.pkl # Scaler untuk data diabetes
│   ├── hypertension_model/ # Model untuk prediksi hipertensi
│   ├── hypertension_preprocessor.pkl # Preprocessor untuk data hipertensi
│   ├── stroke_model/       # Model untuk prediksi stroke
│   └── stroke_preprocessor.pkl # Preprocessor untuk data stroke
├── static/                 # File statis (CSS, JavaScript, Gambar)
│   ├── css/style.css
│   ├── images/
│   │   ├── diabetes.svg
│   │   ├── hypertension.svg
│   │   └── stroke.svg
│   └── js/script.js
├── templates/              # File HTML template untuk Flask
│   ├── diabetes.html
│   ├── hypertension.html
│   ├── index.html
│   ├── menu.html
│   └── stroke.html
└── README.md               # File ini
```

## Cara Instalasi

1.  **Clone Repository (Jika ada di Git)**:
    ```bash
    git clone <URL_REPOSITORY_INI>
    cd <NAMA_DIREKTORI_PROYEK>
    ```

2.  **Buat dan Aktifkan Virtual Environment (Direkomendasikan)**:
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    Jika `requirements.txt` sudah ada:
    ```bash
    pip install -r requirements.txt
    ```
    Jika belum, install manual pustaka utama:
    ```bash
    pip install Flask scikit-learn pandas numpy tensorflow
    ```

## Cara Penggunaan Aplikasi

1.  **Jalankan Aplikasi Flask**:
    Pastikan Anda berada di direktori root proyek.
    ```bash
    python app.py
    ```

2.  **Buka di Browser**:
    Aplikasi biasanya akan berjalan di `http://127.0.0.1:5000/` atau `http://localhost:5000/`. Buka alamat ini di browser Anda.

3.  **Navigasi ke Halaman Prediksi**:
    -   Dari halaman utama (`index.html`), pilih menu prediksi yang diinginkan (Diabetes, Hipertensi, atau Stroke).
    -   Atau, Anda bisa langsung mengakses halaman prediksi melalui URL, misalnya:
        -   `http://localhost:5000/diabetes`
        -   `http://localhost:5000/hypertension`
        -   `http://localhost:5000/stroke`

4.  **Isi Formulir**:
    -   Masukkan data yang diminta pada formulir prediksi.
    -   Gunakan tooltip (arahkan kursor ke kolom input) jika memerlukan penjelasan lebih lanjut mengenai data yang harus diisi.

5.  **Kirim Data untuk Prediksi**:
    -   Klik tombol "Prediksi".
    -   Indikator loading akan muncul selagi sistem memproses data Anda.

6.  **Lihat Hasil Prediksi**:
    -   Hasil prediksi akan ditampilkan di bawah formulir.

7.  **Clear Form (Opsional)**:
    -   Jika ingin memasukkan data baru, klik tombol "Clear Form" untuk mengosongkan semua input.

## Kontribusi

Saat ini, kontribusi untuk proyek ini belum dibuka secara formal. Namun, jika Anda memiliki saran atau menemukan bug, silakan buat *issue* (jika proyek ini ada di platform Git seperti GitHub/GitLab).

## Lisensi

Proyek ini tidak memiliki lisensi spesifik saat ini. Harap gunakan dengan bijak dan sesuai dengan tujuan edukasi.