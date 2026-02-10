import customtkinter as ctk

class Editor(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color="#1B0B21")
        self.pack(side="left", fil="both", expand=True)

