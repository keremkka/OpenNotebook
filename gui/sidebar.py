import customtkinter as ctk
from backend.storage import load_notes



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

        #settings
        self.btn_settings = ctk.CTkButton(self, text="Settings", fg_color="#052424")
        self.btn_settings.pack(pady=10, padx=20, fill="x")

        #notes label
        label = ctk.CTkLabel(self, text="Notes")
        label.pack(padx=20, pady=(20,10))


        #slidebar
        self.notes_frame = ctk.CTkScrollableFrame(self, width=100, fg_color="#113232")
        self.notes_frame.pack(fill="both", expand=True, padx=10, pady=(0,20))

        self.refresh_notes()




    def new_note(self):
        self.master.editor.clear()



    def refresh_notes(self):
        for widget in self.notes_frame.winfo_children():
            widget.destroy()

        notes = load_notes()

        for note_id, data in notes.items():
            title = data["title"]

            btn = ctk.CTkButton(
                self.notes_frame,
                text=title,
                fg_color="#052424",
                command=lambda i=note_id: self.open_note(i)
            )

            btn.pack(fill="x", pady=5)




    def open_note(self, note_id):
        notes = load_notes()
        note = notes[note_id]

        self.master.editor.title.delete(0, "end")
        self.master.editor.textbox.delete("1.0", "end")

        self.master.editor.title.insert(0, note["title"])
        self.master.editor.textbox.insert("1.0", note["content"])


