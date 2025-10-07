import re
import string

def clean_text(msg):
    msg = msg.lower()
    msg = re.sub(r'\d+', '', msg)
    msg = msg.translate(str.maketrans('', '', string.punctuation))
    return msg.strip()
