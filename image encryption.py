import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

# Function to load an image
def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        global img
        img = Image.open(file_path)
        img.thumbnail((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        panel.configure(image=img_tk)
        panel.image = img_tk

# Function to encrypt the image
def encrypt_image():
    global img, encrypted_img
    if img:
        img_array = np.array(img)
        key = 42  # Simple key for XOR
        encrypted_array = img_array ^ key  # XOR operation
        encrypted_img = Image.fromarray(encrypted_array)
        encrypted_img.thumbnail((300, 300))
        img_tk = ImageTk.PhotoImage(encrypted_img)
        panel.configure(image=img_tk)
        panel.image = img_tk
        messagebox.showinfo("Encryption", "Image encrypted successfully!")

# Function to decrypt the image
def decrypt_image():
    global encrypted_img
    if encrypted_img:
        img_array = np.array(encrypted_img)
        key = 42  # Same key used for decryption
        decrypted_array = img_array ^ key  # Reverse XOR
        decrypted_img = Image.fromarray(decrypted_array)
        decrypted_img.thumbnail((300, 300))
        img_tk = ImageTk.PhotoImage(decrypted_img)
        panel.configure(image=img_tk)
        panel.image = img_tk
        messagebox.showinfo("Decryption", "Image decrypted successfully!")

# Initialize the main window
root = tk.Tk()
root.title("Image Encryption/Decryption Tool")

# Panel to display images
panel = tk.Label(root)
panel.pack()
# Buttons for loading, encrypting, and decrypting
load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack(side="left")

encrypt_button = tk.Button(root, text="Encrypt Image", command=encrypt_image)
encrypt_button.pack(side="left")

decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt_image)
decrypt_button.pack(side="left")

# Run the application
root.mainloop()
