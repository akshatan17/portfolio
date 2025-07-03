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
        transition: all 0.5s ease-in-out;
    }
    a {
        color: #3b7d5f;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    a:hover {
        text-decoration: underline;
        color: #1d5c3d;
    }
    h1, h2, h3 {
        color: #2f4f4f;
        transition: all 0.3s ease-in-out;
    }
    .highlight {
        background-color: #e2f0cb;
        padding: 0.75rem;
        border-radius: 10px;
        font-size: 1.05rem;
        animation: fadeIn 0.7s ease-in-out;
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
        animation: fadeInUp 0.7s ease-in-out;
    }
    .footer {
        margin-top: 3rem;
        text-align: center;
        font-size: 0.9rem;
        color: #556b2f;
        animation: fadeIn 1s ease-in-out;
    }
    .icon-link {
        display: flex;
        align-items: center;
        gap: 8px;
        margin: 5px 0;
        font-size: 1.05rem;
        transition: all 0.3s ease;
    }
    .icon-link img {
        width: 20px;
        height: 20px;
    }
    .tab-title {
        text-align: center;
        font-size: 2rem !important;
        font-weight: bold;
        color: #000000 !important;
        animation: fadeInDown 0.6s ease-in-out;
    }

    /* --- TAB OVERRIDES --- */
    .stTabs [role="tab"] {
        justify-content: center;
        color: #000000 !important;
        font-weight: bold;
        font-size: 2rem;
        border: none !important;
        box-shadow: none !important;
        border-bottom: none !important;
        outline: none !important;
        background: transparent !important;
    }
    .stTabs [role="tab"]:hover {
        color: #000000;
    }
    .stTabs [role="tab"][aria-selected="true"] {
        border-bottom: 3px solid black !important;
        box-shadow: none !important;
        background-color: transparent !important;
    }
    .stTabs [role="tab"]:focus {
        outline: none !important;
        box-shadow: none !important;
        border: none !important;
    }
    .stTabs [role="tab"]:focus-visible {
        outline: none !important;
        box-shadow: none !important;
        border: none !important;
    }

    .project-card {
        background-color: #ffffff;
        padding: 1rem;
        margin-top: 1rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        animation: fadeInUp 0.6s ease-in-out;
    }
    .project-card:hover {
        transform: translateY(-5px);
    }
    .skills-list li {
        animation: fadeIn 1s ease-in-out both;
    }
    .testimonial {
        font-style: italic;
        margin-bottom: 1rem;
        animation: fadeIn 0.8s ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    @keyframes fadeInUp {
        from {opacity: 0; transform: translateY(20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    @keyframes fadeInDown {
        from {opacity: 0; transform: translateY(-20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
""", unsafe_allow_html=True)

# --- Top Menu Navigation ---
tabs = st.tabs(["👤 About Me", "📷 Photos", "📜 Certificates"])

# --- About Me ---
with tabs[0]:
    st.markdown("<h1 class='tab-title'>👋 Akshata Nagaraj</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='tab-title'>AI/ML Enthusiast | Creative Coder | Animal Lover</h3>", unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
    I'm passionate about artificial intelligence and coding—and when I'm not doing that, you'll find me caring for animals or reading a book
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
    <div class='project-card'>
    <strong>Hiveminds Internship — RAG PDF Assistant</strong><br>
    Built a user-friendly RAG (Retrieval-Augmented Generation) interface allowing users to upload PDFs and ask questions. Integrated with Gemini AI and deployed on Streamlit to provide real-time, context-aware answers.
    </div>
    """, unsafe_allow_html=True)

    # --- Skills ---
    st.markdown("<div class='section-title'>🧠 Skills</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Languages 🧑‍💻")
        st.markdown("<ul class='skills-list'><li>Python</li><li>Java</li><li>C</li></ul>", unsafe_allow_html=True)
    with col2:
        st.markdown("#### Databases 💾")
        st.markdown("<ul class='skills-list'><li>SQL</li><li>MySQL</li></ul>", unsafe_allow_html=True)

    # --- Testimonials ---
    st.markdown("<div class='section-title'>💬 Testimonials</div>", unsafe_allow_html=True)
    st.markdown("<div class='testimonial'>“Akshata has a brilliant mind for AI and a kind heart for animals.” – Mentor</div>", unsafe_allow_html=True)
    st.markdown("<div class='testimonial'>Her work ethic and creativity are unmatched. A joy to collaborate with.” – Peer</div>", unsafe_allow_html=True)

# --- Photos ---
with tabs[1]:
    st.markdown("<h1 class='tab-title'>📷 Photos</h1>", unsafe_allow_html=True)
    st.markdown("Photo gallery coming soon!")

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