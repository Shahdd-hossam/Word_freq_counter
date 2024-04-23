import nltk
#First download stop words from the nltk library
nltk.download('stopwords')

#import stopwords from the corpus and put it into a set
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))

nltk.download('punkt')

#Read the random paragraph text file
file = open("paragraphs.txt", "r+")
content = file.read().lower()

from nltk.tokenize import word_tokenize,sent_tokenize
tokens = word_tokenize(content)

without_stop_words = []
stop_words_count  = 0
for word in tokens :
    if word in stop_words :
        stop_words_count +=1
        continue
    else :
      without_stop_words.append(word)

# Get word frequencies
from collections import Counter
word_freq = Counter(without_stop_words)

# Print word frequencies
for word,freq in word_freq.items():
    print(f"{word}: {freq}")