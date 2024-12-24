import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.getbrowser import setup_chrome
from CloudflareBypasser import CloudflareBypasser

# Your code here
from datetime import datetime
from bs4 import BeautifulSoup
browser=setup_chrome()
def download_image(url):

    urllist = []

    tab=browser.new_tab()
    tab.get(url)

    cf_bypasser = CloudflareBypasser(tab)
    cf_bypasser.bypass()


    images=tab.ele('#pageScroll').eles('tag:a')
    for i in images:
        src=i.attr('style').split('url(&quot;)')[-1].split('&quot')[0]

        filename=src.split('/')[-1].split('?')[0]
        filepath="themes/appleblog/public/assets/"+filename + ".png"
        res = tab.download(url, filepath)

def preparedefaultimage():
    url = 'https://www.midjourney.com/showcase/recents'
    url2 = 'https://www.midjourney.com/showcase/top'

    filenames=download_image(url)
    return filenames
