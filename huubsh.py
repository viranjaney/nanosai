#import libraries
from bs4 import BeautifulSoup
import requests
import nltk
from nltk.corpus import stopwords
import re
import string
import spacy
import os
import numpy as np

# url = "https://huubsh.com/l/gibson-slash-les-paul-standard-november--3569"
# Make a GET request to fetch the raw HTML content
# page1 = requests.get(url).text

#Data already scraped
# with open("nanos_web.txt",'w',encoding = 'utf-8') as f:   # write html to a file
#     f.write(page1)
#     f.close()


f = open("huubsh_web.txt", 'r', encoding ='utf-8') # Read a file
page2 = f.read()
f.close()

# nltk.download('stopwords')                      # download stopwords from nltk
nlp = spacy.load("de_core_news_lg")               # trained pipelines for German


def clean_html(page):
    # Parse the html content
    soup = BeautifulSoup(page, 'lxml')
    web_text = soup.get_text() # print the parsed data of html
    return web_text

def str_to_list(text):
    pre = []
    pre.append(text)    #append strings to a list
    return pre


def umlauts(text):      # Converting umlauts characters to another form 

    tempVar = text  # local variable

    # Using str.replace()

    tempVar = tempVar.replace('ä', 'ae')
    tempVar = tempVar.replace('ö', 'oe')
    tempVar = tempVar.replace('ü', 'ue')
    tempVar = tempVar.replace('Ä', 'Ae')
    tempVar = tempVar.replace('Ö', 'Oe')
    tempVar = tempVar.replace('Ü', 'Ue')
    tempVar = tempVar.replace('ß', 'ss')

    return tempVar


def clean_text(text):
    stop_words = set(stopwords.words('german'))
    preprocessed_text = []
# tqdm is for printing the status bar
    for sentence in text:
        sentence = sentence.translate(str.maketrans('', '', string.punctuation)) #remove punctuations
        sentence = re.sub(r"http\S+", "", sentence)
        sentence = BeautifulSoup(sentence, 'lxml').get_text()
        sentence = umlauts(sentence)
        sentence = re.sub("\S*\d\S*", "", sentence).strip() #remove words with numbers
        sentence = re.sub('[^a-zA-ZäöüÄÖÜß]+', ' ', sentence) #remove special character
        sentence = ' '.join(e.lower() for e in sentence.split() if e.lower() not in stop_words) #remove stopwords
        preprocessed_text.append(sentence.strip())
    return preprocessed_text

def list_to_str(text):
    str1 = " "
    for ele in text[0]:
        str1 += ele
    return str1

def spacy_most_similar(word):
    ms = nlp.vocab.vectors.most_similar(nlp(word).vector.reshape(1,nlp(word).vector.shape[0]), n=50)
    words = [nlp.vocab.strings[w] for w in ms[0][0]]
    distances = ms[2]
    w2 = []
    for w1 in words:
        if w1.lower() in to_list:
            w2.append(w1.lower())
    return set(w2)

webpage_text = clean_html(page2)
# print(webpage_text)
str1 = str_to_list(webpage_text)
# print(str1)
cleaned_text = clean_text(str1)
# print(cleaned_text)
to_list = list_to_str(cleaned_text)
# print(to_list)

def main():

    word = input("Geben Sie Produkt / Dienstleistung / Schlüsselwort ein : ").lower()
    print("Wichtige Schlüsselwörter: {}".format(spacy_most_similar(word)))

main()




