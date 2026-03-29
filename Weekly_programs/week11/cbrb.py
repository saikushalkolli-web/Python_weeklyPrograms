#24331a05d8
import tkinter as ui
def show_details():
    print("User is interested in:")
    hobby=[]
    if h1.get():
        hobby.append("Reading")
    if h2.get():
        hobby.append("Dancing")
    if h3.get():
        hobby.append("Singing")
    for h in hobby:
        print(h)
    print("Gender: ",gender.get())
window=ui.Tk()
window.title("Data info")
window.geometry("700x300")
h1=ui.IntVar()
h2=ui.IntVar()
h3=ui.IntVar()
ui.Checkbutton(window,text="Reading",variable=h1).pack()
ui.Checkbutton(window,text="Singing",variable=h2).pack()
ui.Checkbutton(window,text="Dancing",variable=h3).pack()
gender=ui.StringVar()
ui.Radiobutton(window,text="MALE",variable=gender,value="Male").pack()
ui.Radiobutton(window,text="FEMALE",variable=gender,value="Feale").pack()
ui.Button(window,text="Show Details",command=show_details).pack()
window.mainloop()