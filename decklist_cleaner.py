# Core Tkinter module:
# - creates the main window
# - handles events (clicks, key presses, etc.)
import tkinter as tk

# ttk = "themed Tk"
# Provides modern-looking widgets (buttons, labels, frames)
from tkinter import ttk

# Simple cross-platform clipboard access
import pyperclip


def clean_clipboard():
    """
    Reads text from the clipboard, removes empty lines,
    and writes the cleaned text back to the clipboard.
    """
    # Get current clipboard contents
    text = pyperclip.paste()

    # Split text into individual lines
    lines = text.splitlines()

    # Keep only lines that contain visible characters
    cleaned_lines = [line for line in lines if line.strip()]

    # Join the cleaned lines back together with real newlines
    cleaned = "\n".join(cleaned_lines)

    # Only overwrite the clipboard if something actually changed
    if cleaned != text:
        pyperclip.copy(cleaned)

    # Update the status text with feedback for the user
    removed = len(lines) - len(cleaned_lines)
    status_label.config(text=f"✅ Removed {removed} empty lines")


# --------------------------------------------------
# GUI setup
# --------------------------------------------------

# Create the main application window
# NOTE: This must always be tk.Tk(), never ttk.Tk()
root = tk.Tk()
root.title("Decklist Cleaner")
root.minsize(280, 150)

root.resizable(False, False)

# Main container frame with padding
# ttk widgets inherit the system theme (less Windows XP vibes)
frame = ttk.Frame(root, padding=(24, 20))
frame.pack(expand=True, fill=tk.BOTH)

# Title text at the top of the window
title_label = ttk.Label(
    frame,
    text="Decklist Cleaner",
    font=("Segoe UI", 16, "bold")
)
title_label.pack(pady=(0, 14))

# Main action button
clean_button = ttk.Button(
    frame,
    text="Clean Clipboard",
    command=clean_clipboard
)
clean_button.pack(pady=(0, 10))

# Status label for feedback after cleaning

status_label = ttk.Label(frame, text="", foreground="green")
status_label.pack()

# --------------------------------------------------
# Keyboard shortcuts and startup behaviour
# --------------------------------------------------

# Allow Ctrl + Enter to trigger cleaning when the window is focused
root.bind("<Control-Return>", lambda e: clean_clipboard())

# Optional: clean clipboard immediately when the app starts
clean_clipboard()

# Start the Tk event loop (this keeps the window open)
root.mainloop()





            