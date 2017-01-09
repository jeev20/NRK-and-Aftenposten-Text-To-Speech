#codes are based from http://effbot.org/tkinterbook/entry.htm and textblob example
#audio credits to http://www.pacdv.com/sounds/voices-2.html

#Author- jeev20. https://github.com/jeev20

# Features

        #Performs Sentiment Analysis on the text pasted in the GUI input
        


from Tkinter import *
from textblob import TextBlob
import time
import tkMessageBox
from PIL import Image, ImageTk

import pygame



root = Tk()
root.geometry("850x450+300+400")
root.title("Text Sentiment Analyzer") 



# input of text in text input box
text = Text(root, width=10, height=10, wrap="word", font=("Helvetica",11))
text.insert('1.0', 'Paste required text here') # use this for user input  # this can be used as generic input (user pastes texts)
text.pack(fill=BOTH, padx=40, pady=20, ipadx=10, ipady=40)
text.focus_set()


#funtion with word counter
def word():
    data = text.get("1.0", "end")   # gets data from entry
    t = TextBlob(data)
    ans1.configure(text = "Total words: " + str(len(t.words)))
    
#button calling total words function
b2 = Button(root, text="Total words", font=("Helvetica",11,"bold"),  command=word,  bg="#CDDC39", fg="#000000").pack( side=LEFT, padx=10, pady=10)    

#function to analyse input text to make a sentiment analysis
def evaluate():
    data = text.get("1.0", 'end')   # gets data from entry
    t = TextBlob(data)
    s = (t.sentiment)
    sa = (t.sentiment.polarity)
    ans.configure(text = "Sentiment value: " + str(sa))
    return sa
    
#function for about menu    
def about():
    output = "Sentiment Analyzer V.1 is free to use software built using TextBlob and Tkinter python modules. \n \n Documentation: https://github.com/jeev20"
    tkMessageBox.showinfo("About", output)
    
#function ot close window     
def exit():
    root.destroy()

def help():
	output = " Paste any text for analysis."
	tkMessageBox.showinfo("Help", output)

#function to generate sound to reflecting sentiment values
def sound():   
	sa = evaluate()
	if sa <= -0.01 and sa >= -0.5:
		pygame.mixer.init()
		pygame.mixer.music.load("boooo.wav")
		pygame.mixer.music.play()
	elif sa <= -0.5 and sa >= -1:
		pygame.mixer.init()
		pygame.mixer.music.load("this-is-ridiculous.wav")
		pygame.mixer.music.play()
	elif sa == 0:
		pygame.mixer.init()
		pygame.mixer.music.load("hmmmm.wav")
		pygame.mixer.music.play()	
	elif sa >= 0.01 and sa <= 0.5:
		pygame.mixer.init()
		pygame.mixer.music.load("applause.wav")
		pygame.mixer.music.play()
	elif sa >= 0.5 and sa <= 1:
		pygame.mixer.init()
		pygame.mixer.music.load("thats-the-loveliest-thing.wav")
		pygame.mixer.music.play()
	else:
		 pass

#button calling evaluate function
b1 = Button(root, text="Evaluate Sentiment", font=("Helvetica",11,"bold"), command=evaluate and sound, bg="#CDDC39", fg="#000000").pack(side = RIGHT, padx=10, pady=10)


#label showing final result of sentiment analysis
ans1 = Label(root, background="#CDDC39")
ans1.configure(font=("Helvetica",11))
ans1.pack(side=LEFT, padx=10, pady=10)

ans = Label(root, background="#CDDC39")
ans.configure(font=("Helvetica",11))
ans.pack(side=RIGHT, padx=10, pady=10 )



# create a toplevel menu
menubar = Menu(root, background ="#E6EE9C")
menubar.add_command(label="About", command=about)
menubar.add_command(label="Help", command=help)
menubar.add_command(label="Quit", command=exit)

# display the menu
root.config(menu=menubar, background="#CDDC39")


root.mainloop()  #shows and runs the tKinter window





