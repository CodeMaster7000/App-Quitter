from tkinter import *

root = Tk()
root.title("App Force Quitter")
label = Label(root, text="App Force Quitter", font=("Arial", 26))
label.pack()
blank_label = Label(root, text="")
blank_label.pack()
app_entry = Entry(root, width=100, borderwidth=5)
app_entry.pack()
app_entry.insert(0, "Enter name of app you wish to force quit:")

def force_quit():
    app_name = app_entry.get()
    os.system(f"taskkill /f /im {app_name}.exe")

    messagebox.showinfo(f"{app_name} has been force quitted.")

execute_button = Button(root, text="Force Quit", command=force_quit)
execute_button.pack()

root.mainloop()
