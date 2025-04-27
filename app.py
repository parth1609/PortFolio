import streamlit as st
import time

st.set_page_config(
    page_title="Parth Patil | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.streamlit.io/community',
        'Report a bug': 'https://github.com/parth1609/portfolio/issues',
        'About': 'A visually appealing, SEO-optimized portfolio website built with Streamlit.'
    }
)

st.markdown("""
<meta name='description' content='Portfolio of Parth Patil - AI Enthusiast, Competitive Programmer, and Developer. Showcasing projects, skills, and contact information.'>
<style>
.stApp {
    background: linear-gradient(135deg, #232526 0%, #414345 100%);
    color: #FAFAFA;
    font-family: 'Segoe UI', 'Roboto', Arial, sans-serif;
}
.section-card {
    min-width: 100%;
    padding: 2rem;
    box-sizing: border-box;
    background: rgba(34,40,49,0.95);
    border-radius: 18px;
    box-shadow: 0 2px 16px rgba(0,0,0,0.15);
    margin-bottom: 2rem;
}
.stButton button {
    background: linear-gradient(90deg, #4F8BF9 0%, #1CB5E0 100%);
    color: white;
    border-radius: 8px;
    font-weight: 600;
    padding: 0.5rem 1.5rem;
    transition: background 0.3s;
    font-size: 1.1rem;
}
.stButton button:hover {
    background: linear-gradient(90deg, #1CB5E0 0%, #4F8BF9 100%);
}
.social-icons a {
    margin-right: 18px;
    color: #4F8BF9;
    font-size: 28px;
    transition: color 0.2s;
    text-decoration: none;
}
.social-icons a:hover {
    color: #1CB5E0;
}
.project-card {
    background: linear-gradient(120deg, #232526 60%, #1CB5E0 100%);
    border-radius: 14px;
    padding: 28px 24px;
    margin-bottom: 28px;
    box-shadow: 0 2px 12px rgba(28,181,224,0.08);
    transition: transform 0.2s, box-shadow 0.2s;
}
.project-card:hover {
    transform: translateY(-4px) scale(1.02);
    box-shadow: 0 8px 32px rgba(28,181,224,0.18);
}
.resume-btn {
    display: inline-block;
    background: linear-gradient(90deg, #4F8BF9 0%, #1CB5E0 100%);
    color: #fff;
    border-radius: 8px;
    font-weight: 600;
    padding: 0.5rem 1.5rem;
    text-decoration: none;
    margin-top: 1rem;
    font-size: 1.1rem;
    transition: background 0.3s;
}
.resume-btn:hover {
    background: linear-gradient(90deg, #1CB5E0 0%, #4F8BF9 100%);
    color: #fff;
}
.profile-pic img {
    border-radius: 50%;
    border: 4px solid #4F8BF9;
    box-shadow: 0 4px 24px rgba(79,139,249,0.3);
    animation: pulse 2s infinite;
}
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.07); }
    100% { transform: scale(1); }
}
@media (max-width: 900px) {
    .section-card, .project-card {
        padding: 1rem;
    }
    .profile-pic img {
        width: 120px !important;
    }
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("Navigation")
if 'go_to' not in st.session_state:
    st.session_state.go_to = "Intro"
st.sidebar.radio(
    "Go to",
    ["Intro", "About", "Projects", "Contact"],
    key="go_to"
)
page = st.session_state.go_to

st.sidebar.markdown("---")
st.sidebar.subheader("Progress")
progress_mapping = {"Intro": 25, "About": 50, "Projects": 75, "Contact": 100}
progress = st.sidebar.progress(progress_mapping[page])

st.markdown(f"<h1 style='text-align: center; font-size: 3rem; letter-spacing: 2px; color: #4F8BF9; margin-bottom: 0.5em;'>Parth Patil Portfolio</h1>", unsafe_allow_html=True)

if page == "Intro":
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.markdown("<div class='profile-pic'>", unsafe_allow_html=True)
        st.image("assets/sec.png", width=180, caption="Parth Patil", output_format="PNG")
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<h1 style='color:#FAFAFA; font-size:2.5rem;'>Parth Patil</h1>", unsafe_allow_html=True)
        typing_text = "400+ GeekforGeeks | Leetcode | AI Enthusiast | Competitive Programmer"
        placeholder = st.empty()
        for i in range(len(typing_text) + 1):
            placeholder.markdown(f"<h3 style='color:#1CB5E0'>{typing_text[:i]}<span style='opacity:0.5;'>|</span></h3>", unsafe_allow_html=True)
            time.sleep(0.02)
        placeholder.markdown(f"<h3 style='color:#1CB5E0'>{typing_text}</h3>", unsafe_allow_html=True)
        st.markdown("""
        <p style='font-size: 1.2rem; color: #B0B3B8;'>Welcome to my portfolio website. Here you'll find my projects, skills, and more about me.</p>
        <p style='font-size: 1.2rem; color: #B0B3B8;'>Feel free to explore my projects and get in touch if you'd like to collaborate or just say hi.</p>
        <a href='assets/ParthPatil_Resume.pdf' download class='resume-btn'>Download Resume</a>
        """, unsafe_allow_html=True)

elif page == "About":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.header("About Me")
    st.markdown("""
    <div style='font-size:1.1rem;'>
    <strong>AI enthusiast</strong> and <strong>competitive programmer</strong> with 400+ solved problems on coding platforms.<br>
    Passionate about building intelligent solutions and optimizing algorithms.<br>
    Currently exploring AI applications in real-world scenarios while maintaining competitive programming skills through regular practice.<br><br>
    <span style='color:#1CB5E0; font-weight:600;'>I believe in learning by doing and sharing knowledge with the community.</span>
    </div>
    """, unsafe_allow_html=True)
    st.subheader("Skills & Tools")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Languages**")
        st.markdown("- Python\n- HTML\n- CSS\n- SQL")
        st.markdown("**Databases**")
        st.markdown("- MySQL\n- SQLite\n- MongoDB")
    with col2:
        st.markdown("**Frameworks/Libraries**")
        st.markdown("- Streamlit\n- Pandas\n- Matplotlib")
        st.markdown("**Others**")
        st.markdown("- Git/Github\n- VS Code")
    st.markdown("---")
    st.markdown("<em style='color:#1CB5E0;'>On my own journey of continuous learning and improvement</em>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Projects":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.header("My Projects")
    # Project 1
    with st.container():
        st.markdown("<div class='project-card'>", unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2], gap="medium")
        with col1:
            st.image('assets/sec.png', width=260, caption="Restaurant Feedback Analysis", output_format="PNG")
        with col2:
            st.subheader("Restaurant Feedback Analysis")
            st.markdown("<p style='color:#B0B3B8;'><strong>Problem:</strong> Restaurants struggle to extract actionable insights from customer reviews. <br><strong>Solution:</strong> Built a sentiment analysis system using NLP and ML to process reviews. <br><strong>Result:</strong> Provided business owners with clear, actionable feedback for improvement.</p>", unsafe_allow_html=True)
            st.markdown("**Tech Used**: Python, Streamlit, CrewAI, MySQL, Ollama")
            st.markdown("<a href='https://github.com/parth1609/Restaurant-Feedback-Analysis' target='_blank' style='color:#1CB5E0; font-weight:600;'>GitHub Repo</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    # Project 2
    with st.container():
        st.markdown("<div class='project-card'>", unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2], gap="medium")
        with col1:
            st.image("https://via.placeholder.com/300x200", use_column_width=True, caption="AI-Powered Content Generator")
        with col2:
            st.subheader("AI-Powered Content Generator")
            st.markdown("<p style='color:#B0B3B8;'><strong>Problem:</strong> Manual content creation is time-consuming. <br><strong>Solution:</strong> Developed a tool using NLP to generate content based on user prompts. <br><strong>Result:</strong> Enabled users to quickly generate high-quality content for various needs.</p>", unsafe_allow_html=True)
            st.markdown("**Role**: Machine Learning Engineer")
            st.markdown("**Duration**: Apr 2023 – Jun 2023")
            st.markdown("**Tech Used**: Python, TensorFlow, Flask, React")
            st.markdown("<a href='https://example.com' target='_blank' style='color:#1CB5E0; font-weight:600;'>Live Demo</a> | <a href='https://github.com' target='_blank' style='color:#1CB5E0; font-weight:600;'>Source Code</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Contact":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.header("Get In Touch")
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.subheader("Contact Information")
        st.markdown("📧 <a href='mailto:parthgajananpatil@gmail.com' style='color:#1CB5E0;'>parthgajananpatil@gmail.com</a>", unsafe_allow_html=True)
        st.markdown("### Social Links")
        st.markdown("""
        <div class='social-icons'>
            <a href="https://github.com/parth1609" target="_blank" aria-label="GitHub">GitHub</a>
            <a href="https://linkedin.com/in/parth-patil-029790250/" target="_blank" aria-label="LinkedIn">LinkedIn</a>
            <a href="https://x.com/patilpa70248397" target="_blank" aria-label="Twitter">Twitter</a>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<a href='assets/ParthPatil_Resume.pdf' download class='resume-btn'>Download Resume</a>", unsafe_allow_html=True)
    with col2:
        st.subheader("Send Me a Message")
        with st.form("contact_form"):
            name = st.text_input("Name", key="contact_name")
            email = st.text_input("Email", key="contact_email")
            message = st.text_area("Message", key="contact_message")
            submit = st.form_submit_button("Send Message")
            if submit:
                st.success("Thanks for reaching out! I'll get back to you soon.")
    st.markdown("---")
    st.markdown("<p style='text-align: center; color:#B0B3B8;'>Thanks for visiting – let's connect!</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)