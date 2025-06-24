from tkinter import Tk, Label, Button, Text, Frame, END, BOTH, X, Y, Scrollbar, RIGHT, LEFT, TOP, BOTTOM
from tkinter import font as tkfont
from Encrypt import encrypt_message
from decrypt import decrypt_message

class LoremEncryptorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Lorem Ipsum Encryptor/Decryptor")
        master.configure(bg="#f5f5f5")
        master.geometry("650x500")
        master.resizable(False, False)

        title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
        label_font = tkfont.Font(family="Helvetica", size=12)
        button_font = tkfont.Font(family="Helvetica", size=11, weight="bold")

        # Title
        self.title_label = Label(master, text="Lorem Ipsum Encryptor/Decryptor", font=title_font, bg="#f5f5f5", fg="#333")
        self.title_label.pack(pady=(20, 10))

        # Input Frame
        input_frame = Frame(master, bg="#f5f5f5")
        input_frame.pack(padx=20, pady=10, fill=X)

        self.label = Label(input_frame, text="Enter your text:", font=label_font, bg="#f5f5f5")
        self.label.pack(anchor="w")

        self.text_input = Text(input_frame, height=6, width=70, font=("Consolas", 11), wrap="word", bd=2, relief="groove")
        self.text_input.pack(pady=5)

        # Button Frame
        button_frame = Frame(master, bg="#f5f5f5")
        button_frame.pack(pady=10)

        self.encrypt_button = Button(button_frame, text="Encrypt", font=button_font, bg="#4CAF50", fg="white", width=12, command=self.encrypt_text)
        self.encrypt_button.pack(side=LEFT, padx=10)

        self.decrypt_button = Button(button_frame, text="Decrypt", font=button_font, bg="#2196F3", fg="white", width=12, command=self.decrypt_text)
        self.decrypt_button.pack(side=LEFT, padx=10)

        self.clear_button = Button(button_frame, text="Clear", font=button_font, bg="#f44336", fg="white", width=12, command=self.clear_text)
        self.clear_button.pack(side=LEFT, padx=10)

        # Output Frame
        output_frame = Frame(master, bg="#f5f5f5")
        output_frame.pack(padx=20, pady=10, fill=BOTH, expand=True)

        self.result_label = Label(output_frame, text="Result:", font=label_font, bg="#f5f5f5")
        self.result_label.pack(anchor="w")

        self.result_text = Text(output_frame, height=8, width=70, font=("Consolas", 11), wrap="word", bd=2, relief="groove", state='disabled')
        self.result_text.pack(pady=5, fill=BOTH, expand=True)

        # Scrollbar for output
        scrollbar = Scrollbar(self.result_text)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.result_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)

    def encrypt_text(self):
        input_text = self.text_input.get("1.0", END).strip()
        encrypted_text = encrypt_message(input_text)
        # Ensure words are separated by spaces
        encrypted_text = ' '.join(encrypted_text.split())
        self.display_result(encrypted_text)

    def decrypt_text(self):
        input_text = self.text_input.get("1.0", END).strip()
        decrypted_text = decrypt_message(input_text)
        # Ensure words are separated by spaces
        decrypted_text = ' '.join(decrypted_text.split())
        self.display_result(decrypted_text)

    def display_result(self, result):
        self.result_text.config(state='normal')
        self.result_text.delete("1.0", END)
        self.result_text.insert(END, result)
        self.result_text.config(state='disabled')

    def clear_text(self):
        self.text_input.delete("1.0", END)
        self.result_text.config(state='normal')
        self.result_text.delete("1.0", END)
        self.result_text.config(state='disabled')

if __name__ == "__main__":
    root = Tk()
    gui = LoremEncryptorGUI(root)
    root.mainloop()