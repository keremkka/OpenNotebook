import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(width=200, fg_color="#264242")
        self.pack(side="left", fill="y")


        #title
        self.title = ctk.CTkLabel(self, text="MENU", font=("Arial", 18, "bold"))
        self.title.pack(pady=(20,10))

        #buttons
        self.btn_editor =ctk.CTkButton(self, text="New Note", fg_color="#052424", command=self.new_note)
        self.btn_editor.pack(pady=10, padx= 20, fill="x")

        self.btn_settings = ctk.CTkButton(self, text="settings", fg_color="#052424")
        self.btn_settings.pack(pady=10, padx=20, fill="x")

        #notes label
        label = ctk.CTkLabel(self, text="Notes")
        label.pack(padx=20, pady=20)

    def new_note(self):
        self.master.editor.clear()

