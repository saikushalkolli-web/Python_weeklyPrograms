#24331a05d8
import tkinter as ui
window=ui.Tk()
window.geometry("700x300")
text=ui.Label(window,text="Using pack()")
text.pack()
frame1=ui.Frame(window)
frame1.pack()
grid1=ui.Label(frame1,text="Placed using grid")
grid1.grid(row=9,column=4)
btn=ui.Button(window,text="click here")
btn.place(x=129,y=99)
window.mainloop()