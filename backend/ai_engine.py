import os
import json
import google.generativeai as genai
import streamlit as st

def get_gemini_response(user_input, target_lang):
    """
    Sends the user input to Gemini API and returns structured JSON.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("❌ API Key missing! Please ensure GEMINI_API_KEY is set in your .env file.")
        return None

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')

        # Advanced Prompt Engineering for Structured HTML Output
        prompt = f"""
        You are a strict English Professor. 
        Analyze the following English text: "{user_input}"
        
        Target Translation Language: {target_lang}

        Tasks:
        1. **Correct**: Fix grammar, spelling, and tense errors.
        2. **Explain**: Provide a comprehensive grammar explanation in **ENGLISH**.
            - Format strictly as an **HTML string** (do not use Markdown).
            - Start with a **constructive paragraph** summarizing the user's main issues (e.g., "Your narrative struggles with past tense consistency...").
            - Follow with an **Ordered List (<ol>)** of specific errors found.
            - For each list item (<li>), start with a **Bold Category (<b>)** (e.g., <b>Tense Inconsistency:</b>, <b>Grammar - Prepositions:</b>), then clearly explain the rule broken.
        3. **Translate**: Translate the *Corrected* text into {target_lang}.
        4. **Categorize**: Count mistakes by type (Grammar, Spelling, Punctuation, Tense, Vocabulary).
        5. **Idiom**: Suggest 1 professional English idiom that fits the context of this sentence.

        Output strictly in this JSON format:
        {{
            "corrected_text": "...",
            "explanation_english": "...",
            "translated_text": "...",
            "error_counts": {{ "Grammar": 0, "Spelling": 0, "Tense": 0, "Vocabulary": 0, "Punctuation": 0 }},
            "smart_idiom": "...",
            "idiom_meaning": "..."
        }}
        """
        
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        st.error(f"API Connection Error: {e}")
        return None

def parse_response(response_text):
    """Parses JSON response from Gemini."""
    try:
        cleaned_json = response_text.strip().replace("```json", "").replace("```", "")
        return json.loads(cleaned_json)
    except json.JSONDecodeError:
        return None