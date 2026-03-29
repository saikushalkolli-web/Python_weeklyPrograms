#24331a05d8
import tkinter as ui
window=ui.Tk()
window.geometry("700x300")
l1=ui.Label(window,text="Enter a word: ")
l1.pack()
entry=ui.Entry(window)
entry.pack()
def texting():
    text=entry.get()
    print("You entered",text)
btn=ui.Button(window,text="Submit",command=texting)
btn.pack()
window.mainloop()