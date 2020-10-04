from tkinter import Label, Entry, Button, Tk, filedialog, messagebox, END, IntVar, Radiobutton
from PIL import Image, ImageTk
from Img8Bits import Img8Bits
from os import path
import time

'''
    GUI with tkinter for easier use without the command line
    by Juan S. Marquerie
'''

VERSION = '0.65'

'''
    This requeires a bit of an explanation... While I was doing
    my first Android App project, I added as a background a really no good,
    ugly green to orange gradient; and del_cieno critisized and mocked
    endlessly this choice...
    In hindshight, this was for the better, but I can still have some fun
    with this...
'''
HORRIBLE_BACKGROUND = True

resizer = Img8Bits()

def define_GUI(tk_window):
    # Window Config
    tk_window.title('Image Bitsizer Utility v ' + VERSION)
    tk_window.geometry('650x100')

    selected_bit_depth = IntVar()

    if HORRIBLE_BACKGROUND:
        back_img = ImageTk.PhotoImage(Image.open('imgs/background.jpg'))
        back = Label(tk_window, image=back_img)
        back.place(x=0, y=0, relwidth=1, relheight=1)
        back.image = back_img

    # Labels
    label_folder_origin = Label(tk_window, text='Enter the texture pack/origin folder')
    label_folder_origin.grid(column=0, row=0)
    label_resolution = Label(tk_window, text='Bit depth')
    label_resolution.grid(column=3, row=0)
    label_resolution = Label(tk_window, text='Enter the resulting texture direction')
    label_resolution.grid(column=7, row=0)

    # Text Input
    txt_direction_input = Entry(tk_window, width=25)
    txt_direction_input.grid(column=0, row=1)
    txt_result_direction_input = Entry(tk_window, width=25)
    txt_result_direction_input.grid(column=7, row=1)

    # Radio button
    r1 = Radiobutton(tk_window, text="32 bits", variable=selected_bit_depth, value=32)
    r1.grid(column=3, row=1)
    r1 = Radiobutton(tk_window, text="16 bits", variable=selected_bit_depth, value=16)
    r1.grid(column=3, row=2)
    r1 = Radiobutton(tk_window, text="8 bits", variable=selected_bit_depth, value=8)
    r1.grid(column=3, row=3)


    # Button Events
    def launch_item_search():
        selected_folder = filedialog.askdirectory()
        txt_direction_input.delete(0, END)
        txt_direction_input.insert(0,selected_folder)

    def launch_search_result_folder():
        selected_folder = filedialog.askdirectory()
        txt_result_direction_input.delete(0, END)
        txt_result_direction_input.insert(0,selected_folder)

    def resize():
        button_resize.configure(state='disabled', text='Resizing...')
        tk_window.update()

        bit_depth = selected_bit_depth.get()

        resizer.change_directory(txt_direction_input.get(), txt_result_direction_input.get(), bit_depth)
        messagebox.showinfo('BitDepth changing Utility', 'Finished resizing!')
        button_resize.configure(state='normal', text='Resize')
        tk_window.update()


    # Buttons
    button_search = Button(tk_window, text='Search', command=launch_item_search)
    button_search.grid(column=1, row=1)
    button_search_2 = Button(tk_window, text='Search', command=launch_search_result_folder)
    button_search_2.grid(column=8, row=1)
    button_resize = Button(tk_window, text='Resize', command=resize)
    button_resize.grid(column=5, row=6)


'''
    Launch the GUI
'''
if __name__ == '__main__':
    window = Tk()
    define_GUI(window)
    window.mainloop()
