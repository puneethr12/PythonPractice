# reading local files

#f= open('C:\\Users\\training_b4b.01.20\\AppData\\Local\\Programs\\Python\\Python37-32\\Data.txt')

#raw=f.read()

#print(raw)


# accesing file from url

#import urllib.request as ur

#url="http://www.gutenberg.org/files/2554/2554-0.txt"

#response = ur.urlopen(url) # response obj will hold data from url

#raw = response.read().decode('utf8')

#print(raw)

#print(type(raw))
#print(len(raw))
#------------------------------------------------------------------------------
# POS

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

text = word_tokenize("And no something completely different")

#print(nltk.pos_tag(text))

#text1 = word_tokenize("They refuse to permit us to obtain the refuse permit")

text1 = word_tokenize("Albert Einstein was born in Ulm, Germany in 1879")

print(nltk.pos_tag(text1))




