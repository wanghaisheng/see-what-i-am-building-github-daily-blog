import os
import requests
import xmltodict
from google.oauth2 import service_account
from googleapiclient.discovery import build

# URL and local path for the sitemap
SITEMAP_URL = os.getenv('SITEMAP_URL')
LOCAL_SITEMAP_PATH = os.getenv('LOCAL_SITEMAP_PATH')

# Load Google credentials from environment variable
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

def read_sitemap(url=None, path=None):
    if url:
        response = requests.get(url)
        return xmltodict.parse(response.content)
    elif path:
        with open(path, 'r') as file:
            return xmltodict.parse(file.read())
    else:
        raise ValueError("Either a URL or a local path must be provided")

# Read the sitemap
sitemap = read_sitemap(url=SITEMAP_URL, path=LOCAL_SITEMAP_PATH)

# Extract URLs from the sitemap
urls = [url['loc'] for url in sitemap['urlset']['url']]

# Set up Google Indexing API
SCOPES = ["https://www.googleapis.com/auth/indexing"]
credentials = service_account.Credentials.from_service_account_file(
    GOOGLE_APPLICATION_CREDENTIALS, scopes=SCOPES)
service = build('indexing', 'v3', credentials=credentials)

# Function to send a URL to the Indexing API
def index_url(url):
    try:
        body = {
            "url": url,
            "type": "URL_UPDATED"
        }
        service.urlNotifications().publish(body=body).execute()
        print(f"Indexed: {url}")
    except Exception as e:
        print(f"Failed to index {url}: {str(e)}")

# Index each URL
for url in urls:
    index_url(url)
