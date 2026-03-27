import tkinter as tk
from tkinter import filedialog, messagebox
import re

def browse_input_file():
    filename = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text files", "*.txt")])
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, filename)

def browse_output_file():
    filename = filedialog.asksaveasfilename(title="Select Output File", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, filename)

def extract_sentences():
    input_file = input_file_entry.get()
    keyword = keyword_entry.get().strip().lower()
    output_file = output_file_entry.get()

    if not input_file or not keyword or not output_file:
        messagebox.showwarning("Missing Info", "Please provide all required inputs.")
        return

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        # Split text into sentences using regex (handles basic punctuation)
        sentences = re.split(r'(?<=[.!?])\s+', text)
        matches = [s for s in sentences if keyword in s.lower()]

        with open(output_file, "w", encoding="utf-8") as out_file:
            for sentence in matches:
                out_file.write(sentence.strip() + "\n")

        messagebox.showinfo("Done", f"{len(matches)} sentence(s) containing '{keyword}' saved to {output_file}.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Keyword Sentence Extractor")

# Input File
tk.Label(root, text="Input File:").grid(row=0, column=0, sticky="e")
input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_input_file).grid(row=0, column=2)

# Keyword
tk.Label(root, text="Keyword:").grid(row=1, column=0, sticky="e")
keyword_entry = tk.Entry(root, width=50)
keyword_entry.grid(row=1, column=1, columnspan=2)

# Output File
tk.Label(root, text="Output File:").grid(row=2, column=0, sticky="e")
output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=2, column=1)
tk.Button(root, text="Browse", command=browse_output_file).grid(row=2, column=2)

# Extract Button
tk.Button(root, text="Extract Sentences", command=extract_sentences, bg="lightblue").grid(row=3, column=1, pady=10)

root.mainloop()
