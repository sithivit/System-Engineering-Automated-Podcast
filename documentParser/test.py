from transformers import RagRetriever, RagTokenForGeneration, DPRQuestionEncoder, DPRQuestionEncoderTokenizer
from datasets import load_dataset

# Load the dataset and the FAISS index
dataset = load_dataset('Locutusque/hercules-v1.0') # Adjust as needed

# Initialize RAG Retriever with FAISS index
retriever = RagRetriever.from_pretrained("facebook/rag-token-nq", index_dataset=dataset)

# Initialize RAG Model
model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq", retriever=retriever)

# Initialize DPR Question Encoder and Tokenizer for querying
q_encoder = DPRQuestionEncoder.from_pretrained("facebook/dpr-question_encoder-single-nq-base")
q_tokenizer = DPRQuestionEncoderTokenizer.from_pretrained("facebook/dpr-question_encoder-single-nq-base")

def query_transformers(question):
    # Encode the question and retrieve embeddings
    question_embedding = q_encoder(**q_tokenizer(question, return_tensors="pt")).pooler_output
    scores, retrieved_examples = dataset.get_nearest_examples('embeddings', question_embedding, k=5)

    # Generate an answer using RAG
    input_ids = retrieved_examples['input_ids']
    generated_ids = model.generate(input_ids)
    generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)

    return generated_text

# Example query
print(query_transformers("Your query here"))

# Example Usage
query = "Do you think LLm is more of a library or librarian?"
print(query_transformers(query))
