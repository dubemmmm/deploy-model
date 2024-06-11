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

# GitHub Projects section
st.header("Projects")
username = 'dubemmmm'  # Replace with your GitHub username
projects = fetch_github_projects(username)

for project in projects:
    st.subheader(project['name'])
    st.write(project['description'])
    st.write(f"[GitHub Link]({project['html_url']})")

    if project['homepage']:
        st.write(f"[Live Demo]({project['homepage']})")

    st.write("---")

# Contact section
st.header("Contact")
st.write("""
Feel free to reach out to me through any of the following platforms:
- [LinkedIn](https://www.linkedin.com/in/your-linkedin-profile)
- [Twitter](https://twitter.com/your-twitter-handle)
- [Email](mailto:your-email@example.com)
""")

# Footer
st.write("© 2024 Your Name. All rights reserved.")



