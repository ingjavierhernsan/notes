import sys
import tkinter as tk
from tkinter import messagebox as mb
from tkcalendar import DateEntry
import logging

class WinUI:
    def __init__(self):
        self.user, self.compname = self.infoPC()

        self.winform1=tk.Tk()

        self.winform1.title("Title")
        self.winform1.geometry("280x160")
        self.winform1.resizable(False, False)
        self.winform1.eval("tk::PlaceWindow . center")

        self.label1=tk.Label(self.winform1, text="User:")
        self.label1.place(x=20, y=10)

        self.label2=tk.Label(self.winform1, text=self.user)
        self.label2.place(x=90, y=10)

        self.label3=tk.Label(self.winform1, text="Name PC:")
        self.label3.place(x=20, y=30)

        self.label4=tk.Label(self.winform1, text=self.compname)
        self.label4.place(x=90, y=30)

        self.label5=tk.Label(self.winform1, text="Start:")
        self.label5.place(x=20, y=55)

        self.calender1=DateEntry(self.winform1, selectmode='day')
        self.calender1.place(x=60, y=55)

        self.label6=tk.Label(self.winform1, text="End:")
        self.label6.place(x=20, y=85)  

        self.calender2=DateEntry(self.winform1, selectmode='day')
        self.calender2.place(x=60, y=85)

        self.boton2=tk.Button(self.winform1, text="Process", command=self.process)
        self.boton2.place(x=40, y=115)

        self.boton1=tk.Button(self.winform1, text="Exit", command=self.exit)
        self.boton1.place(x=200, y=115)

        self.winform1.mainloop()
    
    def exit(self):
        sys.exit(0)

    def process(self):
        dtStart=self.calender1.get_date()
        strMonthStart=dtStart.strftime("%m")
        strYearStart=dtStart.strftime("%Y")

        dtEnd=self.calender2.get_date()
        strMonthEnd=dtEnd.strftime("%m")
        strYearEnd=dtEnd.strftime("%Y")

        try:
            1/0
            self.messageShow("Todo bien")
        except Exception as e:
            self.messageShow(e)

        #mb.showinfo("Information", "Date start: " + strMonthStart + " - " + strYearStart)
        #mb.showinfo("Information", "Date end: " + strMonthEnd + " - " + strYearEnd)
    
    def messageShow(self, messageStr):
        logging.debug(messageStr)
        mb.showinfo("Information", messageStr)

    def infoPC(self):
        return "javier", "xxxxx"

winui1=WinUI()