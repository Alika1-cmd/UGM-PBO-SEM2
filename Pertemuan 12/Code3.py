from tkinter import Tk, Label, Button, Entry, Text, Frame, Canvas, END

class BirthdayApp:
    def __init__(self, master):
        self.master = master
        master.title("Ucapan Ulang Tahun")

        # Hiasan
        self.canvas = Canvas(master, width=300, height=100, bg="Whitw")
        self.canvas.create_text(150, 50, text="=== Happy Birthday ===", font=("Arial", 16, "bold"), fill="Violet")
        self.canvas.pack(pady=10)

        # Frame Utama 
        self.frame = Frame(master)
        self.frame.pack(pady=10)

        # Label dan Entry
        self.label = Label(self.frame, text="Masukkan nama:")
        self.label.grid(row=0, column=0, padx=5)

        self.name_entry = Entry(self.frame, width=25)
        self.name_entry.grid(row=0, column=1, padx=5)

        # Tombol
        self.button = Button(master, text="Hadiah Untukmu!", command=self.show_message, bg="White")
        self.button.pack(pady=5)

        # Text Output
        self.output_text = Text(master, height=3, width=40, font=("Arial", 12))
        self.output_text.pack(pady=10)

    def show_message(self):
        name = self.name_entry.get()
        if name.strip():
            message = f"Selamat ulang tahun {name}!\nSemoga sehat selalu :)"
        else:
            message = "Silakan masukkan nama terlebih dahulu."

        self.output_text.delete("1.0", END)
        self.output_text.insert(END, message)

root = Tk()
app = BirthdayApp(root)
root.mainloop()
