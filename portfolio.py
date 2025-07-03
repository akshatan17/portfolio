import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Akshata Nagaraj | Portfolio", layout="wide", page_icon="🌿")

# --- Custom CSS ---
st.markdown("""
    <style>
    body {
        background-color: #f5f5dc;
    }
    .stApp {
        background-color: #f5f5dc;
        color: #2f4f4f;
        font-family: 'Segoe UI', sans-serif;
    }
    a {
        color: #3b7d5f;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    h1, h2, h3 {
        color: #2f4f4f;
    }
    .highlight {
        background-color: #e2f0cb;
        padding: 0.75rem;
        border-radius: 10px;
        font-size: 1.05rem;
    }
    .contact-info {
        margin-top: 1em;
        font-size: 1rem;
    }
    .section-title {
        margin-top: 2rem;
        font-size: 1.4rem;
        font-weight: bold;
        color: #264d3a;
    }
    .footer {
        margin-top: 3rem;
        text-align: center;
        font-size: 0.9rem;
        color: #556b2f;
    }
    .icon-link {
        display: flex;
        align-items: center;
        gap: 8px;
        margin: 5px 0;
        font-size: 1.05rem;
    }
    .icon-link img {
        width: 20px;
        height: 20px;
    }
    .menu-bar {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-bottom: 2rem;
    }
    .menu-item {
        font-size: 1.1rem;
        font-weight: 500;
        cursor: pointer;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        background-color: #d0e9d4;
        color: #264d3a;
    }
    .menu-item:hover {
        background-color: #bde0c6;
    }
    .tab-title {
        text-align: center;
        font-size: 2rem !important;
        font-weight: bold;
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Top Menu Navigation ---
tabs = st.tabs(["About Me", "Photos", "Certificates"])

# --- About Me ---
with tabs[0]:
    st.markdown("<h1 class='tab-title'>👋 Akshata Nagaraj</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='tab-title'>AI/ML Enthusiast | Creative Coder | Animal Lover</h3>", unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
    I'm passionate about artificial intelligence and coding—and when I'm not doing that, you'll find me caring for animals or exploring the world of neurotechnology.
    </div>
    """, unsafe_allow_html=True)

    # --- Social Links with Icons ---
    st.markdown("<div class='section-title'>🔗 Connect with me</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="icon-link">
        <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="GitHub">
        <a href="https://github.com/akshatan17" target="_blank">GitHub</a>
    </div>
    <div class="icon-link">
        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn">
        <a href="https://www.linkedin.com/in/akshata-nagaraj-4147842b8/" target="_blank">LinkedIn</a>
    </div>
    <div class="icon-link">
        <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" alt="Instagram">
        <a href="https://instagram.com/akshata_1704" target="_blank">Instagram</a>
    </div>
    <div class="icon-link">
        📧 <a href="mailto:akshatanagaraj1704@gmail.com">akshatanagaraj1704@gmail.com</a>
    </div>
    <div class="icon-link">
        📞 +91 99025 83700
    </div>
    """, unsafe_allow_html=True)

    # --- Projects ---
    st.markdown("<div class='section-title'>🛠️ Projects</div>", unsafe_allow_html=True)
    st.markdown("""
    **Hiveminds Internship — RAG PDF Assistant**  
    Built a user-friendly RAG (Retrieval-Augmented Generation) interface allowing users to upload PDFs and ask questions. Integrated with Gemini AI and deployed on Streamlit to provide real-time, context-aware answers.
    """)

    # --- Skills ---
    st.markdown("<div class='section-title'>🧠 Skills</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Languages 🧑‍💻")
        st.markdown("- Python\n- Java\n- C")

    with col2:
        st.markdown("#### Databases 💾")
        st.markdown("- SQL\n- MySQL")

    # --- Testimonials ---
    st.markdown("<div class='section-title'>💬 Testimonials</div>", unsafe_allow_html=True)
    st.markdown("""
    > “Akshata has a brilliant mind for AI and a kind heart for animals.” – Mentor

    > “Her work ethic and creativity are unmatched. A joy to collaborate with.” – Peer
    """)

# --- Photos ---
with tabs[1]:
    st.markdown("<h1 class='tab-title'>📷 Photos</h1>", unsafe_allow_html=True)
    st.info("Photo gallery coming soon!")

# --- Certificates ---
with tabs[2]:
    st.markdown("<h1 class='tab-title'>📜 Certificates</h1>", unsafe_allow_html=True)
    st.info("Certificates will be added shortly.")

# --- Footer ---
st.markdown("""
<div class="footer">
Made with ❤️ using Streamlit | © 2025 Akshata Nagaraj
</div>
""", unsafe_allow_html=True)
