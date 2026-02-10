import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(width=200, fg_color="#3A1E5E")
        self.pack(side="left", fill="y")


        #title
        self.title = ctk.CTkLabel(self, text="MENU", font=("Arial", 18, "bold"))
        self.title.pack(pady=(20,10))

        #buttons
        self.btn =ctk.CTkButton(self, text="Editors", fg_color="#1B0B21")
        self.btn.pack(pady=10, padx= 20, fill="x")

        self.btn_settings = ctk.CTkButton(self, text="settings")
        self.btn.pack(pady=10, padx=20, fill="x")

        #notes label
        label = ctk.CTkLabel(self, text="Notes")
        label.pack(padx=20, pady=20)

