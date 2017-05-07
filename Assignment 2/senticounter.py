"""
Author: Vitaan

Write a script called senticounter.py. Define a function run() inside senticounter.py.

The function should:

- Accept as a parameter the path to a text file. The text file has one review per line. 

- Read the list of positive words from the positive-words.txt file.

- Create a dictionary that includes one key for each positive word that appears in the input text file. The dictionary should map each of these positive words to the number of reviews that include it. For example, if the word "great" appears in 5 reviews, then the dictionary should map the key "great" to the value 5. 

- Return the dictionary 

Notes: Ignore case. You can also assume that the input file includes only letters, no punctuation or other special characters.

"""
#function that loads a lexicon of positive words to a set and returns the set
def loadLexicon(fname):
    newLex=set()
    lex_conn=open(fname,mode='r',encoding='utf8') #to run it on mac
    #add every word in the file to the set
    for line in lex_conn:
        newLex.add(line.strip())# remember to strip to remove the lin-change character
    lex_conn.close()

    return newLex

#function that reads in a file with reviews and decides if each review is positive or negative
#The function returns a list of the input reviews and a list of the respective decisions
def run(path):
    reviews=[]
    myDict={}
    #load the positive and negative lexicons
    posLex=loadLexicon('positive-words.txt')
   
    
    fin=open(path)
    for line in fin: # for every line in the file (1 review per line)
        posList=[] #list of positive words in the review
       
        
        line=line.lower().strip()   
        reviews.append(line)
        
        words=line.split(' ') # slit on the space to get list of words
           
        for word in words: #for every word in the review
            if word in posLex: # if the word is in the positive lexicon
                
                if word not in posList: #if word not in positive list then 
                    posList.append(word) #update the positive list for this review
            
            
        for word in posList:  #now for every word in the positive list
            if word in myDict: #and if the the word is in my dictionary
                myDict[word]=myDict[word]+1 #count the words and increment 
            else:
                myDict[word]=1 #or else set the count to 1
    fin.close()
    return  myDict


print(run('textfile'))
       





