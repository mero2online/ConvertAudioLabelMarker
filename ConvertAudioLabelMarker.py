from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import os

from settings import appVersionNo
from ConvertLabel import ConvertLabel
from ConvertMarker import ConvertMarker
from HelperFunc import resource_path

try:
    import pyi_splash  # type: ignore
    pyi_splash.close()
except:
    pass

filetypes = (
    ('Label or Marker', ['*.txt', '*.csv']),
    # ('All files', '*.*'),
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

root.title(f'ConvertAudioLabelMarker {appVersionNo}')
root.geometry('500x300')
root.configure(bg='#000')

root.resizable(False, False)

root.iconbitmap(resource_path('label_icon.ico'))

# Start program
root.mainloop()
