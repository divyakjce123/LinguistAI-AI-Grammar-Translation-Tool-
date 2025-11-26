import difflib
import textstat

def generate_diff_html(text1, text2):
    """Generates HTML string highlighting differences between two texts."""
    d = difflib.Differ()
    diff = list(d.compare(text1.split(), text2.split()))
    html = []
    for token in diff:
        if token.startswith('+ '):
            html.append(f'<span style="background-color:#DEF7EC; color:#046C4E; padding:2px 6px; border-radius:4px; border-bottom:2px solid #31C48D; font-weight:600;">{token[2:]}</span>')
        elif token.startswith('- '):
            html.append(f'<span style="background-color:#FDE8E8; color:#C81E1E; padding:2px 6px; border-radius:4px; text-decoration:line-through; opacity:0.7;">{token[2:]}</span>')
        elif not token.startswith('? '):
            html.append(token[2:])
    return ' '.join(html)

def get_readability_score(text):
    """Calculates Flesch Reading Ease score."""
    try:
        return textstat.flesch_reading_ease(text)
    except:
        return 0.0