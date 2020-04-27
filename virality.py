file  = open("headlines.txt",'r')
headlines = file.readlines()
words = []
for line in headlines:
    line =line.replace(',','')
    line = line.replace('\'','')
    line = line.replace(':','')
    words.append(line.strip().split(sep=' '))
print ("No. of headlines are "+str(len(headlines)))

count = sum( [ len(line) for line in words])
print ("No. of words are "+str(count))
import nltk
# nltk.download('punkt')
nouns=[]
is_noun = lambda pos: pos[:2] == 'NN'
for line in headlines:
    line =line.replace(',','')
    line = line.replace('\'','')
    line = line.replace(':','')
    tokenized = nltk.word_tokenize(line)
    new_nouns = [word for (word,pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    nouns.append(new_nouns)
count1 = sum( [ len(line) for line in nouns])
print("No. of nouns out of them are "+str(count1))

data={}

for line in nouns:
    for word in line:
        if word in data:
            data[word]+=1
        else:
            data[word]=1


print ("Important of words are")

import math
# Create a list of tuples sorted by index 1 i.e. value field     
listofTuples = sorted(data.items() , reverse=True, key=lambda x: x[1])
# Iterate over the sorted sequence
for elem in listofTuples[:50] :
    print(elem[0] , " ::" , elem[1] )


file = open ("news_headline.txt",'r')
test_headline = file.readline()
test_headline =test_headline.replace(',','')
test_headline = test_headline.replace('\'','')
test_headline = test_headline.replace(':','')
tokenized = nltk.word_tokenize(test_headline)
test_nouns = [word for (word,pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
test_nouns_prob = []

for item in test_nouns:
    test_nouns_prob.append((data[item]-1)/listofTuples[0][1])
import statistics 
final_score = statistics.mean(test_nouns_prob) + statistics.stdev(test_nouns_prob)
print(test_nouns)
print(test_nouns_prob)
print("This is your final probability of news '"+test_headline+"' getting viral :: "+str(final_score))