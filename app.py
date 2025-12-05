import streamlit as st
import google.generativeai as genai
from data import get_showroom_data
from helper import format_currency, search_mobil, get_response_from_gemini
import os
from dotenv import load_dotenv

# Muat environment variables
load_dotenv()

# Set API key Google Gemini
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("❌ GEMINI_API_KEY tidak ditemukan di file .env")
    st.stop()

genai.configure(api_key=api_key)

# Konfigurasi halaman
st.set_page_config(
    page_title="Chatbot Showroom Mobil Sungkang",
    page_icon="🏎",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS custom
st.markdown("""
    <style>
        .stChatMessage {
            border-radius: 12px;
            padding: 12px 16px;
            margin: 8px 0;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
        }
        
        /* Pesan user - tema Purple/Blue */
        .stChatMessage:has(> div > .stMarkdown) {
            background-color: #f0f2f6;
            border-left: 4px solid #667eea;
        }
        
        /* Pesan bot - tema light dengan accent */
        .stChatMessage[data-testid="stChatMessage"]:has(.stMarkdown:contains('Bot')) {
            background-color: #e8f0f8;
            border-left: 4px solid #764ba2;
        }
        
        .header-container {
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 10px;
            color: white;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.2);
        }
        .header-container h1 {
            margin: 0;
            font-size: 42px;
            font-weight: bold;
            color: white !important;
        }
        .header-text h1 {
            margin: 0;
            font-size: 24px;
            font-weight: 600;
            color: white !important;
        }
        .status-badge {
            display: inline-block;
            background-color: #4CAF50;
            color: white;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: bold;
            box-shadow: 0 2px 6px rgba(76, 175, 80, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

# Inisialisasi session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Halo! Selamat datang di Showroom Mobil Sungkang. Saya siap membantu Anda mencari mobil impian. Ada yang bisa saya bantu?"}
    ]

if "showroom_data" not in st.session_state:
    st.session_state.showroom_data = get_showroom_data()

# Header
st.markdown("""
    <div class="header-container">
        <div>
            <h1>🚗 Showroom Mobil Sungkang</h1>
            <p><span class="status-badge">● Online</span> - Siap membantu Anda</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Tampilkan pesan chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input chat
if prompt := st.chat_input("Tanya tentang mobil, harga, promo, dll..."):
    # Tambahkan pesan user ke history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Generating..."):
            print(f"[DEBUG] Pesan user: {prompt}")
            
            # Dapatkan response dari Gemini dengan konteks showroom
            response = get_response_from_gemini(
                prompt,
                st.session_state.showroom_data,
                st.session_state.messages[:-1]  # Semua pesan kecuali pesan user terakhir
            )
            
            print(f"[DEBUG] Response diterima: {response[:100]}...")
        
        st.markdown(response)
    
    # Tambahkan response assistant ke history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Tombol aksi cepat
st.markdown("---")
st.markdown("**Pertanyaan Cepat:**")
col1, col2, col3, col4 = st.columns(4)

# Inisialisasi quick_action flag di session state
if "quick_action_processed" not in st.session_state:
    st.session_state.quick_action_processed = False

with col1:
    if st.button("📋 Daftar Mobil", use_container_width=True, key="btn_daftar"):
        if not st.session_state.quick_action_processed:
            st.session_state.quick_action_processed = True
            user_input = "Apa saja daftar mobil yang tersedia?"
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Generate response secara langsung
            with st.spinner("Generating..."):
                response = get_response_from_gemini(
                    user_input,
                    st.session_state.showroom_data,
                    st.session_state.messages[:-1]
                )
            
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

with col2:
    if st.button("🎁 Promo", use_container_width=True, key="btn_promo"):
        if not st.session_state.quick_action_processed:
            st.session_state.quick_action_processed = True
            user_input = "Apa promo terbaru bulan ini?"
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Generate response secara langsung
            with st.spinner("Generating..."):
                response = get_response_from_gemini(
                    user_input,
                    st.session_state.showroom_data,
                    st.session_state.messages[:-1]
                )
            
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

with col3:
    if st.button("🕐 Jam Buka", use_container_width=True, key="btn_jam"):
        if not st.session_state.quick_action_processed:
            st.session_state.quick_action_processed = True
            user_input = "Berapa jam operasional showroom?"
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Generate response secara langsung
            with st.spinner("Generating..."):
                response = get_response_from_gemini(
                    user_input,
                    st.session_state.showroom_data,
                    st.session_state.messages[:-1]
                )
            
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

with col4:
    if st.button("✉️ Kontak", use_container_width=True, key="btn_kontak"):
        if not st.session_state.quick_action_processed:
            st.session_state.quick_action_processed = True
            user_input = "Bagaimana cara menghubungi showroom?"
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Generate response secara langsung
            with st.spinner("Generating..."):
                response = get_response_from_gemini(
                    user_input,
                    st.session_state.showroom_data,
                    st.session_state.messages[:-1]
                )
            
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.rerun()

# Reset flag setelah rendering
st.session_state.quick_action_processed = False

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; font-size: 12px; margin-top: 20px;">
        <p>⚙️ Powered by Google Gemini | Showroom Mobil Sungkang</p>
        <p>📍 Jl. Gatot Subroto No. 45, Semarang | WhatsApp: +62 812-3456-7890</p>
    </div>
""", unsafe_allow_html=True)