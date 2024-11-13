import tkinter as tk
from tkinter import messagebox
import codecs

def encrypt(text):
    
    return codecs.encode(text, 'rot_13')

def decrypt(text):
    
    return codecs.encode(text, 'rot_13')

def on_encrypt():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Masukkan teks yang valid.")
        return
    encrypted_text = encrypt(text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_text)

def on_decrypt():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Masukkan teks yang valid.")
        return
    decrypted_text = decrypt(text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Enkripsi dan Dekripsi")
root.geometry("600x500")
root.configure(bg="#f0f0f0")

# Mengatur font
header_font = ("Helvetica", 16, "bold")
label_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

# Header
header_label = tk.Label(root, text="Aplikasi Enkripsi dan Dekripsi", font=header_font, bg="#f0f0f0", fg="#333")
header_label.pack(pady=10)

# Input teks
tk.Label(root, text="Masukkan Teks:", font=label_font, bg="#f0f0f0").pack(pady=5)
input_text = tk.Text(root, height=10, width=50, bg="#ffffff", fg="#333", font=label_font)
input_text.pack(pady=5)

# Tombol Enkripsi
encrypt_button = tk.Button(root, text="Enkripsi", command=on_encrypt, bg="#FFB6C1", fg="black", font=button_font)  # Warna pink salem
encrypt_button.pack(pady=5)

# Tombol Dekripsi
decrypt_button = tk.Button(root, text="Dekripsi", command=on_decrypt, bg="#ADD8E6", fg="black", font=button_font)  # Warna baby blue
decrypt_button.pack(pady=5)

# Output teks
tk.Label(root, text="Hasil:", font=label_font, bg="#f0f0f0").pack(pady=5)
output_text = tk.Text(root, height=10, width=50, bg="#ffffff", fg="#333", font=label_font)
output_text.pack(pady=5)

# Menjalankan aplikasi
root.mainloop()
