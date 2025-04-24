# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 09:13:57 2025

@author: irene
"""

import tkinter as tk
from tkinter import messagebox
import streamlit as st

st.title("Il converter che aspettavi finalmente è arrivato!")

def minutes_to_polli():
    try:
        minutes = int(min_entry.get())
        polli = minutes * 4
        min_to_hr_result.config(text=f"{minutes} minutes = {polli}polli")
    except ValueError:
        messagebox.showerror("Errore", "Inserisci un valore valido.")

def polli_to_minutes():
    try:
        polli = int(hour_entry.get())
        minuti = (polli // 4)
        hr_to_min_result.config(text=f"{polli}polli = {minuti} minuti")
    except ValueError:
        messagebox.showerror("Errore", "Inserisci un valore valido.")

# Create the main window
root = tk.Tk()
root.title("Minuti ↔ Polli Converter")

# --- Minutes to Hours Section ---
tk.Label(root, text="Converter Minuti → Polli", font=('Arial', 10, 'bold')).pack(pady=5)
tk.Label(root, text="Minuti:").pack()
min_entry = tk.Entry(root)
min_entry.pack()
tk.Button(root, text="Converti", command=minutes_to_polli).pack(pady=3)
min_to_hr_result = tk.Label(root, text="", fg="blue")
min_to_hr_result.pack(pady=5)

# --- Divider ---
tk.Label(root, text="-" * 40).pack()

# --- Hours to Minutes Section ---
tk.Label(root, text="Converter Polli → Minuti", font=('Arial', 10, 'bold')).pack(pady=5)
tk.Label(root, text="Polli:").pack()
hour_entry = tk.Entry(root)
hour_entry.pack()
tk.Button(root, text="Converti", command=polli_to_minutes).pack(pady=3)
hr_to_min_result = tk.Label(root, text="", fg="green")
hr_to_min_result.pack(pady=5)

# Run the app
root.mainloop()

