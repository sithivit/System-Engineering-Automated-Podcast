import os
import json
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file.
    """
    try:
        return extract_text(pdf_path)
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

def create_jsonl_from_pdf_folder(folder_path, output_jsonl_path):
    documents = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            text = extract_text_from_pdf(file_path)
            
            if text:
                document = {
                    "id": filename,
                    "text": text
                }
                documents.append(document)

    with open(output_jsonl_path, 'w', encoding='utf-8') as output_file:
        for doc in documents:
            json_line = json.dumps(doc)
            output_file.write(json_line + '\n')

# Usage
folder_path = 'documents'
output_jsonl_path = 'database.jsonl'
create_jsonl_from_pdf_folder(folder_path, output_jsonl_path)
