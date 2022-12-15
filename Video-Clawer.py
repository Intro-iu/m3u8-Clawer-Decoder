import requests
import re
import os

def askURL(url):
  header = {}
  return requests.get(url, header = header).content
