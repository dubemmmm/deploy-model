import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Function to load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load icons
icons = {
    "home": load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_0erqc7f7.json"),
    "work": load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_DMgKk1.json"),
    "education": load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_bXrNZP.json"),
    "skills": load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_OARbs9.json"),
    "projects": load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_HU0diTr.json")
}

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#6f42c1, #7952b3);
        color: white;
    }
    .sidebar .sidebar-content a {
        color: white;
    }
    .sidebar .sidebar-content a:hover {
        color: #d1d8e0;
    }
    .css-1aumxhk a {
        color: #6f42c1;
    }
    .css-1aumxhk a:hover {
        color: #7952b3;
    }
    </style>
    """, unsafe_allow_html=True)

# Set the title and description
st.title('My Portfolio')
st.write("""
Welcome to my professional portfolio. Here you can find information about my work experience, education, skills, and projects.
""")

# Add a sidebar with navigation
st.sidebar.title("Navigation")
st.sidebar.image("images/profile.jpg", width=150)
option = st.sidebar.radio("Go to", ["Home", "Work Experience", "Education", "Skills", "Projects"])

# Home Section
if option == "Home":
    st.header("Welcome")
    st_lottie(icons["home"], height=200)
    st.write("I am a motivated and dynamic individual driven by a result-oriented approach and a keen eagerness to learn.")
    st.image("images/profile.jpg", width=300)  # Add your image here

    st.write("## Connect with me")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/your-profile/)")
    st.markdown("[![GitHub](https://img.shields.io/badge/-GitHub-black?style=flat&logo=github)](https://github.com/dubemmmm)")
    st.markdown("[![Email](https://img.shields.io/badge/-Email-red?style=flat&logo=gmail)](mailto:your-email@example.com)")

# Work Experience Section
elif option == "Work Experience":
    st.header("Work Experience")
    st_lottie(icons["work"], height=200)

    st.subheader("Data Science Intern (March 2024 – Present)")
    st.write("Hamoye AI")
    st.write("""
    - Gained understanding of Generative Adversarial Networks (GANs).
    - Optimized large language models (LLMs) through fine-tuning techniques.
    - Developed foundational understanding of different generative models.
    """)

    st.subheader("Generative AI and Data Science Intern (Oct. 2023 – March 2024)")
    st.write("Flexisaf Edusoft Ltd")
    st.write("""
    - Worked with GANs including DCGANs, CycleGANs, and StyleGANs.
    - Executed complex computer vision tasks using Convolutional Neural Networks (CNN) and transfer learning.
    - Utilized NLP and LSTM for sentiment analysis and text summarization.
    """)

    st.subheader("Networking Intern (July 2022 – Oct. 2022)")
    st.write("Treten Networks")
    st.write("""
    - Collaborated with the IP security team to install routers, switches, and ODF in data centers.
    - Troubleshot Cisco Meraki devices to improve functionality.
    """)

    st.subheader("Robotic Process Automation Intern (March 2022 – July 2022)")
    st.write("Polaris Bank Limited")
    st.write("""
    - Utilized software bots to automate banking processes.
    - Implemented Robotic Process Automation (RPA) for repetitive tasks.
    """)

# Education Section
elif option == "Education":
    st.header("Education")
    st_lottie(icons["education"], height=200)
    st.subheader("Bachelor of Science (B.Sc.), Computer Science")
    st.write("Covenant University, 2023 (1st Class, 4.79/5)")

# Skills Section
elif option == "Skills":
    st.header("Technical and Soft Skills")
    st_lottie(icons["skills"], height=200)
    st.subheader("Technical Skills")
    st.write("""
    - Pytorch, Tensorflow, Scikit-learn
    - Matplotlib, Pandas, Numpy
    - Pytesseract, Pillow, OpenCV
    - Django, Flask, HTML5, CSS3
    - Python, JavaScript, C#, Flutter
    - Hugging Face Transformers, NLTK
    - Jupyter Notebook, Google Colab
    """)
    st.subheader("Soft Skills")
    st.write("""
    - Problem Solving
    - Teamwork
    - Leadership
    - Time Management
    - Analytical Thinking
    - Self-Motivation
    - Excellent Communication
    - Flexibility and Adaptability
    """)

# Projects Section
elif option == "Projects":
    st.header("Projects")
    st_lottie(icons["projects"], height=200)

    # Fetch and display pinned GitHub projects
    st.subheader("Pinned GitHub Projects")
    GITHUB_USERNAME = "dubemmmm"
    
    def get_pinned_repos(username):
        url = f"https://api.github.com/users/{username}/repos?per_page=6"
        response = requests.get(url)
        repos = response.json()
        return repos

    repos = get_pinned_repos(GITHUB_USERNAME)
    for repo in repos:
        st.markdown(f"### [{repo['name']}]({repo['html_url']})")
        st.markdown(f"**Description**: {repo['description']}")
        st.markdown(f"**Technologies Used**: {repo['language']}")
        st.markdown("---")

# Save the code in a file named `app.py` and run it using the command `streamlit run app.py`.

# Ensure you have the following in your `requirements.txt`:
# streamlit
# requests
# streamlit-lottie
