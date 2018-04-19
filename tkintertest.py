import os
import tkinter as tk
from tkinter import filedialog, Button, Label, Entry, Frame, END, X, StringVar
import csv
import pandas as pd
import numpy as np
from datetime import datetime



content = ''
filepath = ''


# Function to select csv file

def open_file():
    global content
    global filepath
    filename = filedialog.askopenfilename(filetypes = [(".csv files", "*.csv")])
    content = pd.read_csv(filename,encoding = 'utf-8')
    filepath = os.path.dirname(filename) + "/" + os.path.basename(filename)
    entry.delete(0, END)
    entry.insert(0, filepath)
    return content

# Function to process csv file

def process_file(content):
    df = content
    df['Time'] = pd.to_datetime(df['Time'], format = '%m/%d/%Y %H:%M:%S')
    df['Time2'] = df['Time'].where(df['Device'].str.contains('Turnstile Out')).shift(-1)
    df['TimeDiff'] = (df['Time'] - df['Time2']).astype('timedelta64[h]')
    df = df.set_index("Device")
    df = df.drop("Turnstile Out", axis = 0)
    df.to_csv('output5.csv', columns = ['Personnel Record','Time','Time2','TimeDiff', 'Credential'])

# GUI

root = tk.Tk()
root.title('CSV Reformatter')
root.geometry("550x120+250+100")

mf = Frame(root)
mf.pack()


f1 = Frame(mf, width = 500, height = 250)
f1.pack(fill = X)
f2 = Frame(mf, width = 500, height = 250)
f2.pack()

filepath = StringVar


Label(f1,text = "Select a .csv file").grid(row = 0, column = 0, sticky = 'e')
entry = Entry(f1, width = 50, textvariable = filepath)
entry.grid(row = 0, column = 1, padx = 2, pady = 2, sticky = 'we', columnspan = 25)
Button(f1, text = "Browse", command = open_file).grid(row = 0, column = 27, sticky = 'ew', padx = 8, pady = 4)
Button(f2, text = "Process Now", width = 32, command = lambda: process_file(content)).grid(sticky = 'ew', padx = 10, pady = 10)

root.mainloop()
