from tkinter import *
from tkinter import filedialog

import demo

app = Tk()
filename=''
count=0

def choosefile():
    filename = filedialog.askopenfilename(initialdir = "~",title = "Select file",filetypes = (("mp3 files","*.mp3"),("wav files","*.wav")))
    print (filename)
    enterText.insert(0, filename)

def clear():
    global count
    if count>0:
        list=app.pack_slaves()
        #print (list[-1])
        list[-1].destroy()
    count+=1
    enterText.delete(0,'end')

def predictFile():
    #print(enterText.get()) 
    if enterText.get()=='':
        outText="Cannot Find the given file"
    else:
        result = demo.predictor(enterText.get())
        outText = "The Predicted instrument is "
        if result == 1:
            outText += "cello."
        elif result == 2:
            outText += "clarinet."
        elif result == 3:
            outText += "flute."
        elif result == 4:
            outText += "violin."
        elif result == 5:
            outText += "piano."

    clear()        
    output=Label(app,text=outText, font=('normal',14), padx=15, pady=15)
    output.pack(padx = 10,pady = 10)




title = Label(app, text = "INSTRUMENT DETECTOR", font = ('bold', 18), padx = 15, pady = 15)
title.pack(side = TOP)

enterLabel = Label(app, text = "Enter file name", font = ('normal', 14), padx = 5, pady = 20)
enterLabel.pack(padx = 10,pady = 10)

enterText = Entry(app, textvariable = filename)
chooseButton = Button(app, text = 'Choose file', command = choosefile)
enterText.pack(padx = 10,pady = 10)
chooseButton.pack(padx = 10,pady = 10)

predictButton = Button(app, text = 'Predict', command = predictFile)
predictButton.pack(padx = 10,pady = 10)




app.title("Instrument detector")
app.geometry('800x400')

app.mainloop()