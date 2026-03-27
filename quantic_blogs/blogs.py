import tkinter as tk
from tkinter import filedialog, messagebox
import nltk
from nltk.tokenize import sent_tokenize
import os

# Download tokenizer data once
nltk.download('punkt')

def select_input_file():
    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if path:
        input_file_path.set(path)

def select_output_file():
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if path:
        output_file_path.set(path)

def find_and_save_sentences():
    input_path = input_file_path.get()
    output_path = output_file_path.get()
    keyword = keyword_entry.get().strip()

    if not input_path or not output_path or not keyword:
        messagebox.showwarning("Missing Info", "Please select files and enter a keyword.")
        return

    try:
        with open(input_path, 'r', encoding='utf-8') as infile:
            text = infile.read()
            sentences = sent_tokenize(text)
            matched = [s for s in sentences if keyword.lower() in s.lower()]

        if matched:
            with open(output_path, 'w', encoding='utf-8') as outfile:
                outfile.write('\n'.join(matched))
            result_label.config(text=f"{len(matched)} sentence(s) saved.")
        else:
            result_label.config(text="No matching sentences found.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

# GUI setup
root = tk.Tk()
root.title("Keyword Sentence Extractor")
root.geometry("500x300")

input_file_path = tk.StringVar()
output_file_path = tk.StringVar()

tk.Label(root, text="Input File:").pack()
tk.Entry(root, textvariable=input_file_path, width=60).pack(pady=2)
tk.Button(root, text="Browse Input File", command=select_input_file).pack()

tk.Label(root, text="Keyword:").pack(pady=5)
keyword_entry = tk.Entry(root, width=40)
keyword_entry.pack()

tk.Label(root, text="Output File:").pack(pady=5)
tk.Entry(root, textvariable=output_file_path, width=60).pack(pady=2)
tk.Button(root, text="Browse Output File", command=select_output_file).pack()

tk.Button(root, text="Find and Save Sentences", command=find_and_save_sentences, bg="#4CAF50", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", fg="blue")
result_label.pack()

root.mainloop()
