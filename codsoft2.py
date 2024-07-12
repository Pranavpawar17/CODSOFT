import tkinter as tk
import string
import random

class PasswordGenerator:
    MAX_CHARS = 50
    MIN_CHARS = 3
    GRID_PADY = (10, 10)

    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("800x400")

        self.n_chars = tk.StringVar(self.master)

        self.create_widgets()

    def create_widgets(self):
        self.label_num_chars = tk.Label(self.master, text='Password Length:')
        self.entry_num_chars = tk.Entry(self.master, textvariable=self.n_chars, width=5)

        self.text_password_out = tk.Text(self.master, border=2, height=5, width=60)

        self.frame_buttons = tk.Frame()
        self.button_generate = tk.Button(self.frame_buttons, text='Generate', width=10, command=self.set_password)
        self.button_copy = tk.Button(self.frame_buttons, text='Copy', width=10, command=self.copy_password)
        self.button_reset = tk.Button(self.frame_buttons, text='Reset', width=10, command=self.reset_fields)
        self.button_close = tk.Button(self.frame_buttons, text='Close', command=self.master.quit, width=10)

        self.label_num_chars.grid(row=0, column=0, pady=self.GRID_PADY)
        self.entry_num_chars.grid(row=0, column=1)
        self.text_password_out.grid(row=1, column=0, columnspan=2, pady=self.GRID_PADY)
        self.button_generate.pack(side=tk.LEFT, padx=10)
        self.button_copy.pack(side=tk.LEFT, padx=10)
        self.button_reset.pack(side=tk.LEFT, padx=10)
        self.button_close.pack(side=tk.LEFT, padx=10)
        self.frame_buttons.grid(row=2, column=0, columnspan=2, pady=self.GRID_PADY)

    def set_password(self):
        try:
            n_chars = int(self.n_chars.get())
            if n_chars < self.MIN_CHARS or n_chars > self.MAX_CHARS:
                raise ValueError
        except ValueError:
            self.text_password_out.delete('1.0', tk.END)
            self.text_password_out.insert('1.0', "Invalid password length. Please enter a value between {} and {}".format(self.MIN_CHARS, self.MAX_CHARS))
            return

        chars = string.digits + string.ascii_letters
        password = ''.join(random.choices(chars, k=n_chars))
        self.text_password_out.delete('1.0', tk.END)
        self.text_password_out.insert('1.0', password)

    def copy_password(self):
        password = self.text_password_out.get('1.0', tk.END).strip()
        self.master.clipboard_clear()
        self.master.clipboard_append(password)

    def reset_fields(self):
        self.text_password_out.delete('1.0', tk.END)
        self.entry_num_chars.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    window = PasswordGenerator(root)
    root.mainloop()
