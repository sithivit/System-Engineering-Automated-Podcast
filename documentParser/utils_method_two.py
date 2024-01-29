from transformers import RagTokenizer, RagRetriever, RagTokenForGeneration

tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
retriever = RagRetriever.from_pretrained("facebook/rag-token-nq", index_name="custom", passages_path="database.jsonl")
model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq", retriever=retriever)

def query_transformers(query):
    input_ids = tokenizer(query, return_tensors="pt").input_ids
    generated_ids = model.generate(input_ids)
    generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    return generated_text

query_transformers("Do modern LLMs have beliefs, desires, and intentions?")