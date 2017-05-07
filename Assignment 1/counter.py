"""
Author: Vitaan Thapar
- Create a new script named counter.py 

- The script should include a single function run().

- The run() function should accept as input the path to an input file with the same structure as 'textfile'

- The run() function should return the most frequent word in the input file.

"""

#define a new function
def run(path):
    myDict={} # new dictionary. Maps each word to each frequency 
	    
    fin=open(path) # open a connection to the file 
    for line in fin: # read the file line by line 
        # lower() converts all the letters in the string to lower-case
        # strip() removes blank space from the start and end of the string
        # split(c) splits the string on the character c and returns a list of the pieces. For example, "A1B1C1D".split('1')" returns [A,B,C,D]
        words=line.lower().strip().split(' ')
       
        # use for to go over all the words in the list 
        for word in words: # for each word in the line
            if word in myDict: 
                myDict[word]=myDict[word]+1 # if the word is present, then increase the count of word by 1
            elif word==word: 
                myDict[word]=1 # if a new word occurs then store its count as 1
    fin.close() #close the connection to the text file 

    return max(myDict, key=myDict.get)  #returning the word with the maximum count

freq = run('textfile.txt')
print (freq)  #printint the word with max frequency

