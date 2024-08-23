import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
canvas1 = tk.Canvas(root, width=500, height=300, bg='lightblue2', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text="Image Converter", bg='lightblue2', fg='white', font=('New Amsterdam', 20, 'bold'))
label1.config(font=('helvetica', 20))
canvas1.create_window(250, 100, window=label1)

def getPNG():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)

browse_png = tk.Button(text="Select PNG file", command=getPNG, bg="lightskyblue", fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(250, 150, window=browse_png)

def convert():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    im1.save(export_file_path)

saveasbutton = tk.Button(text="Convert PNG to JPG", command=convert, bg='lightskyblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(250, 200, window=saveasbutton)
root.mainloop()