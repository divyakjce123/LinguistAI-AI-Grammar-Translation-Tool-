import streamlit as st
from utils.config import LANGUAGES

def render_sidebar():
    """Renders the sidebar configuration."""
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/4712/4712009.png", width=70)
        st.markdown("## **LinguistAI**")
        st.markdown("### *Pro English Tutor*")
        st.markdown("---")
        
        st.header("⚙️ Preferences")
        st.info("💡 **Tip:** Select the language for translation and audio output.")
        
        # Dropdown
        selected_lang_label = st.selectbox("Native Language:", list(LANGUAGES.keys()))
        lang_data = LANGUAGES[selected_lang_label]
        
        st.markdown("---")
        st.markdown("### 👨‍💻 About")
        st.info("Advanced AI Website designed for English learners. Handles English, Grammar correction, and Contextual Translation.")
        
        return lang_data

def render_hero_section(lang_name):
    """Renders the main title area."""
    st.markdown('<div class="hero-title">LinguistAI</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Your Personal AI English Professor & Translator</div>', unsafe_allow_html=True)
    st.caption(f"**Current Mode:** Translating to **{lang_name}**")

def render_result_card(title, content, accent_class=""):
    """Renders a styled result card."""
    st.markdown(f"""
    <div class="result-card {accent_class}">
        <div class="card-title">{title}</div>
        <div class="card-content">{content}</div>
    </div>
    """, unsafe_allow_html=True)