import re

def chunk_text(text, chunk_size=1000, overlap=200):
    
    sentences = re.split(r'(?<=[.!?]) +', text)  # Split by sentence
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) < chunk_size:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())

            # Retain overlap portion from the previous chunk
            current_chunk = current_chunk[-overlap:] + sentence + " "

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks