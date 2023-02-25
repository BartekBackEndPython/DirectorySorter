import Engine
import tkinter
import time
import os 

window = tkinter.Tk()
window.title("BarPek Directory Sorter Engine ALFA0.0")
window.geometry("750x750")
window.resizable(False, False)
window.configure(background="#404040")

textFieldLabel = tkinter.Label(text="-Type directory path here-", font=("bebas", 24), bg="#404040", fg="#0000FF")
textFieldLabel.place(relx=0.5, rely=0.035, anchor="center")

textField = tkinter.Entry(font=("arial", 24), bg="#404040", fg="#0000FF")
textField.place(relx=0.5, rely=0.1, anchor="center")

infoText = tkinter.Label(text="Nothing here yet", font=("bebas", 15), bg="#404040", fg="#0000FF")
infoText.place(relx=0.5, rely=0.55, anchor="center")


def reset_info_field():
    infoText.config(text="Nothing here again?", fg="#0000FF")

def reset_text():
    textField.delete(0, tkinter.END)


on_doing = [False]


def sort_folder_(event=None):
    if on_doing[0]:
        infoText.config(text="Other directory is sorting", fg="#CC0000")
        window.after(3000, reset_info_field)
    else:
        if os.path.exists(textField.get()):
            on_doing[0] = True
            infoText.config(text=". . .")
            Engine.Engine.sort_folder(Engine.Formater.format_path(textField.get()))
            time.sleep(2)
            infoText.config(text="Directory is sorted", fg="#009900")
            reset_text()
            on_doing[0] = False
            window.after(3000, reset_info_field)
        else:
            infoText.config(text="Path does not exist", fg="#CC0000")
            reset_text()
            window.after(3000, reset_info_field)

sortButton = tkinter.Button(text="SORT", font=("bebas", 30), bg="#00FFFF", fg="#FFFFFF", command=sort_folder_)
sortButton.place(relx=0.5, rely=0.3, anchor="center")

window.bind("<Return>", sort_folder_)

window.mainloop()