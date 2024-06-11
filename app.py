import streamlit as st
from PIL import Image
import requests

# GitHub username
GITHUB_USERNAME = 'dubemmmm'

# Function to fetch pinned repositories from GitHub
def get_pinned_repos(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=6"
    response = requests.get(url)
    repos = response.json()
    return repos

# Load profile image
profile_image = Image.open('')

# Sidebar - Profile image
st.sidebar.image(profile_image, width=150)

# Sidebar - Contact information
st.sidebar.markdown("## Contact Information")
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/your-linkedin-profile)")
st.sidebar.markdown("[GitHub](https://github.com/your-github-username)")
st.sidebar.markdown("Email: your.email@example.com")

# Main content
st.title("Your Name")
st.write("### Aspiring Generative AI Specialist & Full Stack Developer")

st.markdown("""
I am a motivated and dynamic individual with a keen eagerness to learn and a high commitment to team success. 
My areas of interest lie in artificial intelligence, deep learning, and generative AI, where I leverage my skills 
to contribute to innovative projects. I am also proficient in full stack software development using the Django framework.
""")

# Section - Skills
st.header("Skills")
st.markdown("""
- **Programming Languages**: Python, JavaScript, HTML, CSS
- **Frameworks and Libraries**: Django, TensorFlow, PyTorch
- **Tools and Platforms**: Git, Docker, AWS
- **Machine Learning**: Model development, Fine-tuning, Data preprocessing
- **Generative AI**: GANs, VAEs, Transformers
""")

# Section - Projects
st.header("Projects")

# Fetch and display pinned GitHub projects
st.subheader("Pinned GitHub Projects")
repos = get_pinned_repos(GITHUB_USERNAME)
for repo in repos:
    st.markdown(f"### [{repo['name']}]({repo['html_url']})")
    st.markdown(f"**Description**: {repo['description']}")
    st.markdown(f"**Technologies Used**: {repo['language']}")
    st.markdown("---")

# Section - Education
st.header("Education")
st.markdown("""
- **B.Sc. in Computer Science** - University Name
- **Generative AI Internship** - Hamoye
""")

# Section - Contact Form
st.header("Contact Me")
st.markdown("Feel free to reach out via the contact information in the sidebar or leave a message below:")

contact_form = st.form(key='contact_form')
with contact_form:
    name = st.text_input('Name')
    email = st.text_input('Email')
    message = st.text_area('Message')
    submit_button = st.form_submit_button(label='Send')

if submit_button:
    st.success(f"Thank you for your message, {name}! I'll get back to you soon.")
