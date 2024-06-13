import streamlit as st
import requests



# Set the title and description
st.title('My Portfolio')
st.write("""
I am a motivated and dynamic professional with a passion for
artificial intelligence, deep learning, and generative AI. With a
strong foundation in full-stack software development, particularly
using the Django framework, I bring a comprehensive skill set to
any project. My results-oriented approach and eagerness to learn
drive me to excel in high-pressure situations and contribute to
team success. By leveraging my expertise in AI and software
development, I aim to extract valuable insights from complex
data, fostering informed decision-making and delivering
innovative solutions.
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
