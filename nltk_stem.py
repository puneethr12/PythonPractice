import NLTK as NL
import seaborn as sb

from nltk.tokenize import sent_tokenize, word_tokenize

from nltk.stem import PorterStemmer

ps=PorterStemmer()

#ex_wrd=["python", "pythoner", "pythoning", "pythonly"]

#for w in ex_wrd:
#    print(ps.stem(w))

#-----------------------------
    
#ex_wrd1=["game", "gaming", "gamed", "games"]


#for x in ex_wrd1:
    #print(ps.stem(x))

#---------------------------------------

exw="gaming, the gamers play games"

exw1=word_tokenize(exw)

for y in exw1:
    print(y + ":" + ps.stem(y)) # to get the i/p word and corresponding stem word
