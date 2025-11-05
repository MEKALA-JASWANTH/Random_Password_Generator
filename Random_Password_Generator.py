# Random Password Generator with Enhanced Features
# Added features: Customizable length, Special character options, Copy to clipboard, Save to file, Tkinter GUI

import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip
from datetime import datetime

class PasswordGeneratorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Random Password Generator")
        master.geometry("500x600")
        master.resizable(False, False)
        
        # Title
        title_label = tk.Label(master, text="Random Password Generator", font=("Arial", 18, "bold"), fg="#2c3e50")
        title_label.pack(pady=20)
        
        # Password Length
        length_frame = tk.Frame(master)
        length_frame.pack(pady=10)
        tk.Label(length_frame, text="Password Length:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        self.length_var = tk.IntVar(value=12)
        self.length_spinbox = tk.Spinbox(length_frame, from_=4, to=50, textvariable=self.length_var, width=10, font=("Arial", 12))
        self.length_spinbox.pack(side=tk.LEFT, padx=5)
        
        # Number of Passwords
        count_frame = tk.Frame(master)
        count_frame.pack(pady=10)
        tk.Label(count_frame, text="Number of Passwords:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
        self.count_var = tk.IntVar(value=1)
        self.count_spinbox = tk.Spinbox(count_frame, from_=1, to=20, textvariable=self.count_var, width=10, font=("Arial", 12))
        self.count_spinbox.pack(side=tk.LEFT, padx=5)
        
        # Character Options
        options_frame = tk.LabelFrame(master, text="Character Options", font=("Arial", 12, "bold"), padx=10, pady=10)
        options_frame.pack(pady=15, padx=20, fill="both")
        
        self.uppercase_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text="Include Uppercase Letters (A-Z)", variable=self.uppercase_var, font=("Arial", 10)).pack(anchor="w")
        
        self.lowercase_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text="Include Lowercase Letters (a-z)", variable=self.lowercase_var, font=("Arial", 10)).pack(anchor="w")
        
        self.numbers_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text="Include Numbers (0-9)", variable=self.numbers_var, font=("Arial", 10)).pack(anchor="w")
        
        self.special_var = tk.BooleanVar(value=True)
        tk.Checkbutton(options_frame, text="Include Special Characters (!@#$%^&*)", variable=self.special_var, font=("Arial", 10)).pack(anchor="w")
        
        # Generate Button
        self.generate_btn = tk.Button(master, text="Generate Password(s)", command=self.generate_passwords, 
                                      bg="#3498db", fg="white", font=("Arial", 12, "bold"), padx=20, pady=10)
        self.generate_btn.pack(pady=15)
        
        # Password Display
        display_frame = tk.Frame(master)
        display_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        tk.Label(display_frame, text="Generated Passwords:", font=("Arial", 11, "bold")).pack(anchor="w")
        
        # Text widget with scrollbar
        text_scroll = tk.Scrollbar(display_frame)
        text_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.password_text = tk.Text(display_frame, height=8, width=50, font=("Courier", 10), 
                                     yscrollcommand=text_scroll.set, wrap=tk.WORD)
        self.password_text.pack(side=tk.LEFT, fill="both", expand=True)
        text_scroll.config(command=self.password_text.yview)
        
        # Buttons Frame
        buttons_frame = tk.Frame(master)
        buttons_frame.pack(pady=10)
        
        self.copy_btn = tk.Button(buttons_frame, text="Copy to Clipboard", command=self.copy_to_clipboard,
                                  bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
        self.copy_btn.pack(side=tk.LEFT, padx=5)
        
        self.save_btn = tk.Button(buttons_frame, text="Save to File", command=self.save_to_file,
                                  bg="#e74c3c", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
        self.save_btn.pack(side=tk.LEFT, padx=5)
        
        self.clear_btn = tk.Button(buttons_frame, text="Clear", command=self.clear_display,
                                   bg="#95a5a6", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        self.generated_passwords = []
    
    def generate_passwords(self):
        try:
            length = self.length_var.get()
            count = self.count_var.get()
            
            # Build character set based on options
            char_set = ""
            if self.uppercase_var.get():
                char_set += string.ascii_uppercase
            if self.lowercase_var.get():
                char_set += string.ascii_lowercase
            if self.numbers_var.get():
                char_set += string.digits
            if self.special_var.get():
                char_set += "!@#$%^&*()_+-=[]{}|;:,.<>?"
            
            if not char_set:
                messagebox.showerror("Error", "Please select at least one character option!")
                return
            
            if length < 4:
                messagebox.showerror("Error", "Password length must be at least 4 characters!")
                return
            
            # Generate passwords
            self.generated_passwords = []
            self.password_text.delete(1.0, tk.END)
            
            for i in range(count):
                password = ''.join(random.choice(char_set) for _ in range(length))
                self.generated_passwords.append(password)
                self.password_text.insert(tk.END, f"Password #{i+1}: {password}\n")
            
            messagebox.showinfo("Success", f"{count} password(s) generated successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def copy_to_clipboard(self):
        if not self.generated_passwords:
            messagebox.showwarning("Warning", "No passwords to copy! Please generate passwords first.")
            return
        
        try:
            passwords_text = "\n".join(self.generated_passwords)
            pyperclip.copy(passwords_text)
            messagebox.showinfo("Success", "Passwords copied to clipboard!")
        except:
            # Fallback method if pyperclip is not available
            passwords_text = "\n".join(self.generated_passwords)
            self.master.clipboard_clear()
            self.master.clipboard_append(passwords_text)
            self.master.update()
            messagebox.showinfo("Success", "Passwords copied to clipboard!")
    
    def save_to_file(self):
        if not self.generated_passwords:
            messagebox.showwarning("Warning", "No passwords to save! Please generate passwords first.")
            return
        
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"passwords_{timestamp}.txt"
            
            with open(filename, 'w') as file:
                file.write("=" * 50 + "\n")
                file.write("Random Password Generator - Generated Passwords\n")
                file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write("=" * 50 + "\n\n")
                
                for i, password in enumerate(self.generated_passwords, 1):
                    file.write(f"Password #{i}: {password}\n")
                
                file.write("\n" + "=" * 50 + "\n")
            
            messagebox.showinfo("Success", f"Passwords saved to {filename}!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")
    
    def clear_display(self):
        self.password_text.delete(1.0, tk.END)
        self.generated_passwords = []

def main():
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
