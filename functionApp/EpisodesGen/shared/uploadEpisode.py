from azure.storage.blob import BlobServiceClient
from pymongo import MongoClient
import dotenv
import os

def run(episode_title, description):
    dotenv.load_dotenv()
    uploadBlob(episode_title)
    uploadCosmos(episode_title, description)

def uploadBlob(episode_title):
    CONNECTION_STR = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    service_client = BlobServiceClient.from_connection_string(CONNECTION_STR)
    container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")

    local_file_name = str(episode_title) + ".mp4"
    upload_file_path = os.path.join("tmp", "output_video.mp4")

    # Create a blob client using the episode title as the name for the blob
    blob_client = service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the video
    with open(file=upload_file_path, mode="rb") as data:
        blob_client.upload_blob(data, connection_timeout=600)

def uploadCosmos(title, description):
    CONNECTION_STR = os.getenv("COSMOS_CONNECTION_STRING")
    DB_NAME = os.getenv("COSMOSDB_DBNAME")
    COLLECTION_NAME = os.getenv("COSMOSDB_COLLECTION")
    container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")

    client = MongoClient(CONNECTION_STR)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    media = "https://aipodcaststorage.blob.core.windows.net/" + container_name + "/" + title + ".mp4"

    episode = {
        "title": title,
        "description": description,
        "media": media,
    }

    collection.insert_one(episode)
    
if __name__ == "__main__":
    run("test_title", "test_desc")