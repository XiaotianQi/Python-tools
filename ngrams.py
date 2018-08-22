# _*_coding:utf-8_*_

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict

def cleanInput(input):
    input = re.sub(r'\n+', ' ', input)
    input = re.sub(r'\s+', ' ', input)
    input = re.sub(r'\[[0-9]*\]', ' ', input)
    input = bytes(input, 'utf-8')
    input = input.decode('ascii', 'ignore')
    input = input.split(' ')
    cleanInput = []
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def ngrams(input, n):
    input = cleanInput(input)
    output = dict()
    for i in range(len(input)+1-n):
        newNGram = ' '.join(input[i:i+n])
        if newNGram in output:
            output[newNGram] += 1
        else:
            output[newNGram] = 1
    return output

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html, 'lxml')
content = bsObj.find('div', {'id':'mw-content-text'}).get_text()
ngrams = ngrams(content, 2)
ngrams = dict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
print(ngrams)
