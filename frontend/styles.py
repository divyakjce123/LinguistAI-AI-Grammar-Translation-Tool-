import streamlit as st

def load_custom_css():
    st.markdown("""
    <style>
        /* Import Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        /* Global Styles */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            color: #1F2937;
        }
        
        .stApp {
            background-color: #F9FAFB; /* Very light gray */
        }

        /* Animation Keyframes */
        @keyframes slideIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Header Styling */
        .hero-title {
            color: #4338CA; /* Indigo 700 */
            font-weight: 800;
            font-size: 3rem;
            letter-spacing: -1px;
            margin-bottom: 0.5rem;
            text-align: center;
            background: -webkit-linear-gradient(45deg, #4F46E5, #9333EA);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero-subtitle {
            color: #6B7280;
            font-size: 1.2rem;
            text-align: center;
            margin-bottom: 2rem;
        }

        /* Card Styling */
        .result-card {
            background-color: white;
            padding: 24px;
            border-radius: 16px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            margin-bottom: 20px;
            border: 1px solid #F3F4F6;
            border-left: 5px solid #4F46E5;
            transition: transform 0.2s, box-shadow 0.2s;
            animation: slideIn 0.5s ease-out;
        }
        .result-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }
        
        .card-accent-green { border-left-color: #10B981; }
        .card-accent-blue { border-left-color: #3B82F6; }
        .card-accent-purple { border-left-color: #8B5CF6; }

        .card-title {
            color: #9CA3AF;
            text-transform: uppercase;
            font-size: 0.8rem;
            font-weight: 700;
            letter-spacing: 0.05em;
            margin-bottom: 8px;
        }
        .card-content {
            font-size: 1.2rem;
            line-height: 1.6;
            color: #111827;
            font-weight: 500;
        }
        .translation-text {
            color: #4B5563;
            font-style: italic;
        }

        /* Input Area Styling */
        .stTextArea textarea {
            border-radius: 12px;
            border: 2px solid #E5E7EB;
            padding: 15px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        .stTextArea textarea:focus {
            border-color: #6366F1;
            box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.1);
        }

        /* Button Styling */
        .stButton button {
            background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
            color: white;
            border: none;
            padding: 12px 28px;
            border-radius: 12px;
            font-weight: 600;
            font-size: 16px;
            transition: all 0.3s ease;
            width: 100%;
            height: 55px;
        }
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 12px -3px rgba(124, 58, 237, 0.4);
        }

        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: #FFFFFF;
            border-right: 1px solid #F3F4F6;
        }

        /* Helper Box */
        .helper-box {
            background-color: #EFF6FF;
            border: 1px solid #DBEAFE;
            border-radius: 10px;
            padding: 15px;
            color: #1E40AF;
            font-size: 0.9rem;
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)