# Author - jeev20. https://github.com/jeev20


# Features

                    #This program scraps NRK articles. Converts the News articles to text.
                    #Saves the article text in Article.txt file
                    #Converts text to speech and saves to Title.mp3, Heading.mp3 and Article.mp3 file



from bs4 import BeautifulSoup
from urllib import *
import urllib
import sys
import time
import webbrowser
from gtts import gTTS
import pygame

# open a public URL, in this case, the webbrowser
url1 = "https://www.nrk.no/"
webbrowser.open_new_tab(url1)

time.sleep(3)

# user can input NRK article link
url = raw_input("Please paste link of the NRK News article : ")


n = "Publisert av NRK"

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
                for authors in soup.find('div',class_= "container-widget-content authors authors--expandable").find_all('a'):  # if more than 1 author
                        a += authors.text[0:]
                return a
        except:
                try:
                        for authors in soup.find('a',class_= "author__name"): #for pages with one author
                                a += authors.string
                        return a
                except:
                        return n
        
        

# loop to print article text
def text():
	t=""
	for article in soup.find('div',class_= "article-body lp_articlebody text-body text-body-sans-serif container-widget-content nostack cf").findAll('p'):
	#for article in soup.find('div', class_="column--primary").findAll('p'):
		t += article.text[0:]
	return t
def firsttext():
	t=""
	for article in soup.find('div',class_= "text-body text-body-sans-serif article-lead").findAll('p'):
	#for article in soup.find('div', class_="column--primary").findAll('p'):
		t += article.text[0:]
		return t

def time():
	for article in soup.find('time',class_= "datetime-relative"):
		time = (article.string)
	return time		

file = open("Article.txt", "w")

reload(sys)
sys.setdefaultencoding('utf-8')
file.write(title() )
file.write("\n")
file.write(authors())
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
t = text()







tts = gTTS(text= title, lang = "no")
tts.save("Title.mp3")
pygame.mixer.init()
pygame.mixer.music.load("Title.mp3")
pygame.mixer.music.play()


tts = gTTS(text= firsttext, lang = "no")
tts.save("Heading.mp3")
pygame.mixer.init()
pygame.mixer.music.load("Heading.mp3")
pygame.mixer.music.play()

tts = gTTS(text= t, lang = "no")
tts.save("Article.mp3")
pygame.mixer.init()
pygame.mixer.music.load("Article.mp3")
pygame.mixer.music.play()


 





