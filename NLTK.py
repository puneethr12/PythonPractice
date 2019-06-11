#NLTK

import NLTK as NL
import seaborn as sb

from nltk.tokenize import sent_tokenize, word_tokenize

example=""" Hello Mr. Modi, how are you feeling now?
            The Results are yet to be unvieled. So, hold on let's celebrate tomorrow. You should be the king
            """

#print(sent_tokenize(example))

#print(word_tokenize(example))

#---------------------------------------------------------------------------
# stop words
#---------------------------------

from nltk.corpus import stopwords

#print(set (stopwords.words('english')))


#-----------------------------------------------------------------------------
data= " All work and no play makes jack a dull boy. All work and no play"

#print(word_tokenize(data))

#print(sent_tokenize(data))

phrases=sent_tokenize(data)

print(phrases)
#---------------------------------------------------------------


