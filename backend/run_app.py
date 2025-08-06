from typing import Union
from ingest.chunk_generator import get_chunks
from ingest.data_extractor import DataExtractor
from retrieval.database import DatabaseHandler
from nlp.remove_stopwords import remove_stopwords
from llm.Chat import Chat
import os


PDF_PATH = "/Users/jakobschiller/Desktop/Projekte/AI_Uni_Quiz/file_handling/Skript_Lineare_Algebra.pdf"
db_handler = DatabaseHandler()
extractor = DataExtractor()


def create_collection_for_pdf(path, user_id, collection_id, language):
    pdf_data = extractor.get_pdf_data(path=path)
    cleaned_data = extractor.clean_data(pdf_data)
    sentences, chunks = get_chunks(cleaned_data, language)
    collection = db_handler.create_collection(user_id, collection_id)
    db_handler.add_to_collection(collection, chunks)


def query_existing_db(user_id, collection_id, query):
    collection = db_handler.get_collection(user_id, collection_id)
    if collection != None:
        return collection.query(
            query_texts=query,
            n_results=5
            )['documents']
    else:
        return None

#create_collection_for_pdf(PDF_PATH, "0", "0", "german")

def get_db_response(user_id, collection_id, raw_user_input):
    cleaned_user_input = extractor.clean_data(raw_user_input)
    without_stopwords = remove_stopwords(cleaned_user_input)
    print("Vecot DB Query: ", without_stopwords)
    results = query_existing_db(user_id, collection_id, cleaned_user_input)
    return results

user_request = "Was ist ein Vektor?"

db_response = get_db_response("0", "0", user_request)
chat = Chat(0)
answer = chat.generate_answer(user_request, db_response)

print(answer)

# run file with python -m api.index from AI_UNI_QUIZ as working directory