"""
helper.py - Fungsi-fungsi helper untuk chatbot
"""

import google.generativeai as genai
from typing import List, Dict, Any

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
**{mobil['merek']} {mobil['model']}** ({mobil['tahun']})

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
    text = "**DAFTAR MOBIL KAMI:**\n\n"
    
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
    text = "**PROMOSI SPESIAL BULAN INI:**\n\n"
    
    for i, promo in enumerate(promosi, 1):
        text += f"{i}. **{promo['judul']}**\n   {promo['deskripsi']}\n\n"
    
    text += "*Tawaran terbatas! Jangan lewatkan kesempatan ini.*"
    return text.strip()


def format_jam_operasional(jam_operasional: Dict) -> str:
    """
    Format jam operasional menjadi string
    
    Args:
        jam_operasional: Dictionary berisi jam buka
        
    Returns:
        String berisi jam operasional
    """
    text = "**JAM OPERASIONAL:**\n\n"
    
    for hari, jam in jam_operasional.items():
        text += f"{hari}: {jam}\n"
    
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
    text += f"{showroom_data['nama']}\n"
    text += f"{showroom_data['alamat']}\n\n"
    text += f"WhatsApp: {showroom_data['whatsapp']}\n"
    text += f"Instagram: {showroom_data.get('instagram', 'N/A')}\n"
    text += f"Email: {showroom_data['email']}\n"
    text += f"Website: {showroom_data['website']}\n"
    text += f"\nTim kami siap membantu Anda 24/7!"
    
    return text.strip()


def create_system_prompt(showroom_data: Dict) -> str:
    """
    Membuat system prompt untuk GPT dengan konteks showroom
    
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
"""
    
    return prompt


def get_response_from_gemini(user_message: str, showroom_data: Dict, conversation_history: List[Dict]) -> str:
    """
    Mendapatkan response dari Google Gemini API dengan error handling yang proper
    
    Args:
        user_message: Pesan dari user
        showroom_data: Dictionary berisi data showroom
        conversation_history: History percakapan sebelumnya
        
    Returns:
        Response dari Gemini
    """
    
    try:
        # Buat system prompt dengan konteks showroom
        system_prompt = create_system_prompt(showroom_data)
        
        # Siapkan conversation context
        conversation_text = system_prompt + "\n\n"
        
        # Tambahkan conversation history 
        for msg in conversation_history[-5:]:
            role = "User" if msg["role"] == "user" else "Assistant"
            conversation_text += f"{role}: {msg['content']}\n"
        
        # Tambahkan user message terbaru
        full_prompt = conversation_text + f"User: {user_message}\n\nJawab dalam Bahasa Indonesia dengan ramah dan profesional:"
        
        print(f"[DEBUG] Mengirim request ke Gemini 2.0 Flash...")
        print(f"[DEBUG] Prompt length: {len(full_prompt)} characters")
        
        # Gunakan Gemini 2.0 Flash model
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Panggil Gemini API
        response = model.generate_content(
            full_prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=1000,
                temperature=0.7,
                top_p=0.95
            ),
            safety_settings=[
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
        )
        
        print(f"[DEBUG] ✓ Response berhasil diterima!")
        print(f"[DEBUG] Response length: {len(response.text)} characters")
        return response.text
    
    except ValueError as ve:
        error_msg = str(ve)
        print(f"[ERROR] ValueError: {error_msg}")
        return f"❌ **Value Error**: {error_msg}\n\n📞 Hubungi support: {showroom_data['whatsapp']}"
    
    except TypeError as te:
        error_msg = str(te)
        print(f"[ERROR] TypeError: {error_msg}")
        return f"❌ **Type Error**: {error_msg}\n\n📞 Hubungi support: {showroom_data['whatsapp']}"
    
    except Exception as e:
        error_type = type(e).__name__
        error_msg = str(e)
        
        print(f"[ERROR] {error_type}: {error_msg}")
        
        if "API key" in error_msg or "authentication" in error_msg.lower() or "invalid" in error_msg.lower():
            return f"❌ **Authentication Error**: API Key Gemini tidak valid atau sudah expired.\n\nPesan: {error_msg[:200]}\n\n📍 Verifikasi API Key di: https://makersuite.google.com/app/apikey\n\n📞 Hubungi support: {showroom_data['whatsapp']}"
        
        elif "quota" in error_msg.lower() or "rate limit" in error_msg.lower() or "too many" in error_msg.lower():
            return f"⚠️ **Quota/Rate Limit**: Terlalu banyak request atau quota habis.\n\nPesan: {error_msg[:200]}\n\n📞 Coba lagi dalam beberapa saat atau hubungi: {showroom_data['whatsapp']}"
        
        elif "not found" in error_msg.lower() or "404" in error_msg or "does not exist" in error_msg.lower():
            return f"❌ **Model Error**: Model Gemini tidak tersedia saat ini.\n\nPesan: {error_msg[:200]}\n\n💡 Pastikan API Key valid dan akun sudah aktif\n\n📞 Hubungi support: {showroom_data['whatsapp']}"
        
        elif "blocked" in error_msg.lower() or "safety" in error_msg.lower():
            return f"⚠️ **Safety Filter**: Pertanyaan atau response diblokir oleh safety filter Gemini.\n\nPesan: {error_msg[:200]}\n\n💡 Coba dengan pertanyaan yang berbeda\n\n📞 Hubungi support: {showroom_data['whatsapp']}"
        
        else:
            return f"❌ **{error_type}**: Terjadi error saat memproses request.\n\nPesan: {error_msg[:200]}\n\n📞 Hubungi support: {showroom_data['whatsapp']}"