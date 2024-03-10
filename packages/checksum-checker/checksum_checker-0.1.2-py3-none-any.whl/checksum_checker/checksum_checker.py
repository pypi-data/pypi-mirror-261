#! /usr/bin/python3
import hashlib
import tkinter as tk
import tkinter.filedialog as tkfd
from tkinter import Label, W, GROOVE, DISABLED, NORMAL, StringVar, IntVar

root = tk.Tk()
check_btn = tk.Button(root)
var0 = StringVar()
var1 = StringVar()
algo_ = IntVar()
h_ = hashlib.sha512()
dialog_ = tkfd.FileDialog
path_field_set_ = False

def set_algo():
    '''Set algorithm'''
    global h_
    if algo_ == 1:
        h_ = hashlib.sha512()
    elif algo_ == 2:
        h_ = hashlib.md5()
    elif algo_ == 3:
        h_ = hashlib.sha1()


def open_dialog():
    '''Open dialog'''
    global dialog_
    dialog_ = tkfd.askopenfilename()
    var0.set(dialog_)
    global path_field_set_
    path_field_set_ = True


def print_result(h):
    '''Print result after comparing if hashes are equal'''
    label_list = []
    if h.hexdigest() == var1.get().strip():
        label_list.append(Label(root, text="MATCH", bg='palegreen'))
        label_list[0].grid(row=10, column=1)
    else:
        label_list.append(Label(root, text="NO MATCH", bg='red'))
        label_list[0].grid(row=10, column=1)
    label_list.append(Label(root, text='<-- calculated', bg='floralwhite', fg='black'))
    label_list[1].grid(row=11, column=2)
    label_list.append(Label(root, text='<-- given     ', bg='floralwhite', fg='black'))
    label_list[2].grid(row=12, column=2)
    label_list.append(Label(root, text=h.hexdigest()))
    label_list[3].grid(row=11, column=1)
    label_list.append(Label(root, text=var1.get().strip()))
    label_list[4].grid(row=12, column=1)
    check_btn.config(state='disabled')
    reset_btn = tk.Button(root, text="RESET", relief=GROOVE, font="Helvetica 15")
    reset_btn.configure(command=lambda btn=reset_btn: reset_gui(label_list, btn))
    reset_btn.grid(row=13, column=1)
    
    
def reset_gui(label_list, reset_btn):
    '''Reset the GUI'''
    var0.set('')
    var1.set('')
    root.after(1, reset_btn.destroy)
    for element in label_list:
        root.after(1, element.destroy)
    check_btn.config(state=NORMAL)

def calculate_checksum():
    '''Calculate checksum after reading the file (binary)'''
    if path_field_set_:
        with open(dialog_, 'rb') as file:
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h_.update(chunk)
        print_result(h_)
    else:
        Label(root, text="WARNING: choose a file!")
        print(path_field_set_)
        

 # Start of main routine 
def checksum_checker_gui():
    root.title("Checksum Checker")
    root.configure(background='floralwhite')
    
    path_label = Label(root, bg='floralwhite', fg='black', relief=GROOVE, text="1) Choose file from file system   ")
    path_label.grid(row=0, column=0, sticky=W)
    
    var0.set('')
    path_field = tk.Entry(root, textvariable=var0, width=80, exportselection=1)
    path_field.config(state=DISABLED)
    path_field.grid(row=0, column=1)
    
    hash_label = Label(root, bg='floralwhite', fg='black', relief=GROOVE, text="2) Enter given checksum             ")
    hash_label.grid(row=1, column=0, sticky=W)
    
    var1.set('')
    hash_field = tk.Entry(root, textvariable=var1, width=80, exportselection=1)
    hash_field.grid(row=1, column=1)
    hash_field.focus_force()
    
    algo_.set(1)
    algo_label = Label(root, bg='floralwhite', fg='black', relief=GROOVE, text="3) Choose Algorithm                    ")
    algo_label.grid(row=3, column=0, sticky=W)
    tk.Radiobutton(root, text="SHA-512", bg='floralwhite', fg='black', variable=algo_, value=1, command=set_algo).grid(row=4, column=1, sticky=W)
    tk.Radiobutton(root, text="MD5", bg='floralwhite', fg='black', variable=algo_, value=2, command=set_algo).grid(row=5, column=1, sticky=W)
    tk.Radiobutton(root, text="SHA1", bg='floralwhite', fg='black', variable=algo_, value=3, command=set_algo).grid(row=6, column=1, sticky=W)
    
    tk.Button(root, text="File \u23f6", relief=GROOVE, command=open_dialog).grid(row=0, column=2)
    check_btn = tk.Button(root, text="\u24d2 \u24d7 \u24d4 \u24d2 \u24da", relief=GROOVE, font="Helvetica 15", command=calculate_checksum)
    check_btn.grid(row=8, column=1)
    
    root.mainloop()

