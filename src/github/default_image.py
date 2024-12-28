import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.getbrowser import setup_chrome
from utils.CloudflareBypasser import CloudflareBypasser

# Your code here
from datetime import datetime
from bs4 import BeautifulSoup
browser=setup_chrome()
urls = [
    "https://ideogram.ai/assets/progressive-image/balanced/response/0FOj5KMmQqMOXWjLStMJYA",
    "https://ideogram.ai/assets/progressive-image/balanced/response/1X9YVLORQzKM-WoLSMNLkA",
    "https://ideogram.ai/assets/progressive-image/balanced/response/2XRUWVKMJTKMmWLoRSMNKIA",
    "https://ideogram.ai/assets/progressive-image/balanced/response/3FOJUVOITLMO9WrSMtM5w",
    "https://ideogram.ai/assets/progressive-image/balanced/response/4YIXWVKLTyJMXLpLSMtL5A",
    "https://ideogram.ai/assets/progressive-image/balanced/response/5YRUV7KMRLKM-WmLStNJw",
    "https://ideogram.ai/assets/progressive-image/balanced/response/6FJUVOITzKJMXWpLStN5Q",
    "https://ideogram.ai/assets/progressive-image/balanced/response/7ZOIWVOJTLKM-WjRSNNMw",
    "https://ideogram.ai/assets/progressive-image/balanced/response/8F5JVVKOTRLMWNoLSMtCMA",
    "https://ideogram.ai/assets/progressive-image/balanced/response/9XOUWVKMJTLMO9WpRSMCLg",
    "https://ideogram.ai/assets/progressive-image/balanced/response/Z7D9OE2RRZ4MoLfEN9SVhA",
    "https://ideogram.ai/assets/progressive-image/balanced/response/aXFSKgSpQ3WJgCJuULulXA",
    "https://ideogram.ai/assets/progressive-image/balanced/response/bZSh8OEITni49iIoSMT8xQ",
    "https://ideogram.ai/assets/progressive-image/balanced/response/cSLO8vVpQjaUM4jRXJ8Z5g",
    "https://ideogram.ai/assets/progressive-image/balanced/response/d7F5WtZJTS-zRwBYkRtjUw",
    "https://ideogram.ai/assets/progressive-image/balanced/response/e9Mh2KM6QWL8MojoUrX68w",
    "https://ideogram.ai/assets/progressive-image/balanced/response/fZgJ0vYCRKLfXMmSjLvCHg",
    "https://ideogram.ai/assets/progressive-image/balanced/response/g6IXWBvITsyAjJIoVJuBsw",
    "https://ideogram.ai/assets/progressive-image/balanced/response/hZRLK7DBQyJ6fAmLMt3MBw",
    "https://ideogram.ai/assets/progressive-image/balanced/response/jY8LV0KMTRU8WMuUMtN5IA",
    "https://ideogram.ai/assets/progressive-image/balanced/response/kX9LVYOQTJKM2AmJSNsGhQ",
    "https://ideogram.ai/assets/progressive-image/balanced/response/mZ4YVOKBQ-RjWLoRMtMLXA",
    "https://ideogram.ai/assets/progressive-image/balanced/response/nX5UVLM4QjL9gMmLStt5sw",
    "https://ideogram.ai/assets/progressive-image/balanced/response/o9RYWBvJQaL8XRoLStjGzA",
    "https://ideogram.ai/assets/progressive-image/balanced/response/p9YLV0JQT-RLMKoSMvMLhQ",
    "https://ideogram.ai/assets/progressive-image/balanced/response/qX4UV7KJQyJLMumSMNuA6w",
    "https://ideogram.ai/assets/progressive-image/balanced/response/r6ZUWVL5TSKJWMjoUSMuChg",
    "https://ideogram.ai/assets/progressive-image/balanced/response/s9IXWOKRTyJLjKmMSMtC5w",
    "https://ideogram.ai/assets/progressive-image/balanced/response/tY5LV7OJQa9LMouSMtNLMA",
    "https://ideogram.ai/assets/progressive-image/balanced/response/uX9UVWOKTSyLWMmRSNtE6w",
    "https://ideogram.ai/assets/progressive-image/balanced/response/v6IXWVL9QaJLjMoLStjN5w",
    "https://ideogram.ai/assets/progressive-image/balanced/response/wY9LV0OJQJLMKMjSMvMLjw",
    "https://ideogram.ai/assets/progressive-image/balanced/response/xZ4UV7KRT-LjMmLSttN8IA",
    "https://ideogram.ai/assets/progressive-image/balanced/response/y9RYWVLJQaLXMKoUSMtN6A",
    "https://ideogram.ai/assets/progressive-image/balanced/response/zY5LVOM5TSyLMjmUSNMLCQ"
]

def download_image(urls):

    resulturllist = []
    for url in urls:

        tab=browser.new_tab()
        tab.get(url)

        cf_bypasser = CloudflareBypasser(tab)
        cf_bypasser.bypass()

        project_root = os.path.abspath(os.path.dirname(__file__))
        relative_path="../../themes/appleblog/public/assets/"
        directory = os.path.join(project_root, relative_path)
        filename =url.split('/')[-1]        + ".png"
        if '.' in url:
            filename =url.split('/')[-1]

        filepath = os.path.join(directory, filename)        
        res = tab.download(url, filepath)

def preparedefaultimage():

    filenames=download_image(urls)
    return filenames
