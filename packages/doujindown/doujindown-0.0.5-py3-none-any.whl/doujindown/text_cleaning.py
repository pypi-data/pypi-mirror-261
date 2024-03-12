import re
import string

# TEXT FORMATTING FUNCTIONS 
# hard cleans
def hard_clean(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = text.replace('\n', ' ')
    text = re.sub(r'http.*', '', text)
    text = text.strip(string.punctuation + string.whitespace)
    return text

# soft clean leaves some formatting intact
def soft_clean(text: str, allow_commas: bool=True, space_to_underscore: bool=True, lower: bool=True, remove_weird: bool=False) -> str:
    text = re.sub(r"[\n'\"]", '', text) if allow_commas else re.sub(r"[\n'\",]", '', text)
    text = text.strip(string.whitespace)
    if space_to_underscore: text = re.sub(r" ", '_', text)
    if lower: text = text.lower()
    if remove_weird: text = re.sub(r'[^\w\s]', '', text)
    return text