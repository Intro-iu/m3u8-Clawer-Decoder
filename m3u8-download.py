import requests
import re
import os
import subprocess
from multiprocessing.dummy import Pool

from tqdm import tqdm

def askURL(url):
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'
    }
    response = requests.get(url = url, headers = head)
    return response

def m3u8Clawer(url, filename):
    with open('./'+filename, mode = 'ab') as f:
        videoContent = askURL(url).content
        f.write(videoContent)

if __name__ == '__main__':
    url = 'https://yun.ssdm.cc/SBDM/'
    name = 'SwordArtOnline'
    filenum = 25
    filelist = []
    urlList = []

    for i in range(1, 26):
        if i < 10:  filelist.append(name + '0' + str(i) + '.m3u8')
        else:   filelist.append(name + str(i) + '.m3u8')
        urlList.append(url + filelist[i-1])

    for i in tqdm(range(filenum)):
        m3u8Clawer(urlList[i], '' + filelist[i])

