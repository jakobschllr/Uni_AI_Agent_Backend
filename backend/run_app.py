from typing import Union
from ingest.chunk_generator import get_chunks
from backend.ingest.DataExtractor import DataExtractor
from backend.retrieval.DatabaseHandler import DatabaseHandler
from nlp.remove_stopwords import remove_stopwords
from llm.Chat import Chat
import os


PDF_PATH = "/Users/jakobschiller/Desktop/Projekte/AI_Uni_Quiz/file_handling/Skript_Lineare_Algebra.pdf"
db_handler = DatabaseHandler()
extractor = DataExtractor()


def create_collection(path, collection_id, language):
    pdf_data = extractor.get_pdf_data(path=path)
    cleaned_data = extractor.clean_data(pdf_data)
    sentences, chunks = get_chunks(cleaned_data, language)
    collection = db_handler.create_collection(collection_id)
    db_handler.add_to_collection(collection, chunks)


def query_existing_db(collection_id, query):
    collection = db_handler.get_collection(collection_id)
    if collection != None:
        return collection.query(
            query_texts=query,
            n_results=5
            )['documents']
    else:
        return None

def get_db_response(collection_id, raw_user_input):
    cleaned_user_input = extractor.clean_data(raw_user_input)
    without_stopwords = remove_stopwords(cleaned_user_input)
    results = query_existing_db(collection_id, cleaned_user_input)
    return results


def create_session(session_title):
    create_collection()

    # each session (chat) has it's collection
    # the session name is saved together with the collection_id in an sql database
    pass




user_request = "Was ist ein Vektor?"

db_response = get_db_response("0", "0", user_request)
chat = Chat(0)
answer = chat.generate_answer(user_request, db_response)

print(answer)

# run file with python -m api.index from AI_UNI_QUIZ as working directory