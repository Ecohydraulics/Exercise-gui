import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo
from tkinter.filedialog import askopenfilename, askdirectory
import webbrowser
import sediment_transport as sed


class SediApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

    def run_program(self):
        pass

    def set_grain_file(self):
        pass

    def set_hec_file(self):
        pass

    def select_out_directory(self):
        pass

    def select_file(self, description, file_type):
        pass

    def valid_selections(self):
        pass


if __name__ == '__main__':
    pass
