# rag_utils.py

from transformers import RagTokenizer, RagRetriever, RagTokenForGeneration, BertModel, BertTokenizer
import torch
from datasets import load_dataset

# Function to initialize and return the RAG model
def initialize_rag_model(dataset_path="dataset", index_path="index"):
    # Initialize the tokenizer and retriever
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
    retriever = RagRetriever.from_pretrained("facebook/rag-token-nq", 
                                             index_name="custom",
                                             dataset_path=dataset_path,
                                             index_path=index_path)
    
    # Initialize and return the RAG model
    return RagTokenForGeneration.from_pretrained("facebook/rag-token-nq", retriever=retriever), tokenizer

# Function to create embeddings
def create_embeddings(texts):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained('bert-base-uncased')

    embeddings = []
    for text in texts:
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        embeddings.append(outputs.last_hidden_state.mean(dim=1).squeeze().numpy())

    return embeddings
