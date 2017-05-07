"""
Author: Vitaan

The script visits the profile of a given twitter user, scrolls down the screen twice to load more tweets,
and then write the text and number of likes for each tweet to a file.

Extend the twitter.py script so that it also writes the following information for each tweet to the output file:

- The number of Favorites

- The number of Replies

- The date (Just day and month)
"""


from selenium import webdriver
import time
import codecs


url='https://twitter.com/iamsrk'

#open the browser and visit the url
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

#scroll down twice to load more tweets
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

#find all elements with a class that ends in 'tweet-text'
tweets=driver.find_elements_by_css_selector("[data-item-type=tweet]")

"""
for tweet in tweets:
    print (tweet.find_element_by_css_selector("[class$=tweet-text"))
"""

#write the tweets to a file
fw=codecs.open('tweets.txt','w',encoding='utf-8')
for tweet in tweets:
    txt,retweets,favs,replies,date='NA','NA','NA','NA','NA'
    
    try: txt=tweet.find_element_by_css_selector("[class$=tweet-text]").text
    except: print ('no text')     

    try:
        retweetElement=tweet.find_element_by_css_selector("[class$=js-actionRetweet]")
        retweets=retweetElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    except:
        print ('no retweets')
    
    try:
        favElement=tweet.find_element_by_css_selector("[class$=js-actionFavorite]")
        favs=favElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    except:
        print ('no favourites')    
    
    try:
        repElement=tweet.find_element_by_css_selector("[class$=js-actionReply]")
        replies=repElement.find_element_by_css_selector('[class=ProfileTweet-actionCountForPresentation]').text                                      
    except:
        print ('no replies')
        
    try:
        date=tweet.find_element_by_css_selector("[class=time]").find_element_by_css_selector('[data-long-form="true"]').text 
                                                    
    except:
        print ('no date')   
        
    fw.write(txt.replace('\n',' ')+'\n'+str(retweets)+'\n' + str(favs) +'\n'+ str(replies) +'\n'+ str(date)+'\n')


fw.close()


driver.quit()#close the browser
