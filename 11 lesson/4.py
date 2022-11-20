import urllib.request
import time
from threading import Thread

urls = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    'https://isocpp.org',
]


def read_url(url):
    with urllib.request.urlopen(url) as u:
        return u.read()


start = time.time()
threads = [
    Thread(target = read_url, args =(url,))
    for url in urls
    ]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(time.time() - start)
#output:
#this program : 1.1983916759490967
#previous program: 2.0126349925994873