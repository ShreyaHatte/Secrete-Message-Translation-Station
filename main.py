import tkinter as tk
from tkinter import ttk
from ui_action import encode_action, decode_action, view_history


# ===== MAIN WINDOW =====

window = tk.Tk()
window.title("Secret Message Translation Station")
window.geometry("650x500")
window.config(bg="#17172f")


# ===== LOAD OLD MESSAGES =====

def load_messages():
    messages = []

    try:
        file = open("message_history.txt", "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            if ":" in line:
                msg = line.split(":", 1)[1].strip()
                if msg not in messages:
                    messages.append(msg)

    except:
        pass

    return messages


# ===== REFRESH DROPDOWN =====

def refresh_dropdown():
    message_entry["values"] = load_messages()


# ===== TITLE =====

title = tk.Label(
    window,
    text="Secret Message Translator",
    font=("Arial", 28, "bold"),
    bg="#17172f",
    fg="white"
)
title.pack(pady=25)


# ===== MESSAGE LABEL =====

message_label = tk.Label(
    window,
    text="Enter Message",
    font=("Arial", 16),
    bg="#17172f",
    fg="white"
)
message_label.pack()


# ===== MESSAGE DROPDOWN =====

message_var = tk.StringVar()

message_entry = ttk.Combobox(
    window,
    width=33,
    font=("Arial", 16),
    textvariable=message_var
)

message_entry["values"] = load_messages()
message_entry.pack(pady=10)


# ===== KEY LABEL =====

key_label = tk.Label(
    window,
    text="Enter Secret Key",
    font=("Arial", 16),
    bg="#17172f",
    fg="white"
)
key_label.pack()


# ===== KEY ENTRY =====

key_entry = tk.Entry(
    window,
    width=15,
    font=("Arial", 16)
)
key_entry.pack(pady=10)


# ===== RESULT LABEL =====

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 18),
    bg="#2b2b45",
    fg="white",
    width=30,
    height=2
)
result_label.pack(pady=30)


# ===== ENCODE BUTTON =====

encode_button = tk.Button(
    window,
    text="Encode Message",
    font=("Arial", 16, "bold"),
    bg="#4CAF50",
    fg="white",
    width=20,
    command=lambda: [
        encode_action(message_entry, key_entry, result_label),
        refresh_dropdown()
    ]
)
encode_button.pack(pady=15)


# ===== DECODE BUTTON =====

decode_button = tk.Button(
    window,
    text="Decode Message",
    font=("Arial", 16, "bold"),
    bg="#2196F3",
    fg="white",
    width=20,
    command=lambda: [
        decode_action(message_entry, key_entry, result_label),
        refresh_dropdown()
    ]
)
decode_button.pack(pady=10)


# ===== HISTORY BUTTON =====

history_button = tk.Button(
    window,
    text="View Message History",
    font=("Arial", 12, "bold"),
    bg="#9C27B0",
    fg="white",
    command=view_history
)
history_button.pack()


# ===== RUN APP =====

window.mainloop()