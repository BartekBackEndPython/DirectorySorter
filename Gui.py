import Engine
import constants

import tkinter
import time
import os 

window = tkinter.Tk()
window.title(f"{constants.APP.NAME} {constants.APP.VERSION}")
window.geometry(constants.WINDOW.SIZE)
window.resizable(False, False)
window.configure(bg=constants.WINDOW.BACKGROUND)

textFieldLabel = tkinter.Label(text="-Type directory path here-", font=("bebas", 24), bg=constants.WINDOW.BACKGROUND, fg="#0000FF")
textFieldLabel.place(relx=0.5, rely=0.035, anchor="center")

textField = tkinter.Entry(font=("arial", 24), bg=constants.WINDOW.BACKGROUND, fg="#0000FF")
textField.place(relx=0.5, rely=0.1, anchor="center")

infoText = tkinter.Label(text="Nothing here yet", font=("bebas", 15), bg="#404040", fg="#0000FF")
infoText.place(relx=0.5, rely=0.55, anchor="center")


def reset_info_field():
    infoText.config(text="Nothing here again?", fg="#0000FF")

    
def reset_text():
    textField.delete(0, tkinter.END)

    
on_doing = False


def sort_folder_(event=None):
    global on_doing
    if on_doing:
        infoText.config(text="Other directory is sorting", fg="#CC0000")
        window.after(3000, reset_info_field)
    else:
        if os.path.exists(textField.get()) and os.path.isdir(textField.get()):
            global on_doing
            on_doing = True
            infoText.config(text=". . .")
            Engine.Engine.sort_folder(Engine.Formater.format_path(textField.get()))
            time.sleep(2)
            infoText.config(text="Directory is sorted", fg="#009900")
            reset_text()
            on_doing = False
        else:
            infoText.config(text="Path does not exist or path is not directory", fg="#CC0000")
            reset_text()
            
        window.after(3000, reset_info_field)


sortButton = tkinter.Button(text="SORT", font=("bebas", 30), bg="#00FFFF", fg="#FFFFFF", command=sort_folder_)
sortButton.place(relx=0.5, rely=0.3, anchor="center")

window.bind("<Return>", sort_folder_)


def mainloop():
    if os.path.exists(textField.get()) and os.path.isdir(textField.get()):
        sortButton.config(bg="green")
    else:
        sortButton.config(bg="#00FFFF")

    window.after(10, mainloop)


window.after(10, mainloop)
window.mainloop()
