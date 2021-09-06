import socket
from tkinter import * 
from  threading import Thread
from typing import Counter
from PIL import ImageTk, Image
import random

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None


canvas1 = None

playerName = None
nameEntry = None
nameWindow = None
ticketGrid = None
currentNumberList = None


def createTicket():
    global nameWindow
    global ticketGrid
    #Ticket Frame
    mianLabel = Label(nameWindow,width=65,height=16,relief=RIDGE,borderwidth=5,bg='white')
    mianLabel.place(x=95,y=119)

    xPos = 105
    yPos = 130
    for row in range(0,3):
        rowlist = []
        for col in range(0,9):
            if(platform.system() == 'Darwin'):
                #For Mac users
                 boxButton = Button(nameWindow,
                 font=("Chalkbard SE",18),
                 borderwidth=3,
                 pady=23,
                 padx=22,
                 bg="#fff176", #Intial Yellow color
                 highlightbackground="#fff176",
                 activebackground='#c5ela5') #onPress Green Color


                 boxButton.place(x=xPos,y=yPos)
            else:
                #For window users
                boxButton = tk.Button(nameWindow,font=("Chalkbard SE",30),width=3,height=2,borderwidth=5,bg='#fff176')

            rowlist.append(boxButton)
            xPos += 64
        #Creating nested array
        ticketGrid.append(rowlist)
        xPos = 105
        yPos +=82

def placeNumbers():
    global ticketGrid
    global currentNumberList

    for row in range(0,3):
        randomColList = []
        counter = 0
        #getting random 5 cols
        while counter<=4:
            randomCol = random.randint(0,8)
            if(randomCol not in randomColList):
                randomColList.append(randomCol)
                counter+=1
    #Here Key is index and values are numbers
    numberContainer = {
    "0": [1,2,3,4,5,6,7,8,9],
    "1" : [10,11,12,13,14,15,16,17,18,19],
    "2" : [20,21,22,23,24,25,26,27,28,29],
    "3" : [30,31,32,33,34,35,36,37,38,39],
    "4" : [40,41,42,43,44,45,46,47,48,49],
    "5" : [50,51,52,53,54,55,56,57,58,59],
    "6" : [60,61,62,63,64,65,66,67,68,69],
    "7" : [70,71,72,73,74,75,76,77,78,79],
    "8" : [80,81,82,83,84,85,86,87,88,89]
    }

    #palce an number to practice positon in ticket
    counter = 0
    while (counter < len(randomColList)):
        colNum = randomColList[counter]
        numbersListByIndex = numberContainer[str(colNum)]
        randomNumber = random.choice(numbersListByIndex)

        if(randomNumber not in currentNumberList):
            numberBox = ticketGrid[row] [colNum]
            numberBox.configure(text=randomNumber, fg="black")
            currentNumberList.append(randomNumber)

            counter+=1

def saveName():
    global SERVER
    global playerName
    global nameWindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy()

    SERVER.send(playerName.encode())


def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1
    global screen_width
    global screen_height

    nameWindow  = Tk()
    nameWindow.title("Tambola Family Fun")
    nameWindow.attributes('-fullscreen',True)


    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/background.png")

    canvas1 = Canvas( nameWindow, width = 500,height = 500)
    canvas1.pack(fill = "both", expand = True)

    canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_text( screen_width/2, screen_height/5, text = "Enter Name", font=("Chalkboard SE",100), fill="white")

    nameEntry = Entry(nameWindow, width=15, justify='center', font=('Chalkboard SE', 50), bd=5, bg='white')
    nameEntry.place(x = screen_width/2 - 220, y=screen_height/4 + 100)

    button = Button(nameWindow, text="Save", font=("Chalkboard SE", 30),width=15, command=saveName, height=2, bg="#80deea", bd=3)
    button.place(x = screen_width/2 - 130, y=screen_height/2 - 30)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 5000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


    askPlayerName()




setup()
