# -*- coding:UTF-8 -*-
import requests
import urllib
from bs4 import BeautifulSoup

if __name__ == '__main__':

    def download(url, file_name):
        with open(file_name, "wb") as file:
            response = requests.get(url)
            file.write(response.content)

    target = ''
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('a', class_='js-navigation-open')
    urls = []
    count = 0
    for link in texts:
        download_url = link.get('href')
        if download_url != '':
            download_url = 'https://github.com' + download_url.replace('blob', 'raw')
            file_name = urllib.parse.unquote(download_url.split("/")[-1])
            download(download_url, file_name)
            count += 1
            print(count + 'files done')
            urls.append(download_url)
