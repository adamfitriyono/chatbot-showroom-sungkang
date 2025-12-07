"""
helper.py - Fungsi-fungsi helper untuk chatbot dengan Multi-Model Fallback
"""

import google.generativeai as genai
from typing import List, Dict, Any, Tuple

# Daftar model Gemini (fallback)
GEMINI_MODELS = [
    'gemini-2.0-flash',
    'gemini-2.0-flash-lite',
    'gemini-2.5-flash',
    'gemini-2.5-flash-lite',
    'gemini-2.5-pro',
    'gemini-3-pro',
    'gemini-1.5-pro',
    'gemini-1.5-flash',
]

def format_currency(amount: int) -> str:
    """
    Format angka menjadi currency Rupiah
    
    Args:
        amount: Jumlah dalam rupiah
        
    Returns:
        String dengan format Rp X.XXX.XXX
    """
    return f"Rp {amount:,.0f}".replace(",", ".")


def search_mobil(keyword: str, daftar_mobil: List[Dict]) -> List[Dict]:
    """
    Mencari mobil berdasarkan keyword (merek atau model)
    
    Args:
        keyword: Kata kunci pencarian
        daftar_mobil: List dari semua mobil
        
    Returns:
        List mobil yang cocok dengan keyword
    """
    keyword = keyword.lower()
    hasil = []
    
    for mobil in daftar_mobil:
        if (keyword in mobil['merek'].lower() or 
            keyword in mobil['model'].lower() or
            keyword in mobil['kategori'].lower()):
            hasil.append(mobil)
    
    return hasil


def format_mobil_info(mobil: Dict) -> str:
    """
    Format informasi mobil menjadi string yang readable
    
    Args:
        mobil: Dictionary berisi data mobil
        
    Returns:
        String berisi informasi mobil yang diformat
    """
    info = f"""
🚗 **{mobil['merek']} {mobil['model']}** ({mobil['tahun']})

Spesifikasi: {mobil['spesifikasi']}
Harga: {format_currency(mobil['harga'])}
Cicilan: {format_currency(mobil['cicilan'])}/bulan (36 bulan)
"""
    return info.strip()


def format_daftar_mobil(daftar_mobil: List[Dict]) -> str:
    """
    Format daftar mobil menjadi string yang readable
    
    Args:
        daftar_mobil: List dari semua mobil
        
    Returns:
        String berisi daftar mobil yang diformat
    """
    text = "📋 **DAFTAR MOBIL KAMI:**\n\n"
    
    # Kelompokkan berdasarkan kategori
    kategori_dict = {}
    for mobil in daftar_mobil:
        cat = mobil['kategori']
        if cat not in kategori_dict:
            kategori_dict[cat] = []
        kategori_dict[cat].append(mobil)
    
    # Format per kategori
    for kategori, mobils in kategori_dict.items():
        text += f"**{kategori}:**\n"
        for i, mobil in enumerate(mobils, 1):
            text += f"{i}. {mobil['merek']} {mobil['model']} ({mobil['tahun']}) - {format_currency(mobil['harga'])}\n"
        text += "\n"
    
    return text.strip()


def format_promosi(promosi: List[Dict]) -> str:
    """
    Format daftar promosi menjadi string yang readable
    
    Args:
        promosi: List dari semua promosi
        
    Returns:
        String berisi daftar promosi
    """
    text = "🎉 **PROMOSI SPESIAL BULAN INI:**\n\n"
    
    for i, promo in enumerate(promosi, 1):
        text += f"{i}. **{promo['judul']}**\n   {promo['deskripsi']}\n\n"
    
    text += "⏰ *Tawaran terbatas! Jangan lewatkan kesempatan ini.* 🚗"
    return text.strip()


def format_jam_operasional(jam_operasional: Dict) -> str:
    """
    Format jam operasional menjadi string
    
    Args:
        jam_operasional: Dictionary berisi jam buka
        
    Returns:
        String berisi jam operasional
    """
    text = "⏰ **JAM OPERASIONAL:**\n\n"
    
    for hari, jam in jam_operasional.items():
        text += f"📅 {hari}: {jam}\n"
    
    return text.strip()


def format_kontak(showroom_data: Dict) -> str:
    """
    Format informasi kontak menjadi string
    
    Args:
        showroom_data: Dictionary berisi data showroom
        
    Returns:
        String berisi informasi kontak
    """
    text = "**HUBUNGI KAMI:**\n\n"
    text += f"🏢 {showroom_data['nama']}\n"
    text += f"📍 {showroom_data['alamat']}\n\n"
    text += f"💬 WhatsApp: {showroom_data['whatsapp']}\n"
    text += f"📱 Instagram: {showroom_data.get('instagram', 'N/A')}\n"
    text += f"📧 Email: {showroom_data['email']}\n"
    text += f"🌐 Website: {showroom_data['website']}\n"
    text += f"\n✅ Tim kami siap membantu Anda 24/7!"
    
    return text.strip()


def create_system_prompt(showroom_data: Dict) -> str:
    """
    Membuat system prompt untuk Gemini dengan konteks showroom
    
    Args:
        showroom_data: Dictionary berisi data showroom
        
    Returns:
        String berisi system prompt
    """
    
    daftar_mobil_str = format_daftar_mobil(showroom_data['daftar_mobil'])
    
    prompt = f"""Anda adalah assistant customer service untuk {showroom_data['nama']}.

INFORMASI SHOWROOM:
- Nama: {showroom_data['nama']}
- Alamat: {showroom_data['alamat']}
- WhatsApp: {showroom_data['whatsapp']}
- Instagram: {showroom_data.get('instagram', 'N/A')}
- Email: {showroom_data['email']}
- Website: {showroom_data['website']}

JAM OPERASIONAL:
{format_jam_operasional(showroom_data['jam_operasional'])}

{daftar_mobil_str}

PROMOSI AKTIF:
{format_promosi(showroom_data['promosi'])}

LAYANAN:
{', '.join(showroom_data['layanan'])}

PETUNJUK:
1. Jawab pertanyaan customer dengan ramah dan profesional
2. Gunakan informasi di atas sebagai referensi
3. Tawarkan test drive gratis jika customer tertarik
4. Jika ada pertanyaan khusus, sarankan customer untuk menghubungi showroom
5. Selalu berakhir dengan ajakan untuk menghubungi atau berkunjung
6. Gunakan Bahasa Indonesia yang baik dan sopan
7. Berikan jawaban yang detail, ramah, dan helpful
"""
    
    return prompt


def get_safety_settings() -> List[Dict]:
    """
    Mendapatkan safety settings yang optimal untuk Gemini
    
    Returns:
        List of safety settings configuration
    """
    return [
        {
            "category": genai.types.HarmCategory.HARM_CATEGORY_HARASSMENT,
            "threshold": genai.types.HarmBlockThreshold.BLOCK_ONLY_HIGH,
        },
        {
            "category": genai.types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            "threshold": genai.types.HarmBlockThreshold.BLOCK_ONLY_HIGH,
        },
        {
            "category": genai.types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            "threshold": genai.types.HarmBlockThreshold.BLOCK_ONLY_HIGH,
        },
        {
            "category": genai.types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            "threshold": genai.types.HarmBlockThreshold.BLOCK_ONLY_HIGH,
        },
    ]


def try_gemini_model(model_name: str, prompt: str, showroom_data: Dict) -> Tuple[bool, str]:
    """
    Mencoba menggunakan satu model Gemini tertentu
    
    Args:
        model_name: Nama model yang akan dicoba
        prompt: Prompt untuk dikirim ke model
        showroom_data: Data showroom (untuk error handling)
        
    Returns:
        Tuple (success: bool, response: str)
    """
    try:
        print(f"[DEBUG] 🔄 Mencoba model: {model_name}...")
        
        # Buat instance model
        model = genai.GenerativeModel(
            model_name,
            safety_settings=get_safety_settings()
        )
        
        # Generate content
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=1000,
                temperature=0.7,
                top_p=0.95,
            )
        )
        
        print(f"[DEBUG] ✅ Model {model_name} berhasil!")
        print(f"[DEBUG] Response length: {len(response.text)} characters")
        
        return True, response.text.strip()
    
    except ValueError as ve:
        error_msg = str(ve)
        print(f"[DEBUG] ⚠️ ValueError pada model {model_name}: {error_msg[:100]}")
        return False, error_msg
    
    except TypeError as te:
        error_msg = str(te)
        print(f"[DEBUG] ⚠️ TypeError pada model {model_name}: {error_msg[:100]}")
        return False, error_msg
    
    except Exception as e:
        error_msg = str(e)
        print(f"[DEBUG] ⚠️ Error pada model {model_name}: {type(e).__name__} - {error_msg[:100]}")
        return False, error_msg


def get_response_from_gemini(user_message: str, showroom_data: Dict, conversation_history: List[Dict]) -> str:
    """
    Mendapatkan response dari Google Gemini API dengan multi-model fallback
    
    Strategi:
    1. Coba 8 model Gemini secara berurutan (dari terbaru ke lebih lama)
    2. Jika satu model gagal, otomatis try model berikutnya
    3. Jika semua gagal, return error message yang informatif
    
    Args:
        user_message: Pesan dari user
        showroom_data: Dictionary berisi data showroom
        conversation_history: History percakapan sebelumnya
        
    Returns:
        Response dari Gemini atau error message
    """
    
    try:
        print("\n" + "="*80)
        print("[DEBUG] 🚀 MEMULAI GEMINI REQUEST")
        print(f"[DEBUG] User message: {user_message[:100]}...")
        print(f"[DEBUG] Conversation history: {len(conversation_history)} messages")
        
        # Buat system prompt dengan konteks showroom
        system_prompt = create_system_prompt(showroom_data)
        
        # Siapkan conversation context
        conversation_text = system_prompt + "\n\n--- CONVERSATION HISTORY ---\n"
        
        # Tambahkan conversation history (max 5 pesan terakhir untuk efficiency)
        for msg in conversation_history[-5:]:
            role = "👤 User" if msg["role"] == "user" else "🤖 Assistant"
            conversation_text += f"{role}: {msg['content']}\n"
        
        # Tambahkan user message terbaru
        full_prompt = conversation_text + f"\n👤 User: {user_message}\n\nJawab dalam Bahasa Indonesia dengan ramah dan profesional:"
        
        print(f"[DEBUG] Full prompt length: {len(full_prompt)} characters")
        print("[DEBUG] 📋 Daftar model yang akan dicoba:")
        for i, model in enumerate(GEMINI_MODELS, 1):
            print(f"       {i}. {model}")
        print("-"*80)
        
        # Coba setiap model secara berurutan (fallback strategy)
        for idx, model_name in enumerate(GEMINI_MODELS, 1):
            print(f"\n[DEBUG] Attempt {idx}/{len(GEMINI_MODELS)}")
            success, response = try_gemini_model(model_name, full_prompt, showroom_data)
            
            if success:
                print(f"[DEBUG] 🎉 SUCCESS! Berhasil menggunakan model: {model_name}")
                print("="*80 + "\n")
                return response
        
        # Jika semua model gagal
        print("[DEBUG] ❌ Semua model gagal dicoba!")
        print("="*80 + "\n")
        
        return f"""❌ **Maaf, semua model Gemini sedang tidak tersedia.**

📌 **Informasi Teknis:**
- Sudah mencoba {len(GEMINI_MODELS)} model berbeda
- Semua model mengalami error

**Kemungkinan penyebab:**
1. ⚠️ API Key tidak valid atau sudah expired
2. 🔒 Quota API sudah habis
3. 🌐 Masalah koneksi internet
4. 🔧 Maintenance di server Google

**Solusi:**
1. Verifikasi API Key: https://makersuite.google.com/app/apikey
2. Check quota usage di Google Cloud Console
3. Coba lagi dalam beberapa saat

📞 **Hubungi support kami:**
- WhatsApp: {showroom_data['whatsapp']}
- Email: {showroom_data['email']}

Tim kami siap membantu! 🚗"""
    
    except Exception as e:
        error_type = type(e).__name__
        error_msg = str(e)
        
        print(f"[ERROR] Unhandled {error_type}: {error_msg}")
        print("="*80 + "\n")
        
        # Detect specific error types dan berikan response yang sesuai
        if "api_key" in error_msg.lower() or "authentication" in error_msg.lower() or "invalid" in error_msg.lower() or "unauthorized" in error_msg.lower():
            return f"""❌ **Authentication Error - API Key Problem**

**Pesan Error:**
{error_msg[:300]}

**Penyebab kemungkinan:**
- API Key tidak valid
- API Key sudah expired
- API Key direvoke
- API Key belum activated

**Solusi:**
1. Buka: https://makersuite.google.com/app/apikey
2. Regenerate API Key baru
3. Update di Streamlit Cloud Secrets
4. Refresh aplikasi

📞 **Hubungi support:**
WhatsApp: {showroom_data['whatsapp']}
Email: {showroom_data['email']}"""
        
        elif "quota" in error_msg.lower() or "rate limit" in error_msg.lower() or "too many" in error_msg.lower() or "resource exhausted" in error_msg.lower():
            return f"""⚠️ **Quota/Rate Limit Error**

**Pesan Error:**
{error_msg[:300]}

**Penyebab:**
- Terlalu banyak request dalam waktu singkat
- Quota API sudah habis bulan ini
- Rate limit terlampaui

**Solusi:**
1. ⏳ Tunggu beberapa saat (30 detik - 1 menit)
2. 🔄 Coba lagi dengan pertanyaan yang lebih sederhana
3. 📊 Check quota: https://console.cloud.google.com/apis

💡 **Tips:**
- Batasi panjang percakapan
- Hindari pertanyaan yang terlalu kompleks
- Coba lagi di jam yang berbeda

📞 **Hubungi support:**
WhatsApp: {showroom_data['whatsapp']}"""
        
        elif "not found" in error_msg.lower() or "404" in error_msg or "does not exist" in error_msg.lower() or "model not found" in error_msg.lower():
            return f"""❌ **Model Error - Model Tidak Tersedia**

**Pesan Error:**
{error_msg[:300]}

**Penyebab:**
- Model Gemini yang diminta tidak ada
- Model belum dideploy di region Anda
- Model sudah deprecated

**Informasi Model:**
Kami sudah mencoba 8 model Gemini terbaru

📞 **Hubungi support:**
Email: {showroom_data['email']}
WhatsApp: {showroom_data['whatsapp']}"""
        
        elif "blocked" in error_msg.lower() or "safety" in error_msg.lower():
            return f"""⚠️ **Safety Filter - Response Diblokir**

**Pesan Error:**
{error_msg[:300]}

**Penyebab:**
Response atau pertanyaan Anda diblokir oleh safety filter Gemini untuk keamanan.

**Solusi:**
1. 📝 Coba dengan pertanyaan yang berbeda
2. 🎯 Hindari topik sensitif
3. 📞 Hubungi support jika ini adalah pertanyaan legitimate

💡 **Contoh pertanyaan yang aman:**
- "Berapa harga Toyota Avanza?"
- "Ada promo apa bulan ini?"
- "Jam operasional showroom?"

📞 **Hubungi support:**
WhatsApp: {showroom_data['whatsapp']}"""
        
        else:
            return f"""❌ **Terjadi Error Tak Terduga**

**Tipe Error:** {error_type}

**Pesan Error:**
{error_msg[:300]}

**Kemungkinan Penyebab:**
- Masalah koneksi internet
- Maintenance server Google
- Bug di sistem
- Konfigurasi salah

**Solusi Umum:**
1. 🔄 Refresh halaman aplikasi
2. 🌐 Check koneksi internet Anda
3. ⏳ Tunggu 1-2 menit dan coba lagi

📞 **Hubungi support jika error berlanjut:**
Email: {showroom_data['email']}
WhatsApp: {showroom_data['whatsapp']}"""