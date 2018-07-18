from tkinter import *
from tkinter import ttk


import pandas as pd
import numpy as np

from collections import defaultdict
from sklearn.linear_model import LinearRegression, LogisticRegression
from modelGenerator import *


root = Tk()
root.title("Cricket Prediction")
root.minsize(width=500, height=500)


class match:
    def __init__(self, master):
        self.master = master
        self.master.config(bg='black')
        self.headFont = ('times', 20, 'bold')
        self.headingLabel = Label(master, text="Cricket Match Prediction", fg='blue', bg='black')
        self.headingLabel.config(font=self.headFont)
        self.formHeadingLabel = Label(master, text="Enter details : ", bg='black', fg='white')
        self.subHeadFont = ('times', 15, 'bold')
        self.formHeadingLabel.config(font=self.subHeadFont)

        self.team1Label = Label(master, text="Enter team1", fg='white', bg='black')
        self.team1Entry = Entry(master)

        self.team2Label = Label(master, text="Enter team2", fg='white', bg='black')
        self.team2Entry = Entry(master)

        self.cityLabel = Label(master, text="Enter City", fg='white', bg='black')
        self.cityEntry = Entry(master)

        self.tossWinnerLabel = Label(master, text="Enter tossWinner", fg='white', bg='black')
        self.tossWinnerEntry = Entry(master)

        self.tossDecisionLabel = Label(master, text="Enter tossDecision", fg='white', bg='black')
        self.tossDecisionEntry = Entry(master)

        self.submit = Button(master, text="Submit", command=self.doPredicit)
        #self.submitq=Button(master,text="graph",command=self.graph)
        self.headingLabel.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

        self.formHeadingLabel.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        self.team1Entry=ttk.Combobox()
        self.team1Entry["values"]=("Australia","India","Pakistan","England","South Africa","New Zealand","Sri Lanka","Bangladesh","West Indies","Zimbabwe")
        self.team1Entry.set("Australia")
        self.team1Label.grid(row=2, columnspan=2, sticky=E, padx=15, pady=15)
        self.team1Entry.grid(row=2, column=2, columnspan=2, padx=18, pady=18)

        self.team2Entry = ttk.Combobox()
        self.team2Entry["values"] = ("Australia", "India", "Pakistan", "England", "South Africa", "New Zealand", "Sri Lanka", "Bangladesh",
        "West Indies", "Zimbabwe")
        self.team2Entry.set("South Africa")
        self.team2Label.grid(row=3, columnspan=2, sticky=E, padx=18, pady=18)
        self.team2Entry.grid(row=3, column=2, columnspan=2, padx=18, pady=18)

        self.cityLabel.grid(row=4, columnspan=2, sticky=E, padx=18, pady=18)
        self.cityEntry.grid(row=4, column=2, columnspan=2, padx=18, pady=18)

        self.tossWinnerEntry = ttk.Combobox()
        self.tossWinnerEntry["values"] = (
        "Australia", "India", "Pakistan", "England", "South Africa", "New Zealand", "Sri Lanka", "Bangladesh",
        "West Indies", "Zimbabwe")
        self.tossWinnerEntry.set("Australia")
        self.tossWinnerLabel.grid(row=5, columnspan=2, sticky=E, padx=18, pady=18)
        self.tossWinnerEntry.grid(row=5, column=2, columnspan=2, padx=18, pady=18)

        self.tossDecisionEntry = ttk.Combobox()
        self.tossDecisionEntry["values"] = ("Bat","Ball")
        self.tossDecisionEntry.set("Bat")
        self.tossDecisionLabel.grid(row=6, columnspan=2, sticky=E, padx=18, pady=18)
        self.tossDecisionEntry.grid(row=6, column=2, columnspan=2, padx=18, pady=18)

        self.submit.grid(row=7, columnspan=4, padx=25, pady=25)


    def doPredicit(self):
        if len(self.team1Entry.get()) == 0 | len(self.team2Entry.get()) == 0 | len(self.cityEntry.get()) == 0 | len(
                self.tossWinnerEntry.get()) == 0 | len(self.tossDecisionEntry.get()) == 0:
            print("please fill all entries")
        else:
            if self.tossDecisionEntry.get() != "bat" and self.tossDecisionEntry.get() != "field":
                print("please enter either bat or field in toss Decision Entry")
            else:
                self.result = startPrediction(self.team1Entry.get().capitalize(), self.team2Entry.get().capitalize(),
                                              self.cityEntry.get().capitalize(),
                                              self.tossWinnerEntry.get().capitalize(), self.tossDecisionEntry.get())
                print("Result : " + self.result)
                self.matchWinnerLabel = Label(self.master, text="Winner: " + self.result, fg='red', bg='black')
                self.matchWinnerLabel.grid(row=9, columnspan=4, padx=18, pady=18)
                self.winnerFont = ('times', 25, 'bold')
                self.matchWinnerLabel.config(font=self.winnerFont)


obj = match(root)
root.mainloop()
# ,command = self.doPredicit
