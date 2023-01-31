from tkinter import *;
from tkinter import ttk;
from PIL import ImageTk,Image 
import csv;
from cat import cat;


def main_loop():
    print("main loop accessable")
    
def new_game():
    print("new game works");
    main_loop();
def continue_game():
    print("continue game doesnt work")
    main_loop();



root = Tk();
root.title('cat quest');
root.resizable(False, False)
frm = ttk.Frame(root, padding=10);
frm.grid();
image = Image.open("img/main_menu_img.png")
photo = ImageTk.PhotoImage(image)
label = Label(root, image = photo)
label.image = photo
label.grid(row=1)
ttk.Label(frm, text="CAT QUEST!").grid(column=1, row=0);
ttk.Button(frm, text="new game", command=new_game).grid(column=0, row=2);
ttk.Button(frm, text="continue game", command=continue_game).grid(column=1, row=2);
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=2)


root.mainloop();


