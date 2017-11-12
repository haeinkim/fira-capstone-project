import os
import re
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
from concurrent import futures


def fetch_path(url, path):
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')
    file_names = []

    for tag in soup.findAll("a", href=re.compile('\d+.(mat)')):
        if 'href' in tag.attrs:
            file_name = tag['href']
            file_names.append(file_name)

    file_urls = [url + file_name for file_name in file_names]
    file_dirs = [path + file_name for file_name in file_names]

    return file_urls, file_dirs


def get_file(base_url, base_dir):
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)

    file_urls, file_dirs = fetch_path(base_url, base_dir)

    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map((lambda src, dst: urlretrieve(src, dst)), file_urls,
                     file_dirs)
