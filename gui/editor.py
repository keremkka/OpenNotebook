import customtkinter as ctk
import uuid
from backend.storage import load_notes, save_notes


class Editor(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color="#113232")
        self.pack(side="left", fill="both", expand=True)

        #title
        self.title = ctk.CTkEntry(self, fg_color="#052424", font=("Consolas", 14), height=30)
        self.title.pack(fill="x", expand=False, padx=20, pady=(20,0))

        #status label
        self.status_label = ctk.CTkLabel(self, text="", font=("Arial", 12), fg_color="#052424")
        self.status_label.pack(pady=(5, 0))
        
        #textbox
        self.textbox = ctk.CTkTextbox(self, fg_color="#052424" ,font=("Consolas", 14))
        self.textbox.pack(fill="both", expand=True, padx=20, pady=(10,20))

        #save button
        self.save_button = ctk.CTkButton(self, text="Save", fg_color="#264242", command=self.save_note)
        self.save_button.pack(pady=(0,20))

        #delete button
        self.delete_button = ctk.CTkButton(self, text="Delete", fg_color="#264242", command=self.delete_note)
        self.delete_button.pack(pady=(0,20))





        self.current_note_id = None




    def clear(self):
        self.textbox.delete("1.0","end")
        self.title.delete("0", "end")

    

    def save_note(self):
        title = self.title.get().strip()
        content = self.textbox.get("1.0", "end").strip()

        notes = load_notes()
        titles = [note["title"] for note in notes.values()]
        #print(titles)

        numbers = []
        for t in titles:
            if t.startswith("Note - "):
                try:
                    num = int(t.split("Note - ")[1])
                    numbers.append(num)

                except:
                    pass
        #print(numbers)


    


        if title == "":

            if numbers:
                next_number = max(numbers) + 1
            else:
                next_number = 1 

            #print("next: ", next_number)
            title = f"Note - {next_number}"
            self.title.insert(0, title)

        
        if self.current_note_id is None:
            #creat uuid
            note_id = str(uuid.uuid4())
            notes[note_id] = {
                "title": title,
                "content": content
            }
            self.current_note_id = note_id

        else:
            #update the uuid
            notes[self.current_note_id] = {
                "title": title,
                "content": content
            }

        save_notes(notes)

        self.show_status("Saved ✔")

        self.master.sidebar.refresh_notes()




    def delete_note(self):

        if self.current_note_id is None:
            self.clear()
            self.show_status("Page Cleared")

            return
        
        if self.current_note_id is None:
            self.show_status("No Note Selected")

            return

        notes = load_notes()

        if self.current_note_id in notes:
            del notes[self.current_note_id]
            save_notes(notes)

        self.current_note_id = None
        self.clear()
        self.master.sidebar.refresh_notes()

        self.show_status("Deleted 🗑")


    def show_status(self, message):
        self.status_label.configure(text=message)
        self.status_label.after(2000, lambda: self.status_label.configure(text=""))
