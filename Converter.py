# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 09:13:57 2025

@author: irene
"""

import streamlit as st
from datetime import timedelta

st.set_page_config(page_title="Minuti ↔ Polli Converter 🐔", page_icon="🐔")

st.title("🐔 Il converter che aspettavi finalmente è arrivato!")

st.markdown("Converti **Minuti → Polli** e **Polli → Minuti**")

# Costante: 1 pollo = 14 secondi
SECONDI_PER_POLLO = 14

# --- Minutes to Polli Section ---
st.subheader("🔁 Converter Minuti → Polli")
min_input = st.text_input("Inserisci i minuti", key="min")

if st.button("Converti in polli 🐔"):
    try:
        minutes = float(min_input)
        secondi_totali = int(minutes * 60)
        polli = round(secondi_totali / SECONDI_PER_POLLO, 2)
        st.success(f"✅ {minutes} minuti = {polli} polli")
    except ValueError:
        st.error("❌ Inserisci un numero valido per i minuti.")

st.markdown("---")

# --- Polli to Minutes Section ---
st.subheader("🔁 Converter Polli → Minuti")
polli_input = st.text_input("Inserisci i polli", key="polli")

if st.button("Converti in tempo ⏱️"):
    try:
        polli = float(polli_input)
        secondi_totali = int(polli * SECONDI_PER_POLLO)
        tempo = str(timedelta(seconds=secondi_totali))

        # Formatto per avere hh:mm:ss (aggiunge zeri se mancano)
        if secondi_totali < 3600:
            tempo = "0:" + tempo if ":" not in tempo.split(":")[0] else tempo

        st.success(f"✅ {polli} polli = {tempo} (hh:mm:ss)")
    except ValueError:
        st.error("❌ Inserisci un numero valido per i polli.")

