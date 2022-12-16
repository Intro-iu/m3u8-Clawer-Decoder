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

def readFile(filePath = ''):
    with open(filePath, 'r') as f:
        urlString = f.readlines()
    urlList = [string.strip('\n') for string in urlString if 'https' in string]
    return urlList

def VideoClawer(urlList, filename):
    with open('./'+filename+'.mp4', mode = 'ab') as f:
        for i in tqdm(range(len(urlList)), desc=filename):
            videoContent = askURL(urlList[i]).content
            f.write(videoContent)
    
def save(m3u8filename):
    filecontent = []
    content = readFile(filePath = './'+m3u8filename)
    VideoClawer(content, m3u8filename[:-5])


if __name__ == '__main__':
    filenum = 0
    m3u8filename = []
    for filename in os.listdir('./'):
        if filename[-5:] == '.m3u8':
            filenum = filenum + 1
            m3u8filename.append(filename)
    pool = Pool(filenum)
    pool.map(save, m3u8filename)

    
