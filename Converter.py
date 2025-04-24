# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 09:13:57 2025

@author: irene
"""

import streamlit as st

st.set_page_config(page_title="Minuti ↔ Polli Converter 🐔", page_icon="🐔")

st.title("🐔 Il converter che aspettavi finalmente è arrivato!")

st.markdown("Converti **Minuti → Polli** e **Polli → Minuti** con un clic!")

# --- Minutes to Polli Section ---
st.subheader("🔁 Converter Minuti → Polli")
min_input = st.text_input("Inserisci i minuti", key="min")

if st.button("Converti in polli 🐔"):
    try:
        minutes = int(min_input)
        polli = minutes * 4
        st.success(f"✅ {minutes} minuti = {polli} polli")
    except ValueError:
        st.error("❌ Inserisci un numero valido per i minuti.")

st.markdown("---")

# --- Polli to Minutes Section ---
st.subheader("🔁 Converter Polli → Minuti")
polli_input = st.text_input("Inserisci i polli", key="polli")

if st.button("Converti in minuti ⏱️"):
    try:
        polli = int(polli_input)
        minuti = polli // 4
        st.success(f"✅ {polli} polli = {minuti} minuti")
    except ValueError:
        st.error("❌ Inserisci un numero valido per i polli.")

