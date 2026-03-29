import tkinter as ui
from tkinter import messagebox, filedialog
def show(choice):
    output1.config(text=f"You selected: {choice}")
def open_file():
    filename = filedialog.askopenfilename(title="Open a file")
    if filename:
        messagebox.showinfo("File Selected", f"You chose: {filename}")
def on_select(event):
    selected = listbox.get(listbox.curselection())
    messagebox.showinfo("ListBox Selection", f"You selected: {selected}")
window = ui.Tk()
window.title("GUI Application Demo")
window.geometry("700x400")
menu1 = ui.Menu(window)
f1 = ui.Menu(menu1, tearoff=1)
f1.add_command(label="New", command=lambda: show("New"))
f1.add_command(label="Open File", command=open_file)
f1.add_command(label="Exit", command=window.quit)
menu1.add_cascade(label="File", menu=f1)
window.config(menu=menu1)
mbtn = ui.Menubutton(window, text="Options")
menu = ui.Menu(mbtn, tearoff=1)
menu.add_command(label="Option1", command=lambda: show("Hii"))
menu.add_command(label="Option2", command=lambda: show("Byeee!!"))
mbtn.config(menu=menu)
mbtn.pack(pady=10)
output1 = ui.Label(window, text="Your choice will appear here...")
output1.pack(pady=20)
frame = ui.Frame(window)
frame.pack(pady=10)
scrollbar = ui.Scrollbar(frame)
scrollbar.pack(side=ui.RIGHT, fill=ui.Y)
listbox = ui.Listbox(frame, yscrollcommand=scrollbar.set, height=5)
items = ["Lakers", "Celtics", "Bulls", "Mavericks", "Warriors", "Clippers", "Kings"]
for item in items:
    listbox.insert(ui.END, item)
listbox.pack(side=ui.LEFT, fill=ui.BOTH)
scrollbar.config(command=listbox.yview)
listbox.bind("<<ListboxSelect>>", on_select)
window.mainloop()