
#Author- jeev20. https://github.com/jeev20

# Features

        #This program scraps Aftenposten articles. Converts the News articles to text.
        #Saves the article text in newfile.txt file
        #Converts text to speech and saves to Title.mp3, Heading.mp3 and Article.mp3 file



from bs4 import BeautifulSoup
from urllib import *
import urllib
from textblob import TextBlob
import sys
import time
import webbrowser
from gtts import gTTS
import pygame



# open a public URL, in this case, the webbrowser
url1 = "http://www.aftenposten.no/"
webbrowser.open_new_tab(url1)

time.sleep(3)

# user can input Aftenposten article link
url = raw_input("Please paste link of the Aftenposten news article : ")


n = "Publisert av Aftenposten"

#input webaddress of the twitter account
webadd = urllib.urlopen(url).read()
soup = BeautifulSoup(webadd, "html.parser")
BeautifulSoup(webadd,from_encoding="utf-8")

#tweet title extraction
def title():
	return(soup.title.text)

def authors():
        a=""
        
        try:
                for authors in soup.find_all('div',class_= "author-name section-color-primary"):  # if more than 1 author
                        a += authors.text[0:]
                        return a
        except:
                try:
                        for authors in soup.find_all('div',class_= "author-name section-color-primary"): #for pages with one aut
                                a = authors.text[0:]
                                return a
                except:
                        return n
        
        

# loop to return article text
def text():
	t=""
	for article in soup.find('div',class_= "article-body").findAll('p'):
	#for article in soup.find('div', class_="column--primary").findAll('p'):
		t += article.text[0:]
	return t
def firsttext():
	t=""
	for article in soup.find('p',class_= "article-description").findAll('p'):
	#for article in soup.find('div', class_="column--primary").findAll('p'):
		t += article.text[0:]
	return t

def time():
	for article in soup.find('time',class_= "date published"):
		time = article.string
	return time		






 
file = open("newfile.txt", "w")

reload(sys)
sys.setdefaultencoding('utf-8')
file.write("\n")
file.write(title()  )
file.write("\n")
file.write(authors() )
file.write("\n")
file.write(time())
file.write("\n")
file.write(firsttext())
file.write("\n")
file.write(text())

file.close()

# Debugging
print title()
title = title()
print ""
print authors()
print time()
print ""
print firsttext()
firsttext = firsttext()
print text()
article = text()



tts = gTTS(text= title, lang = "no")
tts.save("Title.mp3")
pygame.mixer.init()
pygame.mixer.music.load("Title.mp3")
pygame.mixer.music.play()

tts = gTTS(text= article, lang = "no")
tts.save("Article.mp3")
pygame.mixer.init()
pygame.mixer.music.load("Article.mp3")
pygame.mixer.music.play()




 
