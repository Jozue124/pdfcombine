from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import filedialog

def merge(pdfs):
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write("result.pdf")
    merger.close()

def get_file_path(pdfs):
    file_path = filedialog.askopenfilename()
    pdfs.append(file_path)
    return file_path

def main():
    
    #initialize stuff
    pdfs = []
    pdflabels = []
    window = tk.Tk()

    
    #create content of window
    ab = tk.Button(window,text="Add pdf",command=(lambda:get_file_path(pdfs)))
    for pdf in pdfs:
        label = Label(window, textvariable=pdf, relief=RAISED)
        pdflabels.append(label)
    mb = tk.Button(window,text="Merge pdfs",command=(lambda:merge(pdfs)))
    #add content to window
    for label in pdflabels:
        label.pack()
    mb.pack()
    ab.pack()

    #run window
    window.geometry("500x200")
    window.mainloop()

    for pdf in pdfs:
        print(pdf)


if __name__ == "__main__":
    main()
