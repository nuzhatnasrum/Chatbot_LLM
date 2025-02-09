import re

def split_text_into_chunks(text, max_length=1000, overlap_length=200):
    sentences = re.split(r'(?<=[.!?]) +', text) 
    chunk_list, temp_chunk = [], ""

    for line in sentences:
        if len(temp_chunk) + len(line) < max_length:
            temp_chunk += line + " "
        else:
            chunk_list.append(temp_chunk.strip())
            temp_chunk = temp_chunk[-overlap_length:] + line + " "  

    if temp_chunk:
        chunk_list.append(temp_chunk.strip())

    return chunk_list
