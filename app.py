import streamlit as st
import sqlite3
from transformers import pipeline

# Connexion à la base de données SQLite
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Création de la table utilisateurs
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT, course TEXT)''')

# Formulaire d'inscription
st.title("Plateforme Éducative Francophone")
st.subheader("Inscrivez-vous à un cours")

name = st.text_input("Nom")
email = st.text_input("Email")
course = st.selectbox("Choisissez un cours", ["Introduction à l'IA", "Programmation Python", "Data Science"])

if st.button("S'inscrire"):
    c.execute("INSERT INTO users (name, email, course) VALUES (?, ?, ?)", (name, email, course))
    conn.commit()
    st.success(f"{name}, vous êtes inscrit(e) au cours {course}!")

# Traitement d'IA avec Hugging Face
st.subheader("Découvrez l'IA avec Hugging Face")
text_input = st.text_area("Entrez du texte à analyser")

if st.button("Analyser le texte"):
    classifier = pipeline('sentiment-analysis')
    result = classifier(text_input)
    st.write(result)
