import os
import subprocess
import customtkinter as ctk
from tkinter import filedialog, messagebox

class PyToExeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Py to Exe Converter")
        self.root.geometry("700x300")
        
        self.py_file_path = ctk.StringVar()
        self.output_dir = ctk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self.root, text="Python File:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        ctk.CTkEntry(self.root, textvariable=self.py_file_path, width=400).grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkButton(self.root, text="Browse...", command=self.browse_py_file).grid(row=0, column=2, padx=10, pady=10)

        ctk.CTkLabel(self.root, text="Output Directory:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        ctk.CTkEntry(self.root, textvariable=self.output_dir, width=400).grid(row=1, column=1, padx=10, pady=10)
        ctk.CTkButton(self.root, text="Browse...", command=self.browse_output_dir).grid(row=1, column=2, padx=10, pady=10)

        ctk.CTkButton(self.root, text="Convert to EXE", command=self.convert_to_exe).grid(row=2, column=1, padx=10, pady=20)

    def browse_py_file(self):
        py_file = filedialog.askopenfilename(title="Select Python File", filetypes=[("Python Files", "*.py")])
        self.py_file_path.set(py_file)

    def browse_output_dir(self):
        output_directory = filedialog.askdirectory(title="Select Output Directory")
        self.output_dir.set(output_directory)

    def convert_to_exe(self):
        py_file = self.py_file_path.get()
        output_directory = self.output_dir.get()

        if not py_file:
            messagebox.showerror("Error", "Please select a Python file to convert.")
            return

        if not output_directory:
            messagebox.showerror("Error", "Please select an output directory.")
            return

        command = f"pyinstaller --onefile --distpath \"{output_directory}\" \"{py_file}\""

        try:
            subprocess.run(["python", "-m", "PyInstaller", "--onefile", "--distpath", output_directory, py_file], check=True)
            messagebox.showinfo("Success", "Conversion successful! The EXE file is located in the output directory.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = PyToExeApp(root)
    root.mainloop()
