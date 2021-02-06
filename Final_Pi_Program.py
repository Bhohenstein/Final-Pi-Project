###PIano
#Group Members: Brenden Hohenstein, Alvin Kie, Frankie Lavall
#Date:12/2/20-3/2/21
#Description: Creates a program that turns the PI into a small piano or keyboard.

from tkinter import *
import pygame
from time import sleep

pygame.init()
Piano = [pygame.mixer.Sound("Piano.ff.C2.aiff"),pygame.mixer.Sound("Piano.mf.Ab1.aiff")
         ,pygame.mixer.Sound("Piano.mf.Eb2.aiff"),pygame.mixer.Sound("Piano.ff.F1.aiff")
         ,pygame.mixer.Sound("Piano.pp.C3.aiff")]
Keyboard = []

sounds = Piano

def changepiano():
    sounds == Piano
    print("Changed")
def changekey():
    sounds == Keyboard


#Main GUI
class MainGUI(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent,bg="white")
        self.parent = parent
        self.setupGUI()


        
    #Sets up GUI
    def setupGUI(self):

        #The Main Menu###########################################################
        menu = Menu(self.master)
        self.master.config(menu=menu)

        IMenu = Menu(menu)
        IMenu.add_command(label="Piano", command = lambda: changepiano())
        IMenu.add_command(label="Keyboard", command = lambda: changekey())
        menu.add_cascade(label="Instruments", menu= IMenu)

        
        #########################################################################
        
        #The Piano Keys################################################################################################
        #White Keys:
        self.key1 = Button(self.parent, bg="white",command = lambda: sounds[0].play())
        self.key1.grid(row=1,column=1,ipadx=15,ipady=100)

        self.key3 = Button(self.parent, bg="white",command = lambda: sounds[2].play())
        self.key3.grid(row=1,column=2,ipadx=15,ipady=100)

        self.key4 = Button(self.parent, bg="white",command = lambda: sounds[3].play())
        self.key4.grid(row=1,column=3,ipadx=15,ipady=100)

        self.key6 = Button(self.parent, bg="white",command = lambda: sounds[4].play())
        self.key6.grid(row=1,column=4,ipadx=15,ipady=100)

        self.key7 = Button(self.parent, bg="white")
        self.key7.grid(row=1,column=5,ipadx=15,ipady=100)

        self.key8 = Button(self.parent, bg="white")
        self.key8.grid(row=1,column=6,ipadx=15,ipady=100)

        self.key9 = Button(self.parent, bg="white")
        self.key9.grid(row=1,column=7,ipadx=15,ipady=100)

        self.key11 = Button(self.parent, bg="white")
        self.key11.grid(row=1,column=8,ipadx=15,ipady=100)

        self.key12 = Button(self.parent, bg="white",)
        self.key12.grid(row=1,column=9,ipadx=15,ipady=100)

        self.key14 = Button(self.parent, bg="white")
        self.key14.grid(row=1,column=10,ipadx=15,ipady=100)

        self.key15 = Button(self.parent, bg="white",)
        self.key15.grid(row=1,column=11,ipadx=15,ipady=100)

        self.key17 = Button(self.parent, bg="white")
        self.key17.grid(row=1,column=12,ipadx=15,ipady=100)

        #Black Keys;
        self.key2 = Button(self.parent, bg="black", command = lambda: sounds[1].play())
        self.key2.grid(row=1,column=1,columnspan=2,ipadx=15,ipady=55,sticky= N)
    
        self.key5 = Button(self.parent, bg="black")
        self.key5.grid(row=1,column=3,columnspan=2,ipadx=15,ipady=55,sticky= N)
        
        self.key7 = Button(self.parent, bg="black")
        self.key7.grid(row=1,column=5,columnspan=2,ipadx=15,ipady=55,sticky= N)
    
        self.key10 = Button(self.parent, bg="black")
        self.key10.grid(row=1,column=7,columnspan=2,ipadx=15,ipady=55,sticky= N)

        self.key13 = Button(self.parent, bg="black")
        self.key13.grid(row=1,column=9,columnspan=2,ipadx=15,ipady=55,sticky= N)

        self.key16 = Button(self.parent, bg="black")
        self.key16.grid(row=1,column=11,columnspan=2,ipadx=15,ipady=55,sticky= N)
        #######################################################################################


        #The default songs#####################################################################
        def stars(): #Plays "twinkle twinkle little star"
            self.key1.invoke()
            sleep(0.1)
            self.key3.invoke()
        def lambs(): #Plays "mary had a little lamb"
            self.key1.invoke()

        self.button4 = Button(self.parent, text = "Stars", fg="teal",command= stars)
        self.button4.grid(row=0,column=1,sticky=N+S+E+W)
        self.button5 = Button(self.parent, text = "Mary", fg="purple",command= stars)
        self.button5.grid(row=0,column=2,sticky=N+S+E+W)
        #######################################################################################



###Main Program
#Creates the window
window = Tk()

#Sets window title
window.title("PIano")

#Generates the GUI
P = MainGUI(window)
window.mainloop()
