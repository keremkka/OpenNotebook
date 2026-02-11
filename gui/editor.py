import customtkinter as ctk
from backend.storage import load_notes, save_notes


class Editor(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color="#113232")
        self.pack(side="left", fill="both", expand=True)

        #title
        self.title = ctk.CTkEntry(self, fg_color="#052424", font=("Consolas", 14), height=30)
        self.title.pack(fill="x", expand=False, padx=20, pady=(20,0))

        #textbox
        self.textbox = ctk.CTkTextbox(self, fg_color="#052424" ,font=("Consolas", 14))
        self.textbox.pack(fill="both", expand=True, padx=20, pady=(10,20))

        #save button
        self.save_button = ctk.CTkButton(self, text="Save", fg_color="#264242", command=self.save_note)
        self.save_button.pack(pady=(0,20))




    def clear(self):
        self.textbox.delete("1.0","end")
        self.title.delete("0", "end")

    

    def save_note(self):
        title = self.title.get().strip()
        content = self.textbox.get("1.0", "end").strip()

        if title == "":
            print("Title is Empty")
            return
        
        notes = load_notes()
        notes[title] = content
        save_notes(notes)

        print("SAVED")
