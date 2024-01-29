import pinecone
import os
from sklearn.feature_extraction.text import TfidfVectorizer

class DocumentVectorizer:
    def __init__(self, pinecone_index):
        self.vectorizer = TfidfVectorizer()
        self.index = pinecone_index

    def vectorize_and_upload(self, document_id, text):
        """
        Vectorize a document and upload it to Pinecone.
        """
        vector = self.vectorizer.fit_transform([text]).toarray()[0]
        self.index.upsert(vectors={(document_id, vector)})
        return vector

def initialize_pinecone(api_key, environment='us-west1-gcp'):
    """
    Initialize Pinecone environment.
    """
    pinecone.init(api_key=api_key, environment=environment)

def create_vector_index(index_name, dimension):
    """
    Create a new vector index.
    """
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(index_name, dimension=dimension)
    return pinecone.Index(index_name)

def query_pinecone(index, query_vector, top_k=5):
    """
    Query Pinecone for the most similar vectors.
    """
    response = index.query(queries=[query_vector], top_k=top_k)
    return response['matches']

def query_pinecone_for_content(query_text, top_k=5):
    """
    Query Pinecone and generate podcast content based on the results.
    """
    query_vector = dv.vectorizer.transform([query_text]).toarray()[0]
    response = index.query(queries=[query_vector], top_k=top_k)
    matches = response['matches']

    # Combine the texts from top matches for LLM input
    combined_text = ' '.join([match['metadata']['text'] for match in matches])
    return combined_text