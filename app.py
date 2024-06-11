import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Define a function to fetch and display GitHub projects
def fetch_github_projects(username):
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)
    return response.json()

# Header section
st.title("My Portfolio")
st.write("""
Welcome to my portfolio! Here, you'll find a showcase of my projects, skills, and experiences.
Feel free to explore and learn more about my work.
""")

# About section
st.header("About Me")
st.write("""
I am a motivated and dynamic individual with a strong results-oriented approach and a keen eagerness to learn.
My areas of interest lie in artificial intelligence, deep learning, and generative AI.
Additionally, I excel in full-stack software development using the Django framework.
""")



