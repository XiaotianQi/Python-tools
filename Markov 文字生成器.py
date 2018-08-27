# _*_coding:utf-8_*_

from urllib.request import urlopen
from random import randint
import re

def buildWordDict(text):
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\"', '', text)

    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, ' '+symbol+' ')
    
    words = text.split(' ')
    words = [word for word in words if word !='']

    wordDict = {}
    for i in range(len(words)-1):
        if words[i] not in wordDict:
            wordDict[words[i]] = {}
        if words[i+1] not in wordDict[words[i]]:
            wordDict[words[i]][words[i+1]] = 0
        wordDict[words[i]][words[i+1]] += 1
    
    return wordDict

def wordListSum(wordList):
    sum = 0
    for value in wordList.values():
        sum += value
    return sum

def retrieveRandomWord(wordList):
    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word

with open(r'C:\Users\bnwse\Desktop\inaugurationSpeech.txt') as f:
    text = f.read()
    wordDict = buildWordDict(text)

    length = 100
    chain = ""
    currentWord = "I"
    for i in range(0, length):
        chain += currentWord+" "
        currentWord = retrieveRandomWord(wordDict[currentWord])

    print(chain)