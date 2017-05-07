"""
Created on Mon Feb 13 16:04:39 2017
Author: Vitaan

- Create a script named parser.py 

- Your script should define the following functions:

def getCritic(review): finds and returns the name of the critic from the given review object (you can re-use the definition from week5func.py).


def getRating(review):  finds and returns the rating from the given review object. The return value should be 'rotten' ,  'fresh', or 'NA' if the review doesn't have a rating.

 

def getSource(review):  finds and returns the source (e.g 'New York Daily News') of the review from the given review object. The return value should be 'NA' if the review doesn't have a source.

 

def getDate(review):  finds and returns the date of the review from the given review object. The return value should be  'NA' if the review doesn't have a date.


def getTextLen(review):  finds and returns the number of characters in the text of the review from the given review object. The return value should 'NA' if the review doesn't have text.

 

Notes:

- Use encode('ascii','ignore') for all return values that include text.

Grading Rubric:

- 20X5=100 items to return.  10 /100=0.1 points for each item 


"""


from bs4 import BeautifulSoup
import re
import time
import requests


def run(url):

    pageNum=1 # number of pages to collect

    fw=open('reviews.txt','w') # output file
	
    for p in range(1,pageNum+1): # for each page 

        print ('page',p)
        html=None

        if p==1: pageLink=url # url for page 1
        else: pageLink=url+'?page='+str(p)+'&sort=' # make the page url
		
        for i in range(5): # try 5 times
            try:
                #use the browser to access the url
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content # get the html
                break # we got the file, break the loop
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print ('failed attempt',i)
                time.sleep(2) # wait 2 secs
				
		
        if not html:continue # couldnt get the page, ignore
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 

        reviews=soup.findAll('div', {'class':re.compile('review_table_row')}) # get all the review divs

        for review in reviews:

          
            critic=getCritic(review)
            icon=getRating(review)
            source=getSource(review)
            date=getDate(review)
            text=getTextLen(review)
            
            print(critic)
            print(icon)
            print(source)
            print(date) 
            print(text)
        

    fw.close()

def getCritic(review):
    
    critic='NA' # initialize critic and text 
    criticChunk=review.find('a',{'href':re.compile('/critic/')})    
    if criticChunk: critic=criticChunk.text#.encode('ascii','ignore')
    
    return critic
    
def getRating(review):
    
    icon='NA'
    iconrev=review.find('div',{'class':'review_icon icon small fresh'})
    if iconrev: icon='fresh'
    else: icon='rotten'
    return icon
    
def getSource(review):
    
    source = 'NA'
    sourceChunk=review.find('a',{'href':re.compile('/source-')})
    if sourceChunk: source=sourceChunk.text#.encode('ascii','ignore')
    else: source='NA'
    
    return source

def getDate(review):
    
    date='NA'
    dateChunk=review.find('div',{'class':'review_date subtle small'})
    if dateChunk: date=dateChunk.text
    else: date ='NA'
    
    return date
    
def getTextLen(review):
    text='NA'
    textChunk=review.find('div',{'class':'the_review'})
    if textChunk: text=textChunk.text#.encode('ascii','ignore')	
    return len(text)
    
    
if __name__=='__main__':
    url='https://www.rottentomatoes.com/m/space_jam/reviews/'
    run(url)
    


