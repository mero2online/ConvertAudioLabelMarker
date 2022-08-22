from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import os

from ConvertLabel import ConvertLabel
from ConvertMarker import ConvertMarker

filetypes = (
    ('All files', '*.*'),
)


def browseFile():
    # open-file dialog
    filename = filedialog.askopenfilename(
        title='Select a file...',
        filetypes=filetypes,)
    pathOnly, file_extension = os.path.splitext(filename)
    if file_extension == '.txt':
        ConvertLabel(filename)
    if file_extension == '.csv':
        ConvertMarker(filename)


root = Tk()

browseBtn = Button(root, text="Browse File", background='#633192', foreground='#faebd7',
                   borderwidth=2, relief="raised", padx=5, pady=5,
                   command=browseFile)
browseBtn.place(x=5, y=5, width=100, height=37)

root.title('ConvertAudioLabelMarker')
root.geometry('500x300')
root.configure(bg='#000')

root.resizable(False, False)

# Start program
root.mainloop()
