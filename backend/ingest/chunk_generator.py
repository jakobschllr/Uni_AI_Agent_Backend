#nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from langchain.text_splitter import RecursiveCharacterTextSplitter


# received text raw data from file and returns sentence-chunks, paragraph chunks and page chunks
def get_chunks(lines, language):
    
    joined_text = ' '.join(lines)
    sentences = sent_tokenize(joined_text, language=language)
   
    chunk_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    chunks = chunk_splitter.split_text(" ".join(sentences)) # so unterbrechen Chunks keine ganzen Sätze

    return sentences, chunks