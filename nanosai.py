# import libraries
from bs4 import BeautifulSoup
import requests
import nltk
from nltk.corpus import stopwords
import re
import string
import spacy
import os
import numpy

# url = "https://nanos.ai/"
# Make a GET request to fetch the raw HTML content
# page1 = requests.get(url).text

# Data already scraped
# with open("nanos_web.txt",'w',encoding = 'utf-8') as f: # write html to a file
#     f.write(page1)
#     f.close()


f = open("nanos_web.txt", 'r', encoding='utf-8')  # Read a file
page2 = f.read()
f.close()

# nltk.download('stopwords')                      # download stopwords from nltk
nlp = spacy.load("en_core_web_lg")  # trained pipelines for English


def clean_html(page):
    # Parse the html content
    soup = BeautifulSoup(page, 'lxml')
    web_text = soup.get_text()  # print the parsed data of html
    return web_text


def str_to_list(text):
    pre = [text]
    return pre


def decontracted(phrase):
    # specific
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase


def clean_text(text):
    stop_words = set(stopwords.words('english'))
    preprocessed_text = []
    # tqdm is for printing the status bar
    for sentence in text:
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))  # remove punctuations
        sentence = re.sub(r"http\S+", "", sentence)
        sentence = BeautifulSoup(sentence, 'lxml').get_text()
        sentence = decontracted(sentence)
        sentence = re.sub("\S*\d\S*", "", sentence).strip()  # remove words with numbers
        sentence = re.sub('[^A-Za-z]+', ' ', sentence)  # remove special character
        sentence = ' '.join(e.lower() for e in sentence.split() if e.lower() not in stop_words)  # remove stopwords
        preprocessed_text.append(sentence.strip())
    return preprocessed_text


def list_to_str(text):
    str1 = " "
    for ele in text[0]:
        str1 += ele
    return str1


def spacy_most_similar(word):
    ms = nlp.vocab.vectors.most_similar(nlp(word).vector.reshape(1, nlp(word).vector.shape[0]), n=40)
    words = [nlp.vocab.strings[w] for w in ms[0][0]]
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
    word = input("Enter Product/Services/Keyword : ").lower()
    print("Important keywords: {}".format(spacy_most_similar(word)))


main()
