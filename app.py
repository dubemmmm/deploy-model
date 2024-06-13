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
# Work Experience Section
elif option == "Work Experience":
    st.header("Work Experience")

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
    st.subheader("Bachelor of Science (B.Sc.), Computer Science")
    st.write("Covenant University, 2023 (1st Class, 4.79/5)")

# Skills Section
elif option == "Skills":
    st.header("Technical and Soft Skills")
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
    
    # Fetch the pinned repositories from GitHub API
    username = "dubemmmm"
    token = "your_personal_access_token"  # Replace with your GitHub Personal Access Token
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"token {token}"}
    
    response = requests.get(url, headers=headers)
    repos = response.json()

    for repo in repos:
        if repo["pushed_at"]:  # Ensure the repo is not empty
            st.subheader(repo["name"])
            st.write(repo["description"])
            st.markdown(f"[View Repository]({repo['html_url']})")

