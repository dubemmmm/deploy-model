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
# Home Section
if option == "Home":
    st.header("Welcome")
    st.write("I am a motivated and dynamic individual driven by a result-oriented approach and a keen eagerness to learn.")
    st.image("IMG_3489.JPG", width=300)  # Add your image here

    st.write("## Connect with me")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/chidubem-onwuchuluba-787414227/)")
    st.markdown("[GitHub](https://github.com/dubemmmm)")
    st.markdown("[Email](mailto:onwuchulubachidubem@gmail.com)")
