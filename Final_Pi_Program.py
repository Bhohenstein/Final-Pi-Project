###PIano
#Group Members: Brenden Hohenstein, Alvin Kie, Frankie Lavall
#Date:12/2/20-3/2/21
#Description: Creates a program that turns the PI into a small piano or keyboard.

from tkinter import *
from time import sleep
import pygame

pygame.init()
Piano = [pygame.mixer.Sound("c2.aiff"),pygame.mixer.Sound("d2.aiff") #White Keys
         ,pygame.mixer.Sound("e2.aiff"),pygame.mixer.Sound("f2.aiff")
         ,pygame.mixer.Sound("g2.aiff"),pygame.mixer.Sound("a2.aiff")
         ,pygame.mixer.Sound("b2.aiff"),pygame.mixer.Sound("c4.aiff")
         ,pygame.mixer.Sound("d4.aiff"),pygame.mixer.Sound("e4.aiff")
         ,pygame.mixer.Sound("f4.aiff"),pygame.mixer.Sound("g4.aiff")
         ,pygame.mixer.Sound("a4.aiff"),pygame.mixer.Sound("b4.aiff")
         #Black Keys
        ,pygame.mixer.Sound("Db2.aiff"),pygame.mixer.Sound("Eb2.aiff")
        ,pygame.mixer.Sound("F#2.aiff"),pygame.mixer.Sound("Ab2.aiff")
        ,pygame.mixer.Sound("Bb2.aiff"),pygame.mixer.Sound("Db4.aiff")
        ,pygame.mixer.Sound("Eb4.aiff"),pygame.mixer.Sound("F#4.aiff")
        ,pygame.mixer.Sound("Ab4.aiff"),pygame.mixer.Sound("Bb4.aiff")]



Xylophone = [pygame.mixer.Sound("c2xylo.aiff"),pygame.mixer.Sound("d2xylo.aiff") #White Keys
             ,pygame.mixer.Sound("e2xylo.aiff"),pygame.mixer.Sound("f2xylo.aiff")
             ,pygame.mixer.Sound("g2xylo.aiff"),pygame.mixer.Sound("a2xylo.aiff")
             ,pygame.mixer.Sound("b2xylo.aiff"),pygame.mixer.Sound("c4xylo.aiff")
             ,pygame.mixer.Sound("d4xylo.aiff"),pygame.mixer.Sound("e4xylo.aiff")
             ,pygame.mixer.Sound("f4xylo.aiff"),pygame.mixer.Sound("g4xylo.aiff")
             ,pygame.mixer.Sound("a4xylo.aiff"),pygame.mixer.Sound("b4xylo.aiff")
             #Black Keys
            ,pygame.mixer.Sound("Db2xylo.aiff"),pygame.mixer.Sound("Eb2xylo.aiff")
            ,pygame.mixer.Sound("F#2xylo.aiff"),pygame.mixer.Sound("Ab2xylo.aiff")
            ,pygame.mixer.Sound("Bb2xylo.aiff"),pygame.mixer.Sound("Db4xylo.aiff")
            ,pygame.mixer.Sound("Eb4xylo.aiff"),pygame.mixer.Sound("F#4xylo.aiff")
            ,pygame.mixer.Sound("Ab4xylo.aiff"),pygame.mixer.Sound("Bb4xylo.aiff")]

Perc = [pygame.mixer.Sound("Basic_Rock_135.mp3"),pygame.mixer.Sound("Cymbal_Groove.mp3")] 

Strings = [] #Violin and Guitar


#Main GUI
class MainGUI(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent,bg="white")
        self.parent = parent
        self.setupGUI()
        self.sounds = Piano

    def changesounds(self,sound):
        if sound == "piano":
            self.sounds = Piano
            print("Piano")
        if sound == "xylo":
            self.sounds = Xylophone
            print("Xylophone")
        if sound == ("strings"):
            self.sounds = Strings
            print("Strings")
        if sound == ("perc"):
            self.sounds = Perc
            print("Percussion")

    
    def playsounds(self,note):
        self.sounds[note].play()
        self.after(500) #Find a way to implement this that doesn't slow down the whole program.
        

        

    def playsong(self,note):
        self.sounds[note].play()
        self.after(780) #Find a way to implement this that doesn't slow down the whole program.
        self.sounds[note].stop()
        
        

        
    #Sets up GUI
    def setupGUI(self):

        #The Main Menu###########################################################
        menu = Menu(self.master)
        self.master.config(menu=menu)

        IMenu = Menu(menu)
        IMenu.add_command(label="Piano", command = lambda: self.changesounds("piano"))
        IMenu.add_command(label="Xylophone", command = lambda: self.changesounds("xylo"))
        IMenu.add_command(label="Percussion", command = lambda: self.changesounds("perc"))
        IMenu.add_command(label="Strings", command = lambda: self.changesounds("strings"))
        menu.add_cascade(label="Instruments", menu= IMenu)

        
        #########################################################################
        
        #The Piano Keys################################################################################################
        #the ipadx and ipady control how big the keys are, these will probably need to be tested and changed for the PI's screen.
        #White Keys:
        self.key1 = Button(self.parent, bg="white",command = lambda: self.playsounds(0))
        self.key1.grid(row=1,column=1,ipadx=15,ipady=100)

        self.key3 = Button(self.parent, bg="white",command = lambda: self.playsounds(1))
        self.key3.grid(row=1,column=2,ipadx=15,ipady=100)

        self.key5 = Button(self.parent, bg="white",command = lambda: self.playsounds(2))
        self.key5.grid(row=1,column=3,ipadx=15,ipady=100)

        self.key6 = Button(self.parent, bg="white",command = lambda: self.playsounds(3))
        self.key6.grid(row=1,column=4,ipadx=15,ipady=100)

        self.key8 = Button(self.parent, bg="white",command = lambda: self.playsounds(4))
        self.key8.grid(row=1,column=5,ipadx=15,ipady=100)

        self.key10 = Button(self.parent, bg="white",command = lambda: self.playsounds(5))
        self.key10.grid(row=1,column=6,ipadx=15,ipady=100)

        self.key12 = Button(self.parent, bg="white",command = lambda: self.playsounds(6))
        self.key12.grid(row=1,column=7,ipadx=15,ipady=100)

        self.key13 = Button(self.parent, bg="white",command = lambda: self.playsounds(7))
        self.key13.grid(row=1,column=8,ipadx=15,ipady=100)

        self.key15 = Button(self.parent, bg="white",command = lambda: self.playsounds(8))
        self.key15.grid(row=1,column=9,ipadx=15,ipady=100)

        self.key17 = Button(self.parent, bg="white",command = lambda: self.playsounds(9))
        self.key17.grid(row=1,column=10,ipadx=15,ipady=100)

        self.key18 = Button(self.parent, bg="white",command = lambda: self.playsounds(10))
        self.key18.grid(row=1,column=11,ipadx=15,ipady=100)

        self.key20 = Button(self.parent, bg="white",command = lambda: self.playsounds(11))
        self.key20.grid(row=1,column=12,ipadx=15,ipady=100)

        self.key22 = Button(self.parent, bg="white",command = lambda: self.playsounds(12))
        self.key22.grid(row=1,column=13,ipadx=15,ipady=100)

        self.key24 = Button(self.parent, bg="white",command = lambda: self.playsounds(13))
        self.key24.grid(row=1,column=14,ipadx=15,ipady=100)



        #Black Keys:
        self.key2 = Button(self.parent, bg="black",command = lambda: self.playsounds(14))
        self.key2.grid(row=1,column=1,columnspan=2,ipadx=10,ipady=55,sticky= N)
    
        self.key4 = Button(self.parent, bg="black",command = lambda: self.playsounds(15))
        self.key4.grid(row=1,column=2,columnspan=2,ipadx=10,ipady=55,sticky= N)
        
        self.key7 = Button(self.parent, bg="black",command = lambda: self.playsounds(16))
        self.key7.grid(row=1,column=4,columnspan=2,ipadx=10,ipady=55,sticky= N)
    
        self.key9 = Button(self.parent, bg="black",command = lambda: self.playsounds(17))
        self.key9.grid(row=1,column=5,columnspan=2,ipadx=10,ipady=55,sticky= N)

        self.key11 = Button(self.parent, bg="black",command = lambda: self.playsounds(18))
        self.key11.grid(row=1,column=6,columnspan=2,ipadx=10,ipady=55,sticky= N)

        self.key14 = Button(self.parent, bg="black",command = lambda: self.playsounds(19))
        self.key14.grid(row=1,column=8,columnspan=2,ipadx=10,ipady=55,sticky= N)

        self.key16 = Button(self.parent, bg="black",command = lambda: self.playsounds(20))
        self.key16.grid(row=1,column=9,columnspan=2,ipadx=10,ipady=55,sticky= N)

        self.key19 = Button(self.parent, bg="black",command = lambda: self.playsounds(21))
        self.key19.grid(row=1,column=11,columnspan=2,ipadx=10,ipady=55,sticky= N)

        self.key21 = Button(self.parent, bg="black",command = lambda: self.playsounds(22))
        self.key21.grid(row=1,column=12,columnspan=2,ipadx=10,ipady=55,sticky= N)

        self.key23 = Button(self.parent, bg="black",command = lambda: self.playsounds(23))
        self.key23.grid(row=1,column=13,columnspan=2,ipadx=10,ipady=55,sticky= N)
        #######################################################################################



        #The default songs#####################################################################
        def stars(): #Plays "twinkle twinkle little star"
            self.playsong(7)
            self.playsong(7)
            self.playsong(11)
            self.playsong(11)
            self.playsong(12)
            self.playsong(12)
            self.playsong(11)
            sleep(.75)
            self.playsong(10)
            self.playsong(10)
            self.playsong(9)
            self.playsong(9)
            self.playsong(8)
            self.playsong(8)
            self.playsong(7)
            sleep(.75)
            self.playsong(11)
            self.playsong(11)
            self.playsong(10)
            self.playsong(10)
            self.playsong(9)
            self.playsong(9)
            self.playsong(8)
            sleep(.75)
            self.playsong(11)
            self.playsong(11)
            self.playsong(10)
            self.playsong(10)
            self.playsong(9)
            self.playsong(9)
            self.playsong(8)
            sleep(.75)
            self.playsong(7)
            self.playsong(7)
            self.playsong(11)
            self.playsong(11)
            self.playsong(12)
            self.playsong(12)
            self.playsong(11)
            sleep(.75)
            self.playsong(10)
            self.playsong(10)
            self.playsong(9)
            self.playsong(9)
            self.playsong(8)
            self.playsong(8)
            self.playsong(7)
            sleep(.75)
            
            
        def lambs(): #Plays "mary had a little lamb"
            self.playsong(9)
            self.playsong(8)
            self.playsong(7)
            self.playsong(8)
            self.playsong(9)
            self.playsong(9)
            self.playsong(9)
            sleep(.5)
            self.playsong(8)
            self.playsong(8)
            self.playsong(8)
            self.playsong(9)
            self.playsong(11)
            self.playsong(11)
            sleep(.5)
            self.playsong(9)
            self.playsong(8)
            self.playsong(7)
            self.playsong(8)
            self.playsong(9)
            self.playsong(9)
            self.playsong(9)
            sleep(.5)
            self.playsong(9)
            self.playsong(8)
            self.playsong(8)
            self.playsong(9)
            self.playsong(8)
            self.playsong(7)
            

        def sheep(): #Plays black sheep.
            self.playsong(7)
            self.playsong(7)
            self.playsong(11)
            self.playsong(11)

            self.playsong(12)
            self.playsong(12)
            self.playsong(12)
            self.playsong(12)
            self.playsong(11)

            self.playsong(10)
            self.playsong(10)
            self.playsong(9)
            self.playsong(9)

            self.playsong(8)
            self.playsong(8)
            self.playsong(7)

            self.playsong(11)
            self.playsong(11)
            self.playsong(11)
            self.playsong(10)
            self.playsong(10)

            self.playsong(9)
            self.playsong(9)
            self.playsong(9)
            self.playsong(8)

            self.playsong(7)
            self.playsong(11)
            self.playsong(11)
            self.playsong(11)
            self.playsong(10)
            self.playsong(10)
            self.playsong(10)

            self.playsong(10)
            self.playsong(9)
            self.playsong(9)
            self.playsong(9)
            self.playsong(8)

            self.playsong(7)
            self.playsong(7)
            self.playsong(11)
            self.playsong(11)

            self.playsong(12)
            self.playsong(12)
            self.playsong(12)
            self.playsong(12)
            self.playsong(11)

            self.playsong(10)
            self.playsong(10)
            self.playsong(9)
            self.playsong(9)

            self.playsong(8)
            self.playsong(8)
            self.playsong(7)

        def HBD(): #Plays happy birthday song
            self.playsong(11)
            self.playsong(11)
            self.playsong(12)
            self.playsong(11)
            self.playsong(7)
            self.playsong(13)
            sleep(.5)
            self.playsong(11)
            self.playsong(11)
            self.playsong(12)
            self.playsong(11)
            self.playsong(8)
            self.playsong(7)
            sleep(.5)
            self.playsong(11)
            self.playsong(11)
            self.playsong(11)
            self.playsong(9)
            self.playsong(7)
            self.playsong(13)
            self.playsong(12)
            sleep(.5)
            self.playsong(10)
            self.playsong(10)
            self.playsong(9)
            self.playsong(7)
            self.playsong(8)
            self.playsong(7)
            




        self.button4 = Button(self.parent, text = "Stars", fg="teal",command= stars)
        self.button4.grid(row=0,column=1,sticky=N+S+E+W)
        self.button5 = Button(self.parent, text = "Mary", fg="purple",command= lambs)
        self.button5.grid(row=0,column=2,sticky=N+S+E+W)
        self.button6 = Button(self.parent, text = "Sheep", fg="black",command= sheep)
        self.button6.grid(row=0,column=3,sticky=N+S+E+W)
        self.button7 = Button(self.parent, text = "HBD", fg="red",command= HBD)
        self.button7.grid(row=0,column=4,sticky=N+S+E+W)
        #######################################################################################



###Main Program
#Creates the window
window = Tk()

#Sets window title
window.title("PIano")

#Generates the GUI
P = MainGUI(window)
window.mainloop()
