# from cipher import Cipher
# from tkinter import messagebox


# # ===== FILE HANDLING CLASS =====

# class FileHandler:

#     # WRITE INTO FILE
#     @staticmethod
#     def write_file(text):

#         file = open("message_history.txt", "a")

#         file.write(text + "\n")

#         file.close()


#     # READ FROM FILE
#     @staticmethod
#     def read_file():

#         try:

#             file = open("message_history.txt", "r")

#             data = file.read()

#             file.close()

#             return data

#         except:

#             return "No History Found"


# # ===== ENCODE FUNCTION =====

# def encode_action(message_entry, key_entry, result_label):

#     message = message_entry.get()

#     key = key_entry.get()

#     if not key.isdigit():

#         result_label.config(text="Key must be number")

#         return

#     cipher = Cipher(int(key))

#     result = cipher.encode_message(message)

#     result_label.config(text="Encoded : " + result)


#     # FILE WRITING
#     FileHandler.write_file("Encoded : " + result)


# # ===== DECODE FUNCTION =====

# def decode_action(message_entry, key_entry, result_label):

#     message = message_entry.get()

#     key = key_entry.get()

#     if not key.isdigit():

#         result_label.config(text="Key must be number")

#         return

#     cipher = Cipher(int(key))

#     result = cipher.decode_message(message)

#     result_label.config(text="Decoded : " + result)


#     # FILE WRITING
#     FileHandler.write_file("Decoded : " + result)


# # ===== VIEW HISTORY =====

# def view_history():

#     # FILE READING
#     history = FileHandler.read_file()

#     messagebox.showinfo("Message History", history)

from cipher import Cipher
from tkinter import messagebox


class FileHandler:

    @staticmethod
    def write_file(text):

        with open("message_history.txt", "a") as file:
            file.write(text + "\n")

    @staticmethod
    def read_file():

        try:
            with open("message_history.txt", "r") as file:
                return file.read()
        except:
            return "No History Found"


# ===== UPDATE DROPDOWN FUNCTION =====

def update_dropdown(message_entry, new_message):

    values = list(message_entry["values"])

    if new_message not in values:
        values.append(new_message)

    message_entry["values"] = values


# ===== ENCODE =====

def encode_action(message_entry, key_entry, result_label):

    message = message_entry.get()
    key = key_entry.get()

    if not key.isdigit():
        result_label.config(text="Key must be number")
        return

    cipher = Cipher(int(key))
    result = cipher.encode_message(message)

    result_label.config(text="Encoded : " + result)

    # SAVE TO FILE
    FileHandler.write_file("Encoded : " + result)

    # UPDATE DROPDOWN
    update_dropdown(message_entry, message)


# ===== DECODE =====

def decode_action(message_entry, key_entry, result_label):

    message = message_entry.get()
    key = key_entry.get()

    if not key.isdigit():
        result_label.config(text="Key must be number")
        return

    cipher = Cipher(int(key))
    result = cipher.decode_message(message)

    result_label.config(text="Decoded : " + result)

    # SAVE TO FILE
    FileHandler.write_file("Decoded : " + result)

    # UPDATE DROPDOWN
    update_dropdown(message_entry, message)


# ===== HISTORY =====

def view_history():

    history = FileHandler.read_file()
    messagebox.showinfo("Message History", history)