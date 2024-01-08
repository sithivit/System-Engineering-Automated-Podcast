import json
import os

def solo_transcript_to_json(transcript):
    sections = transcript.strip().split("\n\n\n\n")  # Split by double line breaks for paragraphs
    entries = []

    for section in sections:
        section_text = section.strip()
        if section_text:  # Ensure the section is non-empty
            entries.append({"text": section_text})

    return entries

def write_json_file(data, file_name):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)

# Sample data
files = os.listdir()
for file in files:
    if file.endswith(".txt"):
        with open(file, 'r', encoding='utf-8') as f:
            transcript = "".join(f.readlines())
            name = file.replace(".txt", ".json")
            # Convert and write to JSON file

            json_data = solo_transcript_to_json(transcript)
            write_json_file(json_data, name)

print("JSON file created successfully.")