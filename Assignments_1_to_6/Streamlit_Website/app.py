import streamlit as st

# Page Configuration
st.set_page_config(page_title="My Awesome Website", page_icon="🌟", layout="wide")

# Hide default Streamlit styling and spacing
st.markdown("""
    <style>
    body {
        background-color: black;
        color: white;
    }
    header, footer, .css-18e3th9 {
        visibility: hidden;
        height: 0px;
    }
    .main {
        color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        margin: 1rem;
    }
    .big-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.5rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;
        padding: 1rem;
        border-top: 1px solid #ddd;
        margin-top: 2rem;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Home Page
if page == "Home":
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h1 class='big-title'>Welcome to My Awesome Website!</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Where creativity meets technology.</p>", unsafe_allow_html=True)
    st.image("https://picsum.photos/1200/400", use_container_width=True, caption="A Glimpse of Creativity")
    st.write("""
        Welcome to my professional portfolio website built with **Streamlit**. 
        This platform highlights my technical expertise, creative approach to problem-solving, 
        and passion for crafting impactful digital solutions. 
        Feel free to explore the different sections to learn more about my background, 
        projects, and how to connect with me.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# About Page
elif page == "About":
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h1 class='big-title'>About Me</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>My Journey & Passion</p>", unsafe_allow_html=True)
    st.image("https://picsum.photos/800/300", use_container_width=True, caption="A snippet of my journey")
    st.write("""
        As a dedicated and forward-thinking developer, I specialize in building modern, 
        user-centric web applications. With a strong foundation in computer science and 
        a drive for continuous learning, I transform innovative ideas into scalable, 
        elegant solutions. My work reflects a balance of creativity, precision, 
        and a deep understanding of technology.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# Contact Page
elif page == "Contact":
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h1 class='big-title'>Get in Touch</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>We'd love to hear from you!</p>", unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Thank you for your message! I'll get back to you soon.")
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Made with ❤️ by Saba Junaid</div>", unsafe_allow_html=True)
