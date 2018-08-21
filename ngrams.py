# _*_coding:utf-8_*_

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

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
    output = []
    for i in range(len(input)+1-n):
        output.append(input[i:i+n])
    return output

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html, 'lxml')
content = bsObj.find('div', {'id':'mw-content-text'}).get_text()
ngrams = ngrams(content, 2)
print(ngrams)
print('2-grams count is: ', str(len(ngrams)))
