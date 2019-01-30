# -*- coding:UTF-8 -*-
import requests
import urllib
from bs4 import BeautifulSoup

if __name__ == '__main__':

    def download(url, file_name):
        # open in binary mode
        with open(file_name, "wb") as file:
            # get request
            response = requests.get(url)
            # write to file
            file.write(response.content)

    target = 'https://github.com/QSCTech/zju-icicles/tree/master/%E8%AE%A1%E7%AE%97%E7%90%86%E8%AE%BA/%E8%AF%95%E5%8D%B7'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('a', class_='js-navigation-open')
    urls = []
    for link in texts:
        download_url = link.get('href')
        if download_url != '':
            download_url = 'https://github.com' + download_url.replace('blob', 'raw')
            file_name = urllib.parse.unquote(download_url.split("/")[-1])
            download(download_url, file_name)
            print('one file done')
            urls.append(download_url)
