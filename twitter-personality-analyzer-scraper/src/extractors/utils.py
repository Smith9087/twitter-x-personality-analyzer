thonimport json

def clean_text(text):
    # This function cleans tweet text by removing unwanted characters or links
    return ' '.join(word for word in text.split() if not word.startswith('http'))