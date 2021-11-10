from tkinter import *
from tkinter import font
from tkinter.ttk import *


class VIEW:
    def __init__(self) -> None:

        self.root = Tk()
        self.root.title('Control ESP')
        self.root.geometry('800x600')
        self._id = StringVar()
        self._pass = StringVar()
        self._token = StringVar()
        #row configure
        self.root.rowconfigure(0, weight=3)
        self.root.rowconfigure(1, weight=2)
        self.root.rowconfigure(2, weight=2)
        self.root.rowconfigure(3, weight=2)
        self.root.rowconfigure(4, weight=2)
        #column configure
        # self.root.columnconfigure(0, weight=2)
        # self.root.columnconfigure(1, weight=2)
        self.initLabel()
        self.initButton()
        self.initEntry()

    def initButton(self):
        self.button1 = Button(self.root, text='B1', command=None)
        self.button1.grid(column=1, row=4, ipady=10)
        self.button2 = Button(self.root, text='B2', command=None)
        self.button2.grid(column=2, row=4, ipady=10)
        self.button3 = Button(self.root, text='B3-SENT', command=None)
        self.button3.grid(column=3, row=4, ipady=10, padx=5)

    def initEntry(self):
        self.ID_input = Entry(self.root, textvariable=self._id, font=('Arial', 10, 'bold'))
        self.ID_input.grid(column=1, row=1, ipady=10, ipadx=10)
        self.pass_input = Entry(self.root, textvariable=self._pass, font=('Arial', 10, 'bold'))
        self.pass_input.grid(column=1, row=2, ipady=10, ipadx=10)
        self.token_input = Entry(self.root, textvariable=self._token, font=('Arial', 10, 'bold'))
        self.token_input.grid(column=1, row=3, ipady=10, ipadx=10)
    
    def initLabel(self):
        self.labelTitle = Label(self.root, text='ESP Control', anchor=CENTER, font=('Arial', 30, 'bold'))
        self.labelTitle.grid(column=0, row=0)
        self.labelID = Label(self.root, text = 'ID:', anchor=CENTER, font=('Arial', 15, 'bold'))
        self.labelID.grid(column=0, row=1)
        self.Passowrd = Label(self.root, text = 'Password:', anchor=CENTER, font=('Arial', 15, 'bold'))
        self.Passowrd.grid(column=0, row=2)
        self.token = Label(self.root, text='Token:', anchor=CENTER, font=('Arial', 15, 'bold'))
        self.token.grid(column=0, row=3)

def main():
    pass
    

if __name__ == "__main__":
    main()