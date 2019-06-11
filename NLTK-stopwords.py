import NLTK as NL
import seaborn as sb

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

example1=""" Hello Mr. Modi, how are you feeling now?
            The Results are yet to be unvieled. So, hold on let's celebrate tomorrow. You should be the king
            """
stop_words = set (stopwords.words('english'))

word_tokens1=word_tokenize(example1)

filter_sentence = [w for w in word_tokens1 if w not in stop_words]

#filter_sentence=[]


for w in word_tokens1:
    if w in stop_words:
        filter_sentence.append(w)

print(word_tokens1)
print(filter_sentence)

