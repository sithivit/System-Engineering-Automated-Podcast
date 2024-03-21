import warnings
warnings.filterwarnings("ignore")
import re

from langchain.document_loaders import HuggingFaceDatasetLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from transformers import AutoTokenizer, pipeline
from langchain import HuggingFacePipeline
from langchain.chains import RetrievalQA
import pdfplumber
import os

class Document:
    def __init__(self, text, metadata=None):
        self.page_content = text
        self.metadata = metadata if metadata is not None else {}

MODELPATH = "sentence-transformers/all-MiniLM-l6-v2"
MODEL_KWARGS = {'device':'cpu'}
ENCODE_KWARGS = {'normalize_embeddings': False}

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text(x_tolerance=2, y_tolerance=2) + " " # concatenate text from all pages
    return text

def extract_text_from_txt(txt_path):
    """Extract text from a TXT file."""
    with open(txt_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def load_HuggingfaceDataset(dataset_name, page_content_column):
    loader = HuggingFaceDatasetLoader(dataset_name, page_content_column)

    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    docs = text_splitter.split_documents(data)
    return docs

def create_embedding():
    embeddings = HuggingFaceEmbeddings(
        model_name=MODELPATH,     # Provide the pre-trained model's path
        model_kwargs=MODEL_KWARGS, # Pass the model configuration options
        encode_kwargs=ENCODE_KWARGS # Pass the encoding options
    )
    return embeddings

#Embedding
def save_doc_db(dataset_name="documents", page_content_column="context"):
    embeddings = create_embedding()
    if dataset_name == "documents":
        docs = []
        for filename in os.listdir(os.path.join(os.getcwd(),"scripts","scriptAudioGen","documentParser",dataset_name)):
            if filename.endswith('.pdf'):
                text = extract_text_from_pdf(os.path.join(os.getcwd(),"scripts","scriptAudioGen","documentParser",dataset_name, filename))
                docs.append(text)
            elif filename.endswith('.txt'):
                text = extract_text_from_txt(os.path.join(os.getcwd(),"scripts","scriptAudioGen","documentParser",dataset_name, filename))
                docs.append(text)
        formatted_docs = [Document(text) for text in docs]
        db = FAISS.from_documents(formatted_docs, embeddings) 
        return db
    else:
        #databricks/databricks-dolly-15k
        docs = load_HuggingfaceDataset(dataset_name, page_content_column)
        db = FAISS.from_documents(docs, embeddings)
        return db

def extract_text_by_keywords(text, topics, subtopics):
    
    extracted_text = []
    
    keywords = topics + subtopics
    
    sections = text.split('.')
    
    for section in sections:
        if any(keyword.lower() in section.lower() for keyword in keywords):
            extracted_text.append(section)
            
    return '\n'.join(extracted_text)

def similarity_search(input):
    db = save_doc_db()
    searchDocs = db.similarity_search(input)
    return searchDocs[0].page_content


