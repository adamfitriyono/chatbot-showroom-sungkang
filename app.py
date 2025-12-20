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

# Font Awesome CDN
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
""", unsafe_allow_html=True)

# CSS custom
st.markdown("""
    <style>
        @keyframes gradientShift {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }
        
        @keyframes shimmer {
            0% {
                transform: translateX(-100%);
            }
            100% {
                transform: translateX(100%);
            }
        }
        
        @keyframes iconFloat {
            0%, 100% {
                transform: translateY(0px);
            }
            50% {
                transform: translateY(-5px);
            }
        }
        
        @keyframes pulse {
            0%, 100% {
                box-shadow: 0 4px 12px rgba(17, 119, 255, 0.2);
            }
            50% {
                box-shadow: 0 4px 20px rgba(17, 119, 255, 0.4);
            }
        }
        
        @keyframes badgePulse {
            0%, 100% {
                box-shadow: 0 0 10px rgba(76, 175, 80, 0.5), 0 0 20px rgba(76, 175, 80, 0.3), 0 2px 6px rgba(76, 175, 80, 0.2);
                transform: scale(1);
            }
            50% {
                box-shadow: 0 0 20px rgba(76, 175, 80, 0.8), 0 0 30px rgba(76, 175, 80, 0.5), 0 2px 10px rgba(76, 175, 80, 0.4);
                transform: scale(1.05);
            }
        }
        
        @keyframes dotBlink {
            0%, 100% {
                opacity: 1;
                transform: scale(1);
            }
            50% {
                opacity: 0.5;
                transform: scale(0.8);
            }
        }
        
        @keyframes badgeGlow {
            0%, 100% {
                background-color: #4CAF50;
            }
            50% {
                background-color: #66BB6A;
            }
        }
        .stChatMessage {
            border-radius: 12px;
            padding: 12px 16px;
            margin: 8px 0;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
        }
        
        /* Pesan user - tema Blue */
        .stChatMessage:has(> div > .stMarkdown) {
            background-color: #f0f2f6;
            border-left: 4px solid #1177FF;
        }
        
        /* Pesan bot - tema light dengan accent biru */
        .stChatMessage[data-testid="stChatMessage"]:has(.stMarkdown:contains('Bot')) {
            background-color: #e8f0f8;
            border-left: 4px solid #0d5fcc;
        }
        
        .header-container {
            display: flex;
            flex-direction: column;
            padding: 24px 28px;
            background: linear-gradient(135deg, #1177FF 0%, #2a8fff 25%, #0d5fcc 50%, #1177FF 75%, #0d5fcc 100%);
            background-size: 200% 200%;
            border-radius: 12px;
            color: white;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(17, 119, 255, 0.2);
            position: relative;
            overflow: hidden;
            animation: gradientShift 8s ease infinite, pulse 3s ease-in-out infinite;
        }
        
        .header-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            animation: shimmer 3s infinite;
        }
        
        .header-icon {
            font-size: 48px;
            color: white;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
            margin-right: 18px;
            animation: iconFloat 3s ease-in-out infinite;
            display: inline-block;
            flex-shrink: 0;
        }
        .header-container h1 {
            margin: 0;
            font-size: 42px;
            font-weight: bold;
            color: white !important;
            display: flex;
            align-items: center;
            position: relative;
            z-index: 1;
            line-height: 1.2;
            margin-bottom: 0;
        }
        
        .header-container > div {
            position: relative;
            z-index: 1;
            width: 100%;
        }
        
        .header-container p {
            margin: 12px 0 0 0;
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 14px;
            color: rgba(255, 255, 255, 0.95);
            line-height: 1.5;
        }
        .header-text h1 {
            margin: 0;
            font-size: 24px;
            font-weight: 600;
            color: white !important;
        }
        .status-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background-color: #4CAF50;
            color: white;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: bold;
            box-shadow: 0 0 10px rgba(76, 175, 80, 0.5), 0 0 20px rgba(76, 175, 80, 0.3), 0 2px 6px rgba(76, 175, 80, 0.2);
            animation: badgePulse 2s ease-in-out infinite, badgeGlow 2s ease-in-out infinite;
            position: relative;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .status-badge::before {
            content: '';
            width: 8px;
            height: 8px;
            background-color: white;
            border-radius: 50%;
            display: inline-block;
            animation: dotBlink 1.5s ease-in-out infinite;
            box-shadow: 0 0 6px rgba(255, 255, 255, 0.8);
        }
        
        .header-helper-text {
            font-weight: 400;
            letter-spacing: 0.3px;
        }
        
        .footer-container {
            background: linear-gradient(135deg, #18202F 0%, #1f2a3f 100%);
            border-radius: 12px;
            padding: 20px 24px;
            margin-top: 30px;
            text-align: center;
            color: white;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }
        
        .footer-container p {
            margin: 0;
            font-size: 13px;
            line-height: 1.6;
            color: rgba(255, 255, 255, 0.95);
        }
        
        .footer-container .footer-line-1 {
            font-size: 14px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            flex-wrap: wrap;
        }
        
        .footer-container .footer-separator {
            width: 70%;
            height: 1px;
            background: rgba(255, 255, 255, 0.25);
            margin: 12px auto;
        }
        
        .footer-container .footer-line-2 {
            font-size: 12px;
            color: rgba(255, 255, 255, 0.85);
            margin-top: 12px;
        }
        
        .footer-icon {
            font-size: 14px;
            margin-right: 4px;
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
            <h1><i class="fas fa-car-side header-icon"></i> Showroom Mobil Sungkang</h1>
            <p><span class="status-badge">Online</span><span class="header-helper-text">Siap membantu Anda</span></p>
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
        with st.spinner("Tunggu ya..."):
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
            with st.spinner("Tunggu ya..."):
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
            with st.spinner("Tunggu ya..."):
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
            with st.spinner("Tunggu ya..."):
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
            with st.spinner("Tunggu ya..."):
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
st.markdown("""
    <div class="footer-container">
        <p class="footer-line-1">
            <span><i class="fas fa-map-marker-alt footer-icon"></i> Jl. Gatot Subroto No. 45, Semarang</span>
            <span>|</span>
            <span><i class="fas fa-robot footer-icon"></i> Powered by Google Gemini</span>
        </p>
        <div class="footer-separator"></div>
        <p class="footer-line-2">
            @2025 Showroom Mobil Sungkang. All rights reserved.
        </p>
    </div>
""", unsafe_allow_html=True)