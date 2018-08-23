# _*_coding:utf-8_*_

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator

# 清晰文本
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

# 常用语料库
def isCommon(ngram):
    commonWords = [
        "the", "be", "and", "of", "a", "in", "to", "have", "it", "i",
        "that", "for", "you", "he", "with", "on", "do", "say", "this", "they",
        "is", "an", "at", "but", "we", "his", "from", "that", "not", "by",
        "she", "or", "as", "what", "go", "their", "can", "who", "get", "if",
        "would", "her", "all", "my", "make", "about", "know", "will", "as", "up",
        "one", "time", "has", "been", "there", "year", "so", "think", "when", "which",
        "them", "some", "me", "people", "take", "out", "into", "just", "see", "him",
        "your", "come", "could", "now", "than", "like", "other", "how", "then", "its",
        "our", "two", "more", "these", "want", "way", "look", "first", "also", "new",
        "because", "day", "more", "use", "no", "man", "find", "here", "thing", "give",
    ]
    for word in ngram.split():
        if word in commonWords:
            return True
    return False

# n-gram 模型
def ngrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)+1-n):
        newNGram = ' '.join(input[i:i+n])
        if isCommon(newNGram):
            continue
        if newNGram not in output: 
            output[newNGram] = 0
        output[newNGram] += 1
    return output

# 获取 n-gram 语词所在语句
def getFirstSentenceContaining(ngram, content):
    sentences = content.split(".")
    for sentence in sentences: 
        if ngram in sentence:
            return sentence
    return ""

content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
ngrams = ngrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
# print(sortedNGrams)

# 出现频率大于2的语词 及其 所在语句
topWords=[]
for i in range(len(sortedNGrams)):
    if sortedNGrams[i][1] > 2:
        topWords.append(sortedNGrams[i][0])
print(topWords)

sentences = set()
for word in topWords:
    sentences.add(getFirstSentenceContaining(word, content))
for i in list(sentences):
    print(i)
