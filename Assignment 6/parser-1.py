"""
Author: Vitaan
Created on Mon Feb 27 15:33:05 2017

Your script should define the following functions: 

processSentence(sentence,posLex,negLex,tagger):  The parameters of this function are a sentence (a string), a set positive words, a set of negative words, and a POS tagger.  The function should return a list with all the 4-grams in the sentence that have the following structure:                                                   

not <any word> <pos/neg word> <noun>. 

For example: not a good idea

 ---------------------------------------------------------------------------------------------

getTop3(D): The only parameter of this function is a dictionary D.  All the values in the dictionary are integers. The function returns a list of the keys with the 3 largest values in the dictionary.

 

Notes:

Don't change the names or the parameters of any of the functions
Make sure that your script imports all the libraries needed by the two functions
 
"""



import re
import nltk
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize
from nltk import load
from nltk.probability import FreqDist
import codecs


#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=codecs.open(fname,mode='r',encoding='utf8')
    #add every word in the file to the set
    for sentence in lex_conn:
        newLex.add(sentence.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

# return all the terms that belong to a specific POS type
def getPOSterms(terms,POStags,tagger):
	
    tagged_terms=tagger.tag(terms)#do POS tagging on the tokenized sentence

    POSterms={}
    for tag in POStags:POSterms[tag]=set()

    #for each tagged term
    for pair in tagged_terms:
        for tag in POStags: # for each POS tag 
            if pair[1].startswith(tag): POSterms[tag].add(pair[0])

    return POSterms

# updates the frequency of each noun in the sentence
# returns a list of all the 'not <any word>  <pos/neg word>  <noun>' 4grams in the sentence
def processSentence(sentence,posLex,negLex,tagger):

        matchedfgrams=[]

        sentence=re.sub('[^a-zA-Z\d]',' ',sentence)#replace chars that are not letters or numbers with a spac
        sentence=re.sub(' +',' ',sentence).strip()#remove duplicate spaces

        #tokenize the sentence
        terms = nltk.word_tokenize(sentence.lower())

        #identify noun by POStags
        POStags=['NN'] # POS tags of interest
        POSterms=getPOSterms(terms,POStags,tagger)
        nouns=POSterms['NN']

        fourgrams = ngrams(terms,4) #compute 4-grams

        #for each 4gram
        for tg in fourgrams:
                if tg[0] == 'not' and (tg[2] in posLex or tg[2] in negLex) and tg[3] in nouns: 
                        matchedfgrams.append(tg)

        return matchedfgrams


# gts the list with the 3 most frequent keys in a dictionary
def getTop3(D):

        result=[]

        temp = FreqDist(D)

        for pair in temp.most_common(3):
                result.append(pair[0])

        return result


def run(fpath):
        dict={'idea': 30,'thing':70,'vitaan':9,'good':7,'might':88,'end':99}
        posLex=loadLexicon('positive-words.txt')
        negLex=loadLexicon('negative-words.txt')

        #make a new tagger
        _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
        tagger = load(_POS_TAGGER)

        #read the input
        f=open(fpath)
        text=f.read().strip()
        f.close()
        
        #split sentences
        sentences=sent_tokenize(text)
      
        # for each sentence
        for sentence in sentences:
                print(processSentence(sentence,posLex,negLex,tagger))

        freqNouns=getTop3(dict)  
        
        return freqNouns
        


if __name__=='__main__':
        print (run('input.txt'))

                              