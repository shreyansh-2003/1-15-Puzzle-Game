"""
Developed by Shreyansh Padarha 
"""

# importing required libraries
from tkinter import *
import tkinter.font as font
import random

"""
1-15 puzzle game 
"""

"""
Parent Class GUI
consisting all the widgets for selection within the 1-15 puzzle game
"""


class GUI:

    def __init__(self, master):
        # creating an array that will help in creating the board and computing the moves
        self.posA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ""]
        self.copy = []

        random.shuffle(self.posA)  # initialising a shuffled array

        # generalised font for all pieces of the puzzle
        Calcis_Font = font.Font(size=40, weight='bold')

        self.buttonL = []  # list that will hold all button objects

        # Row 1
        self.btn1 = Button(master, text=self.posA[0], command=lambda: self.clickerFirstB(0),
                           fg='black', height=1, width=1, relief="raised")
        self.btn1['font'] = Calcis_Font
        self.btn1.grid(row=0, column=0, padx=1, pady=2, ipady=15, ipadx=20)
        self.buttonL.append(self.btn1)

        self.btn2 = Button(master, text=self.posA[1], command=lambda: self.clickRow0Center(1),
                           fg='black', bg='#788395', height=1, width=1)
        self.btn2['font'] = Calcis_Font
        self.btn2.grid(row=0, column=1, padx=1, pady=2, ipady=15, ipadx=20)
        self.buttonL.append(self.btn2)

        self.btn3 = Button(master, text=self.posA[2], command=lambda: self.clickRow0Center(2),
                           fg='black', bg='#788395', height=1, width=1)
        self.btn3['font'] = Calcis_Font
        self.btn3.grid(row=0, column=2, padx=1, pady=2, ipady=15, ipadx=20)
        self.buttonL.append(self.btn3)

        self.btn4 = Button(master, text=self.posA[3], command=lambda: self.clickBtn4(3),
                           fg='black', bg='#788395', height=1, width=1)
        self.btn4['font'] = Calcis_Font
        self.btn4.grid(row=0, column=3, padx=1, pady=2, ipady=15, ipadx=20)
        self.buttonL.append(self.btn4)

        # Row 2
        self.btn5 = Button(master, text=self.posA[4], command=lambda: self.clickColumn0(4),
                           fg='black', bg='#788395', height=1, width=1)
        self.btn5['font'] = Calcis_Font
        self.btn5.grid(row=1, column=0, padx=1, pady=1, ipady=15, ipadx=20)
        self.buttonL.append(self.btn5)

        self.btn6 = Button(master, text=self.posA[5], command=lambda: self.clickCenter(5),
                           fg='black', bg='#788395', height=1, width=1)
        self.btn6['font'] = Calcis_Font
        self.btn6.grid(row=1, column=1, padx=1, pady=1, ipady=15, ipadx=20)
        self.buttonL.append(self.btn6)

        self.btn7 = Button(master, text=self.posA[6], command=lambda: self.clickCenter(6),
                           fg='black', bg='#788395', height=1, width=1)
        self.btn7['font'] = Calcis_Font
        self.btn7.grid(row=1, column=2, padx=1, pady=1, ipady=15, ipadx=20)
        self.buttonL.append(self.btn7)

        self.btn8 = Button(master, text=self.posA[7], command=lambda: self.clickColumn3(7),
                           fg='black', bg='#788395', height=1, width=1)
        self.btn8['font'] = Calcis_Font
        self.btn8.grid(row=1, column=3, padx=1, pady=1, ipady=15, ipadx=20)
        self.buttonL.append(self.btn8)

        # row 3
        self.btn9 = Button(master, text=self.posA[8], command=lambda: self.clickColumn0(8),
                           fg='black', bg='#788395', height=1, width=1)
        self.btn9['font'] = Calcis_Font
        self.btn9.grid(row=2, column=0, padx=1, pady=1, ipady=15, ipadx=20)
        self.buttonL.append(self.btn9)

        self.btn10 = Button(master, text=self.posA[9], command=lambda: self.clickCenter(9),
                            fg='black', bg='#788395', height=1, width=1)
        self.btn10['font'] = Calcis_Font
        self.btn10.grid(row=2, column=1, padx=1, pady=1, ipady=15, ipadx=20)
        self.buttonL.append(self.btn10)

        self.btn11 = Button(master, text=self.posA[10], command=lambda: self.clickCenter(10),
                            fg='black', bg='#788395', height=1, width=1)
        self.btn11['font'] = Calcis_Font
        self.btn11.grid(row=2, column=2, padx=1, pady=1, ipady=15, ipadx=20)
        self.buttonL.append(self.btn11)

        self.btn12 = Button(master, text=self.posA[11], command=lambda: self.clickColumn3(11),
                            fg='black', bg='#788395', height=1, width=1)
        self.btn12['font'] = Calcis_Font
        self.btn12.grid(row=2, column=3, padx=1, pady=1, ipady=15, ipadx=20)
        self.buttonL.append(self.btn12)

        # row 4
        self.btn13 = Button(master, text=self.posA[12], command=lambda: self.clickBtn13(12),
                            fg='black', bg='#788395', height=1, width=1)
        self.btn13['font'] = Calcis_Font
        self.btn13.grid(row=3, column=0, padx=1, pady=1, ipady=15, ipadx=20)
        self.buttonL.append(self.btn13)

        self.btn14 = Button(master, text=self.posA[13], command=lambda: self.clickerRow3(13)
                            , fg='black', bg='#788395', height=1, width=1)
        self.btn14['font'] = Calcis_Font
        self.btn14.grid(row=3, column=1, padx=1, pady=1, ipady=15, ipadx=20)
        self.buttonL.append(self.btn14)

        self.btn15 = Button(master, text=self.posA[14], command=lambda:
        self.clickerRow3(14), fg='black', bg='brown', height=1, width=1)
        self.btn15['font'] = Calcis_Font
        self.btn15.grid(row=3, column=2, padx=1, pady=1, ipady=15, ipadx=20)
        self.buttonL.append(self.btn15)

        self.btn16 = Button(master, text=self.posA[15], command=lambda: self.clickerLast(15)
                            , fg='black', bg='#788395', height=1, width=1)
        self.btn16['font'] = Calcis_Font
        self.btn16.grid(row=3, column=3, padx=1, pady=1, ipady=15, ipadx=20)
        self.buttonL.append(self.btn16)

        # Shuffle (row 5)
        self.shfB = Button(master, text=" Shuffle ", command=self.shuffle, fg='black', bg='brown')
        self.shfB['font'] = Calcis_Font
        self.shfB.grid(row=4, columnspan=4, padx=10, pady=10, ipady=5, ipadx=35)

        # row 6 : creator label (row 6)
        self.cLabel = Label(master, text="Created by Shreyansh Padarha", fg='black', bg="#BA8C63")
        self.cLabel['font'] = font.Font(size=16, weight='bold')
        self.cLabel.grid(row=5, columnspan=4, sticky="e")

    # After shuffle button is clicked
    def shuffle(self):
        random.shuffle(self.posA)

        initial = 0

        # looping through the buttons and placing values according to the new shuffled array's indices
        for x in self.buttonL:
            if type(self.posA[initial]) != int:  # if the element is space / blank spot
                x['text'] = ""
            else:
                x['text'] = self.posA[initial]

            initial = initial + 1

    # function to display "game won" message
    def popupWon(self, master):
        wonPopup = Toplevel(master, bg="#CC9966")

        wonPopup.title(" 1-15 PUZZLE GAME ")
        wonPopup.geometry("320x110")
        wonPopup.resizable(width=False, height=False)

        Calcis_Font = font.Font(size=30, weight='bold')

        winMsg = Label(wonPopup, text="HURAH ! YOU WON", fg='black', bg='#CC9966')
        winMsg['font'] = Calcis_Font
        winMsg.grid(row=0, column=0, padx=15, pady=8)

        okButton = Button(wonPopup, text="OK", fg='black', command=wonPopup.destroy, bg='#CC9966',
                          font=("Arial", 20, 'bold'))
        okButton.grid(row=1, column=0)

    def isSorted(self):

        self.copy = self.posA[0:16]
        self.copy.remove("")

        if self.copy == sorted(self.copy):
            self.popupWon(puzzle)

        else:
            pass


"""
Child Inheritance Class Process
consisting all the process and commands for the buttons created in GUI 
"""

"""
-> Basic idea for checking which buttons must be swapped

if position_to_be_swapped is not an integer 
#which will mean its the only blank space string in the list
    then swap with it

"""


class Button_Clicks(GUI):

    def __init__(self, master):
        super().__init__(master)  # inheriting all attributes from parent class

    # for first button clicked
    # row : 0, column : 0
    def clickerFirstB(self, num):
        # places it could possibly move
        addOne = self.posA[num + 1]
        addFour = self.posA[num + 4]

        # if this position is "" then, it will be swapped
        if type(addOne) != int:
            self.swap(num, num + 1)
        # if this position is "" then, it will be swapped
        elif type(addFour) != int:
            self.swap(num, num + 4)

        # checking whether the list is sorted
        self.isSorted()

    # row : 0 ,column : 1 & 2
    def clickRow0Center(self, num):
        addOne = self.posA[num + 1]
        subOne = self.posA[num - 1]
        addFour = self.posA[num + 4]

        if type(addOne) != int:
            self.swap(num, num + 1)

        elif type(subOne) != int:
            self.swap(num, num - 1)

        elif type(addFour) != int:
            self.swap(num, num + 4)

    # row : 0 , column : 3
    def clickBtn4(self, num):
        subOne = self.posA[num - 1]
        addFour = self.posA[num + 4]

        if type(subOne) != int:
            self.swap(num, num - 1)

        elif type(addFour) != int:
            self.swap(num, num + 4)

    # row : 1,2 , column : 0
    def clickColumn0(self, num):
        subFour = self.posA[num - 4]
        addOne = self.posA[num + 1]
        addFour = self.posA[num + 4]

        if type(addOne) != int:
            self.swap(num, num + 1)

        elif type(addFour) != int:
            self.swap(num, num + 4)

        elif type(subFour) != int:
            self.swap(num, num - 4)

    # row : 1,2 , column : 3
    def clickColumn3(self, num):
        subFour = self.posA[num - 4]
        subOne = self.posA[num - 1]
        addFour = self.posA[num + 4]

        if type(subOne) != int:
            self.swap(num, num - 1)

        elif type(addFour) != int:
            self.swap(num, num + 4)

        elif type(subFour) != int:
            self.swap(num, num - 4)

    # row : 1,2 , column : 1,2
    def clickCenter(self, num):
        subFour = self.posA[num - 4]
        subOne = self.posA[num - 1]
        addOne = self.posA[num + 1]
        addFour = self.posA[num + 4]

        if type(addOne) != int:
            self.swap(num, num + 1)

        elif type(subOne) != int:
            self.swap(num, num - 1)

        elif type(addFour) != int:
            self.swap(num, num + 4)

        elif type(subFour) != int:
            self.swap(num, num - 4)

    # row : 3, column : 0
    # 13th button
    def clickBtn13(self, num):
        addOne = self.posA[num + 1]
        subFour = self.posA[num - 4]

        if type(addOne) != int:
            self.swap(num, num + 1)

        elif type(subFour) != int:
            self.swap(num, num - 4)

    # row : 3 , column 1,2
    def clickerRow3(self, num):
        addOne = self.posA[num + 1]
        subFour = self.posA[num - 4]
        subOne = self.posA[num - 1]

        if type(addOne) != int:
            self.swap(num, num + 1)

        elif type(subOne) != int:
            self.swap(num, num - 1)

        elif type(subFour) != int:
            self.swap(num, num - 4)

    # row : 3, column : 3
    # last button
    def clickerLast(self, num):
        subOne = self.posA[num - 1]
        subFour = self.posA[num - 4]

        if type(subOne) != int:
            self.swap(num, num - 1)

        elif type(subFour) != int:
            self.swap(num, num - 4)

        self.isSorted()

    # main function that swaps numbered position and empty spot
    def swap(self, swapee, blank):
        swapeeButton = self.buttonL[swapee]
        blankButton = self.buttonL[blank]

        temp = self.posA[swapee]
        self.posA[swapee] = ""
        self.posA[blank] = temp

        blankButton['text'] = self.posA[blank]
        swapeeButton['text'] = self.posA[swapee]


"""
MAIN DRIVER CODE
"""

if __name__ == "__main__":
    puzzle = Tk()
    puzzle.title(" 1-15 PUZZLE GAME ")
    puzzle.geometry("425x480")  # setting genomtry/size of the window
    puzzle.resizable(width=False, height=False)  # disabling manual readjustment of window
    puzzle.configure(bg="#BA8C63")  # setting a brown background colour

    root = GUI(puzzle)
    process = Button_Clicks(puzzle)

    puzzle.mainloop()

"""
Developed by Shreyansh Padarha
"""
