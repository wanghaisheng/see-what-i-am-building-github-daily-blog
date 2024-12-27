import requests, json, os
from datetime import datetime
from bs4 import BeautifulSoup

def get_image_urls(url):

    urllist = []
    try:
        headers = {'User-Agent': 'curl/7.84.0'}
        page = requests.get(url, headers=headers, allow_redirects=True)
        soup = BeautifulSoup(page.content, 'html.parser')
        body = soup.find("body")
        sc = list(body.find_all("script"))[-1].string
        sc = str(sc)
        print(soup)
        script = soup.find('script', {'id': '__NEXT_DATA__'})
        sc = script.contents[0]    
        print(sc)
    # parse JSON
        sc = json.loads(sc).get("props").get("pageProps").get("jobs")
        for i in sc:
            urllist.append(i.get("event").get("seedImageURL"))
    except Exception as e:
        print('get url error',e)
    return urllist

def download_image(urllist):
    curdate = datetime.now().strftime("%Y%m%d")
    os.makedirs(curdate, exist_ok=True)
    os.chdir(curdate)

    headers = {'User-Agent': 'curl/7.84.0'}
    i = 1
    filenames=[]
    for url in urllist:
        page = requests.get(url, headers=headers, allow_redirects=True)
        with open("themes/appleblog/public/assets/"+str(i) + ".png", 'wb') as f:
            f.write(page.content)
        i+=1
        print(f"Downloaded {i}.png")
        filenames.append(i+'.png')
    return filenames
def preparedefaultimage():
    url = 'https://www.midjourney.com/showcase/recents'
    url2 = 'https://www.midjourney.com/showcase/top'
    urllist1 = get_image_urls(url)
    urllist2 = get_image_urls(url2)
    unique = set()
    for i in urllist1:
        unique.add(i)
    for i in urllist2:
        unique.add(i)
    if len(list(unique))==0:
        unique=urls = [
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

        
    filenames=download_image(unique)
    return filenames
