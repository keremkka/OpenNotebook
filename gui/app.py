import customtkinter as ctk
from gui.sidebar import Sidebar
from gui.editor import Editor

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #window settings:
        self.title("ONB")
        self.geometry("900x600")

        self.sidebar = Sidebar(self)
        self.editor = Editor(self)


