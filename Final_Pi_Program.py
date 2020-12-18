###PIano
#Group Members: Brenden Hohenstein, Alvin Kie, Frankie Lavall
#Date:12/2/20-3/2/21
#Description: Creates a program that turns the PI into a small piano or keyboard.

from tkinter import *
import pygame

pygame.init()
sounds = [pygame.mixer.Sound("Piano.ff.A0.aiff")]

#Main GUI
class MainGUI(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent,bg="white")
        self.parent = parent
        self.setupGUI()
        

    #Sets up GUI
    def setupGUI(self):
        #The Main Menu
        self.button1 = Button(self.parent, text = "QUIT",fg="red",command = self.quit)
        self.button1.grid(row=0,column=6,sticky=E)
        #self.button2 = Button(self.parent, text = "Piano", fg="green")
        #self.button2.grid(row=0,column=0,sticky=W)
        #self.button3 = Button(self.parent, text = "Keyboard", fg="blue")
        #self.button3.grid(row=0,column=0,sticky=E)

        
        #The Piano and buttons
        #the ipadx and ipady control how big the keys are, these will probably need to be tested and changed for the PI's screen. 
        self.key1 = Button(self.parent, bg="white",command = sounds[1].play())
        self.key1.grid(row=1,column=0,ipadx=75,ipady=125)
        
        self.key2 = Button(self.parent, bg="black")
        self.key2.grid(row=1,column=1,ipadx=50,ipady=125)
        
        self.key3 = Button(self.parent, bg="white")
        self.key3.grid(row=1,column=2,ipadx=75,ipady=125)
        
        self.key4 = Button(self.parent, bg="black")
        self.key4.grid(row=1,column=3,ipadx=50,ipady=125)
        
        self.key5 = Button(self.parent, bg="white")
        self.key5.grid(row=1,column=4,ipadx=75,ipady=125)
        
        self.key6 = Button(self.parent, bg="black")
        self.key6.grid(row=1,column=5,ipadx=50,ipady=125)
        
        self.key7 = Button(self.parent, bg="white")
        self.key7.grid(row=1,column=6,ipadx=75,ipady=125)




###Main Program
#Creates the window
window = Tk()

#Sets window title
window.title("PIano")

#Generates the GUI
P = MainGUI(window)
window.mainloop()
