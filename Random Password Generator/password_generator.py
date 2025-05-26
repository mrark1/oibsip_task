import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import json
import os
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("550x500")
        self.root.resizable(False, False)

        try:
            self.root.iconbitmap(os.path.join("assets", "icon.ico"))
        except:
            pass

        self.password_history = []
        self.load_history()

        self.setup_styles()
        self.create_widgets()
        self.update_history_listbox()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#f8f9fa')
        style.configure('TLabel', background='#f8f9fa', font=('Arial', 10))
        style.configure('Header.TLabel', font=('Arial', 16, 'bold'))
        style.configure('TButton', font=('Arial', 10))

        style.configure('red.Horizontal.TProgressbar', background='red')
        style.configure('yellow.Horizontal.TProgressbar', background='orange')
        style.configure('green.Horizontal.TProgressbar', background='green')

    def create_widgets(self):
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(self.main_frame, text="Advanced Password Generator", style='Header.TLabel').grid(row=0, column=0, columnspan=3, pady=(0, 10))

        # Password length
        ttk.Label(self.main_frame, text="Password Length:").grid(row=1, column=0, sticky=tk.W)
        self.length_slider = ttk.Scale(self.main_frame, from_=8, to=50, orient=tk.HORIZONTAL)
        self.length_slider.set(12)
        self.length_slider.grid(row=1, column=1, sticky=tk.EW, padx=5)
        self.length_value = ttk.Label(self.main_frame, text="12")
        self.length_value.grid(row=1, column=2, sticky=tk.W)
        self.length_slider.config(command=self.update_length_value)

        # Character type checkboxes
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)

        check_frame = ttk.LabelFrame(self.main_frame, text="Include Characters")
        check_frame.grid(row=2, column=0, columnspan=3, pady=5, sticky=tk.EW)

        ttk.Checkbutton(check_frame, text="Uppercase (A-Z)", variable=self.uppercase_var).grid(row=0, column=0, sticky=tk.W)
        ttk.Checkbutton(check_frame, text="Lowercase (a-z)", variable=self.lowercase_var).grid(row=1, column=0, sticky=tk.W)
        ttk.Checkbutton(check_frame, text="Digits (0-9)", variable=self.digits_var).grid(row=2, column=0, sticky=tk.W)
        ttk.Checkbutton(check_frame, text="Symbols (!@#$)", variable=self.symbols_var).grid(row=3, column=0, sticky=tk.W)

        # Exclude characters
        exclude_frame = ttk.LabelFrame(self.main_frame, text="Exclude Characters")
        exclude_frame.grid(row=3, column=0, columnspan=3, pady=5, sticky=tk.EW)
        ttk.Label(exclude_frame, text="Characters to exclude:").grid(row=0, column=0, sticky=tk.W)
        self.exclude_entry = ttk.Entry(exclude_frame)
        self.exclude_entry.grid(row=1, column=0, sticky=tk.EW)

        # Strength meter
        strength_frame = ttk.LabelFrame(self.main_frame, text="Password Strength")
        strength_frame.grid(row=4, column=0, columnspan=3, pady=5, sticky=tk.EW)
        self.strength_label = ttk.Label(strength_frame, text="Strength: -")
        self.strength_label.grid(row=0, column=0, sticky=tk.W)
        self.strength_bar = ttk.Progressbar(strength_frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
        self.strength_bar.grid(row=0, column=1, sticky=tk.E, padx=5)

        # Generated password
        password_frame = ttk.LabelFrame(self.main_frame, text="Generated Password")
        password_frame.grid(row=5, column=0, columnspan=3, pady=5, sticky=tk.EW)
        self.password_entry = ttk.Entry(password_frame, font=('Arial', 12), justify='center')
        self.password_entry.grid(row=0, column=0, sticky=tk.EW, padx=5, pady=5)

        # Buttons
        btn_frame = ttk.Frame(self.main_frame)
        btn_frame.grid(row=6, column=0, columnspan=3, pady=10)
        ttk.Button(btn_frame, text="Generate", command=self.generate_password).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Copy", command=self.copy_to_clipboard).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="Save", command=self.save_password).grid(row=0, column=2, padx=5)

        # History
        history_frame = ttk.LabelFrame(self.main_frame, text="Password History")
        history_frame.grid(row=7, column=0, columnspan=3, sticky=tk.EW, pady=5)
        self.history_listbox = tk.Listbox(history_frame, height=5)
        self.history_listbox.grid(row=0, column=0, sticky=tk.EW)
        scrollbar = ttk.Scrollbar(history_frame, orient=tk.VERTICAL, command=self.history_listbox.yview)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        self.history_listbox.config(yscrollcommand=scrollbar.set)

        history_btns = ttk.Frame(history_frame)
        history_btns.grid(row=1, column=0, columnspan=2, pady=5)
        ttk.Button(history_btns, text="Load", command=self.load_selected_password).grid(row=0, column=0, padx=5)
        ttk.Button(history_btns, text="Delete", command=self.delete_selected_password).grid(row=0, column=1, padx=5)
        ttk.Button(history_btns, text="Clear", command=self.clear_password_history).grid(row=0, column=2, padx=5)

        self.main_frame.columnconfigure(1, weight=1)
        exclude_frame.columnconfigure(0, weight=1)
        password_frame.columnconfigure(0, weight=1)

    def update_length_value(self, value):
        self.length_value.config(text=str(int(float(value))))

    def generate_password(self):
        length = int(self.length_slider.get())
        pool = []
        if self.uppercase_var.get():
            pool.extend(string.ascii_uppercase)
        if self.lowercase_var.get():
            pool.extend(string.ascii_lowercase)
        if self.digits_var.get():
            pool.extend(string.digits)
        if self.symbols_var.get():
            pool.extend('!@#$%^&*()-_=+')

        exclude = set(self.exclude_entry.get())
        pool = [char for char in pool if char not in exclude]

        if not pool:
            messagebox.showerror("Error", "No characters available. Adjust your settings.")
            return

        password = ''.join(random.choice(pool) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.calculate_strength(password)

    def calculate_strength(self, password):
        strength = 0
        strength += min(len(password) / 50 * 40, 40)

        types = [any(c.isupper() for c in password),
                 any(c.islower() for c in password),
                 any(c.isdigit() for c in password),
                 any(c in string.punctuation for c in password)]
        strength += sum(types) * 15

        self.strength_bar['value'] = strength
        if strength < 40:
            self.strength_bar.config(style='red.Horizontal.TProgressbar')
            label = "Weak"
        elif strength < 70:
            self.strength_bar.config(style='yellow.Horizontal.TProgressbar')
            label = "Moderate"
        else:
            self.strength_bar.config(style='green.Horizontal.TProgressbar')
            label = "Strong"

        self.strength_label.config(text=f"Strength: {label} ({int(strength)}%)")

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("No Password", "Generate a password first!")

    def save_password(self):
        password = self.password_entry.get()
        if password:
            self.password_history.append(password)
            self.password_history = self.password_history[-20:]  # limit to 20
            self.save_history()
            self.update_history_listbox()
            messagebox.showinfo("Saved", "Password saved to history.")
        else:
            messagebox.showwarning("Empty", "No password to save.")

    def load_selected_password(self):
        selection = self.history_listbox.curselection()
        if selection:
            password = self.history_listbox.get(selection[0])
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
            self.calculate_strength(password)

    def delete_selected_password(self):
        selection = self.history_listbox.curselection()
        if selection:
            index = len(self.password_history) - 1 - selection[0]
            del self.password_history[index]
            self.save_history()
            self.update_history_listbox()

    def clear_password_history(self):
        if messagebox.askyesno("Confirm", "Clear entire password history?"):
            self.password_history = []
            self.save_history()
            self.update_history_listbox()

    def load_history(self):
        try:
            with open('password_history.json', 'r') as f:
                self.password_history = json.load(f)
        except:
            self.password_history = []

    def save_history(self):
        with open('password_history.json', 'w') as f:
            json.dump(self.password_history, f)

    def update_history_listbox(self):
        self.history_listbox.delete(0, tk.END)
        for pwd in reversed(self.password_history):
            self.history_listbox.insert(tk.END, pwd)

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
