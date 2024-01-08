import json
import os

def transcript_to_json(transcript):
    lines = transcript.strip().split("\n")
    pairs = []

    for i in range(0, len(lines), 3):  # Step by 2 to create pairs
        prompt = lines[i].strip()
        if i+3 > len(lines):
            response = "END"
        else:
            response = lines[i + 3].strip()
        if prompt and response:  # Ensure both prompt and response are non-empty
            pairs.append({"prompt": prompt, "completion": response})

    return pairs

def write_json_file(data, file_name):
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)

# Sample data
files = os.listdir()
print(files)
for file in files:
    if file.endswith(".txt"):
        f = open(file)
        name = file.replace(".txt", ".json")
        transcript = "".join(f.readlines())
        # Convert and write to JSON file
        json_data = transcript_to_json(transcript)
        write_json_file(json_data, name)

print("JSON file created successfully.")
