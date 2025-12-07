# 🚗 Chatbot Showroom Mobil Sungkang

Chatbot AI customer service untuk Showroom Mobil Sungkang menggunakan **Google Gemini API** dan **Streamlit**. Fitur chat interaktif, informasi mobil lengkap, promo, dan informasi layanan lainnya.

## Fitur Utama

- **Chatbot Interaktif AI**: Percakapan natural dengan Google Gemini API yang memahami konteks showroom
- 🚗 **Katalog Lengkap**: 20 mobil dengan harga, spesifikasi, kategori, dan warna pilihan
- 🎁 **Promo Aktif**: 5 penawaran spesial (diskon, asuransi gratis, DP 0%, trade-in, cicilan 0%)
- 💳 **Paket Pembiayaan**: 5 pilihan tenor cicilan (12, 24, 36, 48, 60 bulan)
- 🏥 **Layanan**: 8 jenis layanan purna jual (test drive, konsultasi gratis, asuransi, dsb)
- 🏢 **Fasilitas**: 9 fasilitas modern (showroom, ruang tunggu, WiFi, kafe kecil, dsb)
- ⏲️ **Jam Operasional**: Senin-Jumat 08:00-18:00, Sabtu 08:00-14:00, Minggu Libur
- 📱 **WhatsApp Integration**: Kontak langsung ke 4 departemen (Penjualan, Finance, After Sales)
- 🎯 **Quick Actions**: 4 tombol pintas (Daftar Mobil, Promo, Jam Buka, Kontak)
- 📸 **Social Media**: Instagram & Email terintegrasi
- 🎨 **Modern UI**: Desain responsif dengan styling gradient dan animasi

## 🛠️ Tech Stack

| Komponen     | Versi                     | Deskripsi                         |
| ------------ | ------------------------- | --------------------------------- |
| **Frontend** | Streamlit 1.28.0          | Web framework untuk UI interaktif |
| **AI Model** | Gemini API Key            | Model dari Google                 |
| **Language** | Python 3.10+              | Backend logic & API integration   |
| **API**      | google-generativeai 0.3.0 | Google Generative AI SDK          |
| **Tools**    | python-dotenv, requests   | Environment & HTTP utilities      |

## 📋 Persyaratan Sistem

- **Python**: 3.10 atau lebih tinggi
- **Gemini API Key**: Gratis di https://makersuite.google.com/app/apikey
- **Koneksi Internet**: Untuk komunikasi dengan Gemini API
- **RAM**: Minimal 512MB (recommended 1GB+)
- **Storage**: ~50MB untuk project files

## 🚀 Instalasi & Setup Lokal

### 1️⃣ Clone Repository

```bash
git clone https://github.com/adamfitriyono/chatbot-showroom-sungkang
cd chatbot-sungkang
```

### 2️⃣ Setup Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Packages yang diinstall:

- `streamlit==1.28.0` - Web framework
- `google-generativeai==0.3.0` - Gemini API
- `python-dotenv==1.0.0` - Environment variables
- `requests==2.31.0` - HTTP requests

### 4️⃣ Setup Environment Variables

**Buat file `.env` di root directory:**

```env
GEMINI_API_KEY=your-api-key-here
```

**Dapatkan API Key:**

1. Kunjungi https://makersuite.google.com/app/apikey
2. Klik "Create API Key"
3. Copy key dan paste di `.env`

### 5️⃣ Jalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan membuka di `http://localhost:8501`

## 📁 Struktur Project

```
chatbot-sungkang/
│
├── app.py                    # Main aplikasi Streamlit
├── data.py                   # Data repository (mobil, promo, kontak, dll)
├── helper.py                 # Helper functions & Gemini integration
├── requirements.txt          # Python dependencies
│
├── .env                     # Environment variables
├── .gitignore               # Git ignore rules
├── .streamlit/
│   ├── config.toml          # Streamlit configuration
│   └── secrets.toml         # Streamlit Cloud secrets
│
└── README.md                # Dokumentasi project
```

### **app.py**

```
Purpose: Main entry point aplikasi
Content:
  - Imports & Gemini API setup
  - Page config (title, icon, layout)
  - CSS styling (gradient header, chat bubbles)
  - Session state management
  - Chat display loop & message handling
  - Quick action buttons (4 tombol)
  - Footer dengan info showroom
Comments: Semua dalam Bahasa Indonesia
```

### **data.py**

```
Purpose: Centralized data repository
Content:
  - Showroom metadata (nama, alamat, kontak, social media)
  - 20 daftar mobil (harga Rp139M-530M)
  - 5 promo aktif (diskon, asuransi, DP 0%, trade-in, cicilan)
  - 5 paket pembiayaan (12-60 bulan)
  - 8 jenis layanan purna jual
  - 9 fasilitas showroom
  - 4 kontak departemen
  - Jam operasional
Format: Dictionary dengan fungsi get_showroom_data()
```

### **helper.py**

```
Purpose: Utility functions & Gemini integration
Functions:
  - format_currency() - Format Rupiah
  - search_mobil() - Search mobil by keyword
  - format_mobil_info() - Display single car
  - format_daftar_mobil() - Display all 20 cars
  - format_promosi() - Display promotions
  - format_jam_operasional() - Display operating hours
  - format_kontak() - Display contact info
  - create_system_prompt() - Build Gemini context
  - get_response_from_gemini() - Call Gemini API
Model: Gemini (fallback)
Error Handling: Auth, quota, model availability, safety filters
Comments: Bahasa Indonesia
```

## 🔧 Konfigurasi & Customization

### Mengubah Data Showroom

Edit `data.py` - Function `get_showroom_data()`:

```python
# Ubah info showroom
"showroom": {
    "nama": "Showroom Mobil Sungkang",
    "alamat": "...",  # Ubah alamat
    "whatsapp": "...",  # Ubah nomor
    "instagram": "...",  # Ubah handle
}

# Tambah/hapus mobil di dalam "mobil" dictionary
# Edit promo, financing, services, facilities sesuai kebutuhan
```

### Customize AI Prompt

Edit `helper.py` - Function `create_system_prompt()`:

```python
def create_system_prompt(showroom_data):
    # Ubah instruksi untuk Gemini
    system_prompt = """
    Anda adalah customer service AI untuk [SHOWROOM].
    ... ubah instruksi sesuai kebutuhan ...
    """
    return system_prompt
```

### Ubah Theme/Styling

Edit `app.py` - CSS section:

```python
css = """
    :root {
        --primary-color: #667eea;  # Ubah warna primary
        --secondary-color: #764ba2;  # Ubah warna secondary
    }
    ...
"""
```

## 🐛 Troubleshooting & Error Handling

### Error 1: "API Key Invalid"

```
❌ Error: Invalid API key provided
Solusi:
  - Regenerate API key di https://makersuite.google.com/app/apikey
  - Copy key yang benar ke .env atau .streamlit/secrets.toml
  - Pastikan tidak ada spasi ekstra di key
  - Restart aplikasi (tekan R di browser)
```

### Error 2: "Module not found"

```
❌ Error: No module named 'streamlit' / 'google'
Solusi:
  - Pastikan virtual environment activated
  - Run: pip install -r requirements.txt
  - Cek requirements.txt tidak kosong
  - Update pip: python -m pip install --upgrade pip
```

### Error 3: "Quota Exceeded"

```
❌ Error: Resource has been exhausted
Solusi:
  - Gemini API gratis punya rate limit
  - Tunggu beberapa saat sebelum request baru
  - Upgrade ke paid plan jika diperlukan
  - Check usage di https://console.cloud.google.com
```

### Error 4: "Safety Filter Triggered"

```
❌ Error: Request blocked by safety filters
Solusi:
  - Coba ubah sistem prompt di helper.py
  - Hindari topik yang sensitive
  - Rephrase pertanyaan user-facing guidance
```

### Error 5: "Connection Timeout"

```
❌ Error: Request timed out
Solusi:
  - Check koneksi internet
  - Cek status Google API status page
  - Coba jalankan ulang request
  - Increase timeout di helper.py if needed
```

### Error 6: "Port 8501 already in use"

```
❌ Error: Address already in use
Solusi:
  - Kill process: netstat -ano | findstr :8501 (Windows)
  - Run di port berbeda: streamlit run app.py --server.port 8502
  - Restart IDE/terminal
```

## 📊 Info Showroom Sungkang

| Info            | Detail                                                       |
| --------------- | ------------------------------------------------------------ |
| **Nama**        | Showroom Mobil Sungkang                                      |
| **Alamat**      | Jl. Gatot Subroto No. 45, Semarang, Jawa Tengah              |
| **WhatsApp**    | +62 812-3456-7890 (Sales), +62 813-5678-9012 (Finance)       |
| **Instagram**   | @sungkangmobil                                               |
| **Email**       | info@sungkangmobil.com                                       |
| **Website**     | www.sungkangmobil.com                                        |
| **Jam Kerja**   | Senin-Jumat 08:00-18:00, Sabtu 08:00-14:00, Minggu LIBUR     |
| **Mobil**       | 20 pilihan (Toyota, Honda, Daihatsu, Isuzu, Mitsubishi, dsb) |
| **Harga Range** | Rp 139 Juta - Rp 530 Juta                                    |

⚠️ **Yang Harus Diperhatikan:**

- Jangan share API Key kepada siapapun
- Jangan commit `.env` atau `secrets.toml`
- Regenerate API Key jika terekspos
- Monitor usage di Google Cloud Console
- Use API quotas/rate limiting

## 📚 Link Penting & Resources

| Link                                          | Deskripsi               |
| --------------------------------------------- | ----------------------- |
| [Streamlit Docs](https://docs.streamlit.io)   | Dokumentasi framework   |
| [Gemini API](https://ai.google.dev)           | Google AI & Gemini info |
| [Streamlit Cloud](https://share.streamlit.io) | Deployment platform     |
| [Python Docs](https://docs.python.org/3/)     | Python documentation    |
| [GitHub](https://github.com)                  | Code repository         |

## 📦 Version Info

```
Project: Chatbot Showroom Mobil Sungkang
Version: 1.0.0
Python: 3.10+
Streamlit: 1.28.0
Gemini Multi-model
```

## 👨‍💻 Author

Created for Tugas Mata Kuliah Kecerdasan Buatan (AI) - Minggu 8-14
