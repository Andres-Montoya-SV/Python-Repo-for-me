from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings

warnings.filterwarnings('ignore')

nltk.download('punkt', quiet=True)

article = Article('https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521')
article.download()
article.parse()
article.nlp()
corpus = article.text
##print(corpus)

text = corpus
sentence_list = nltk.sent_tokenize(text)
##print(sentence_list)

def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))
    
    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
        return list_index
                

def greeting(text):
    text = text.lower()
    bot_greeting = ['Hi', 'Hola', 'Hello', 'Hi there', 'Welcome', 'Hello there', 'Howdy', 'Hi (: ']
    user_greeting = [bot_greeting, 'Hi', 'hi', 'hola', 'H0la', 'Holi', 'Holo']
    
    for word in text.split():
        if word in user_greeting:
            return random.choice(bot_greeting)
        

def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0
    
    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response+ ' ' +sentence_list[index[i]]
            response_flag = 1
            j = j + 1
        if j > 2:
            break
    if response_flag == 0:
        bot_response = bot_response+ ' ' + "I apologize, i don't undestand you"
    sentence_list.remove(user_input)
    
    return bot_response

print('Nathalia: I am Doctor Bot or Doc Bot for short. I will answer your queries about Chronic Kidney diseas. I f you would like to exit please type "bye"')

exit_list = ['Exit', 'Bye', 'see you later', 'c ya', 'see ya', 'bye', 'Goodbye', 'goodbye', 'good bye', 'Quit', 'quit', 'exit']

while True:
    user_input = input()
    if user_input.lower() in exit_list:
        print('Nathalia: Chat with you later')
        break
    else:
        if greeting(user_input) != None:
            print('Nathalia: ' +greeting(user_input))
        else:
            print('Nathalia: ' + bot_response(user_input))