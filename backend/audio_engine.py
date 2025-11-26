from gtts import gTTS
import io

def text_to_speech(text, lang='en'):
    """Generates MP3 audio bytes from text."""
    try:
        if not text: 
            return None
        tts = gTTS(text=text, lang=lang)
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        return mp3_fp
    except Exception as e:
        print(f"TTS Error: {e}")
        return None