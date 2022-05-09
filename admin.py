import tkinter as tk
from tkinter import Frame, ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pyAesCrypt


# create the root window
root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.title('Gyan Shaala Docs')
root.resizable(False, False)
#root.geometry('800x300')
root.option_add("*Font","Cambria")
frame = Frame(root)
frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
frame.pack_propagate(0)
newFileName=""
filename=""

def select_file():
    global filename

    filetypes = (
        ('pdf files', '*.pdf'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    if filename==""   :
        showinfo("Warning","No file selected...")
    else:
        label1.configure(text="Selected File is : ")
        label2.configure(text=filename)
        textbox1.config(state='enabled')
        textbox2.config(state='enabled')
        enc_button.config(state='enabled')
        dec_button.config(state='enabled')

def enc_file():
    
    global filename
    global newFileName
    global encPass

    lastname = filename.split("/")[-1]
    password = textbox1.get()
    if password=="":
        showinfo("Warning","Enter password...")
    else:
        newName = "/Encrypted_"+lastname
        filePathList = filename.split("/")[:-1]
        filePathString = '/'.join(filePathList)
        newFileName = filePathString+newName
        pyAesCrypt.encryptFile(filename, newFileName, password)
        encPass.set("")
        showinfo("Success",message="Successfully encrypted")

def dec_file():
    global decPass
    global filename
    global newFileName
    lastname = filename.split("/")[-1]
    password = textbox2.get()
    if password=="":
        showinfo("Warning","Enter password...")
    else:
        newName = "/Decrypted_"+lastname
        filePathList = filename.split("/")[:-1]
        filePathString = '/'.join(filePathList)
        newFileName = filePathString+newName
        pyAesCrypt.decryptFile(filename, newFileName, password)
        decPass.set("")
        showinfo("Success",message="Successfully decrypted")

# open button
open_button = ttk.Button(
    frame,
    text='Select PDF',
    command=select_file
)

enc_button = ttk.Button(
    frame,
    text='Encrypt File',
    command=enc_file,
    state='disabled'
)

dec_button = ttk.Button(
    frame,
    text='Decrypt File',
    command=dec_file,
    state='disabled'
)




open_button.grid(row=2, column=1, padx=10, pady=10,ipadx=10, ipady=10)

label1 = ttk.Label(frame,text="",width=20)
label1.grid(row=3,column=0, padx=10, pady=10)

label2 = ttk.Label(frame,text="", width=60)
label2.grid(row=3,column=1, padx=10, pady=10)

encPass = tk.StringVar()
textbox1 = ttk.Entry(frame, textvariable=encPass, show='*', state='disabled', width=50)
textbox1.grid(row=6, column=1, padx=10, pady=10)

decPass = tk.StringVar()
textbox2 = ttk.Entry(frame, textvariable=decPass, show='*', state='disabled', width=50)
textbox2.grid(row=7, column=1, padx=10, pady=10)

label3 = tk.Label(frame,text="Enter Password to Encrypt").grid(row=6,column=0)
enc_button.grid(row=6,column=2, padx=10, pady=10)

label4 = tk.Label(frame,text="Enter Password to Decrypt").grid(row=7,column=0)
dec_button.grid(row=7, column=2, padx=10, pady=10)

# run the application
root.mainloop()
