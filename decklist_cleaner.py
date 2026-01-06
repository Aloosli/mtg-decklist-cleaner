import tkinter as tk
import pyperclip

def clean_clipboard():
    text = pyperclip.paste()
    lines = text.splitlines()

    cleaned_lines = [line for line in lines if line.strip()]
    cleaned = "\n".join(cleaned_lines)

    if cleaned != text:
    pyperclip.copy(cleaned)


    removed = len(lines) - len(cleaned_lines)
    status_label.config(text=f"✅ Removed {removed} empty lines")



root = tk.Tk()
root.title("Decklist Cleaner")
root.geometry("300x150")
root.resizable(False, False)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True, fill=tk.BOTH)

title_label = tk.Label(frame, text="Decklist Cleaner", font=("Helvetica", 16,"bold"))
title_label.pack(pady=(0, 10))

clean_button = tk.Button(
    frame,
    text="Clean Clipboard",
    command=clean_clipboard,
    font=("Helvetica", 12),
    width=20,
    height=2
)
clean_button.pack()

status_label = tk.Label(frame, text="",fg="green")
status_label.pack( pady=(10, 0))
clean_clipboard()
root.bind("<Control-Return>", lambda e: clean_clipboard())
root.mainloop()




            