import streamlit as st
import pandas as pd
from dotenv import load_dotenv

# Import Modules
from frontend.styles import load_custom_css
from frontend.components import render_sidebar, render_hero_section, render_result_card
from backend.ai_engine import get_gemini_response, parse_response
from backend.audio_engine import text_to_speech
from utils.helpers import generate_diff_html, get_readability_score

# --- 1. Init & Config ---
load_dotenv()
st.set_page_config(
    page_title="LinguistAI - Pro English Tutor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. Load UI Styles ---
load_custom_css()

# --- 3. Sidebar Logic ---
lang_data = render_sidebar()
target_lang_name = lang_data["name"]
target_lang_code = lang_data["code"]

# --- 4. Main Page Layout ---
render_hero_section(target_lang_name)

# Input Container
with st.container():
    st.markdown("""
    <div class="helper-box">
        <b>👋 How to use:</b> Write your sentence in English (even if it's broken or incorrect). 
        The AI will fix the grammar, explain the rules, and translate it for you!
    </div>
    """, unsafe_allow_html=True)
    
    user_input = st.text_area(
        "Enter English text to analyze:", 
        height=150, 
        placeholder="Type here... (e.g., 'I am go to market yesterday for buy vegetable')",
        label_visibility="collapsed"
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        analyze_btn = st.button("✨ Analyze & Fix English", type="primary")

# --- 5. Application Logic ---
if analyze_btn:
    if not user_input.strip():
        st.warning("⚠️ Please enter some text first.")
    else:
        with st.spinner("🤖 Analyzing syntax, semantics, and context..."):
            
            # Call Backend AI
            raw_response = get_gemini_response(user_input, target_lang_name)
            
            if raw_response:
                data = parse_response(raw_response)
                
                if data:
                    st.markdown("---")
                    
                    # --- Section 1: Correction & Translation ---
                    c1, c2 = st.columns(2)
                    
                    # Correction Column
                    with c1:
                        render_result_card("✅ Corrected English", data['corrected_text'], "card-accent-green")
                        audio_en = text_to_speech(data['corrected_text'], 'en')
                        if audio_en: st.audio(audio_en, format='audio/mp3')

                    # Translation Column
                    with c2:
                        render_result_card(f"🗣️ Translation ({target_lang_name})", 
                                         f"<span class='translation-text'>{data['translated_text']}</span>", 
                                         "card-accent-blue")
                        audio_native = text_to_speech(data['translated_text'], lang=target_lang_code)
                        if audio_native: 
                            st.audio(audio_native, format='audio/mp3')
                        else:
                            st.caption(f"Audio not available for {target_lang_name}")

                    # --- Section 2: Analytics Dashboard ---
                    st.markdown("### 📊 Analysis Dashboard")
                    tab1, tab2, tab3 = st.tabs(["📝 Explanation", "📈 Mistake Analytics", "💡 Smart Idiom"])
                    
                    with tab1:
                        # Render HTML explanation directly
                        render_result_card("👩‍🏫 Tutor's Feedback", data['explanation_english'], "card-accent-purple")
                        
                        st.markdown("#### 🔍 Changes Highlighted")
                        diff_html = generate_diff_html(user_input, data['corrected_text'])
                        st.markdown(f'<div style="background-color:white; padding:20px; border-radius:12px; border:1px solid #eee; line-height:2.0; font-family:monospace;">{diff_html}</div>', unsafe_allow_html=True)

                    with tab2:
                        errors = data.get('error_counts', {})
                        if any(errors.values()):
                            df = pd.DataFrame(list(errors.items()), columns=["Error Type", "Count"])
                            st.bar_chart(df.set_index("Error Type"))
                        else:
                            st.success("🎉 No major errors found! Excellent work.")
                            
                        score = get_readability_score(data['corrected_text'])
                        col_m1, col_m2 = st.columns(2)
                        col_m1.metric("Readability Score", f"{score:.1f}", "Higher is easier")

                    with tab3:
                        st.markdown(f"""
                        <div class="result-card" style="background: linear-gradient(to right, #ffffff, #f0f9ff); border-left: 5px solid #F59E0B;">
                            <div class="card-title" style="color:#D97706;">🌟 Level Up Your Vocabulary</div>
                            <div class="card-content">
                                <b>Instead of:</b> "{data['corrected_text']}"<br><br>
                                <b>Try this idiom:</b> <span style="color:#D97706; font-weight:bold; font-size:1.3em;">{data['smart_idiom']}</span><br>
                                <i style="font-size:0.9em; color:#666;">Meaning: {data['idiom_meaning']}</i>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                    # --- Download Report ---
                    report_text = f"Original: {user_input}\nCorrected: {data['corrected_text']}\nTranslation: {data['translated_text']}"
                    st.download_button("📥 Download Analysis Report", report_text, file_name="linguist_report.txt")
                    
                else:
                    st.error("Error processing AI response. Please try again.")