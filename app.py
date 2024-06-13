import streamlit as st
import requests
# Set the title and description
st.title('My Portfolio')
st.write("""
Welcome to my professional portfolio. Here you can find information about my work experience, education, skills, and projects.
""")
# Add a sidebar with navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Go to", ["Home", "Work Experience", "Education", "Skills", "Projects"])
