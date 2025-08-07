import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from datetime import datetime
from io import StringIO

# --- Page Config (Called only once) ---
st.set_page_config(
    page_title="Akshata Nagaraj | Portfolio",
    layout="wide",
    page_icon="🌿"
)

# --- Custom CSS for Enhanced UI ---
# (Your original CSS was great, I've just added a few tweaks for new elements)
st.markdown("""
    <style>
    /* --- Color Palette & Fonts --- */
    :root {
        --bg-color: #f5ffeb;
        --text-color: #333333;
        --primary-color: #5d4037;
        --secondary-color: #795548;
        --accent-color: #a1887f;
        --card-bg: #ffffff;
        --border-color: #e0e0e0;
    }

    body {
        background-color: var(--bg-color);
        font-family: 'Inter', 'Segoe UI', 'Roboto', 'Helvetica', 'Arial', sans-serif;
    }
    .stApp {
        background-color: var(--bg-color);
        color: var(--text-color);
    }
    h1, h2, h3, h5 {
        color: var(--primary-color);
    }
    a {
        color: var(--primary-color);
        text-decoration: none;
        font-weight: 600;
    }
    a:hover {
        color: var(--secondary-color);
        text-decoration: underline;
    }
    
    /* --- Animation --- */
    .fade-in {
        animation: fadeIn 1.5s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* --- Tab Styles --- */
    .stTabs [role="tablist"] {
        justify-content: center;
        gap: 2.5rem;
        border-bottom: 1px solid var(--border-color);
    }
    .stTabs [role="tab"] {
        font-weight: 600;
        font-size: 1.15rem;
        background-color: transparent;
        color: var(--secondary-color) !important;
        border: none;
        border-radius: 0;
        padding: 10px 0;
        margin: 0;
        transition: color 0.3s ease;
    }
    .stTabs [role="tab"]:hover {
        color: var(--primary-color) !important;
    }
    .stTabs [role="tab"][aria-selected="true"] {
        background-color: transparent !important;
        color: var(--primary-color) !important;
        box-shadow: none;
        border-bottom: 3px solid var(--primary-color);
    }
    
    /* --- General & Specific Content Styles --- */
    .section-header {
        text-align: center;
        padding-top: 2rem;
        margin-bottom: 3rem;
    }
    .section-header h1 {
        font-size: 2.8rem !important;
        font-weight: 700;
        color: var(--primary-color) !important;
    }
    .section-header p {
        font-size: 1.2rem;
        color: var(--text-color);
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }

    /* --- Card Styles (for Projects, Blog, Pets) --- */
    .card {
        background-color: var(--card-bg);
        padding: 2rem;
        border-radius: 10px;
        margin-top: 1.5rem;
        border: 1px solid var(--border-color);
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.08);
    }
    .card h3 { margin-top: 0; }
    
    /* --- Specific "About Me" Styles --- */
    .intro-text { font-size: 1.1rem; line-height: 1.8; margin-top: 1rem; }
    .section-title {
        font-size: 1.8rem;
        font-weight: 600;
        color: var(--primary-color);
        margin-top: 2rem;
        margin-bottom: 1.5rem;
    }
    .icon-link { display: flex; align-items: center; gap: 15px; margin: 12px 0; font-size: 1.1rem; }
    .icon-link img { width: 24px; height: 24px; }

    /* --- Skill Bar Styles --- */
    .skill-item { margin-bottom: 1.2rem; display: flex; align-items: center; gap: 1rem; }
    .skill-name { font-weight: 600; width: 120px; }
    .skill-bar-container { width: 100%; background-color: #e9ecef; border-radius: 20px; height: 15px; overflow: hidden; }
    .skill-bar { height: 100%; border-radius: 20px; background-color: var(--primary-color); }
    .skill-level { font-size: 0.9rem; color: var(--secondary-color); font-style: italic; width: 100px; text-align: right; }
    
    /* --- Blog Navigation Styles --- */
    .blog-nav-arrows { display: flex; justify-content: space-between; margin-top: 1.5rem; }

    /* --- Custom Button Styles --- */
    .stButton > button {
        background-color: var(--primary-color); color: white; border: 2px solid var(--primary-color);
        border-radius: 25px; padding: 8px 20px; font-weight: 600; transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: var(--secondary-color); border-color: var(--secondary-color); color: white;
    }
    .stButton > button:disabled {
        background-color: #a88d83; color: #e0e0e0; border-color: #e0e0e0;
    }

    /* --- Footer --- */
    .footer { margin-top: 5rem; padding-bottom: 2rem; text-align: center; font-size: 0.9rem; color: var(--secondary-color); }
    </style>
""", unsafe_allow_html=True)


# --- DATA & HELPER FUNCTIONS ---

# Data for Blog Posts
blog_posts = [
    {
        "title": "How I Fell in Love with Coding", "date": "July 20, 2025",
        "content": "My journey into coding began with Scratch... a powerful tool to create meaningful impact."
    },
    {
        "title": "The Art of Problem Solving", "date": "July 28, 2025",
        "content": "At its core, programming is not about writing code; it's about solving problems... extends far beyond the world of software development."
    },
    {
        "title": "More Than a Pet: A Dog Named Betty", "date": "August 5, 2025",
        "content": "Some passions are discovered in a classroom... that dream, sparked by one wonderful dog, stays with me every day."
    }
]

# Data for Pet Adoption Dashboard (Self-contained CSV)
PET_DATA_STRING = """name,type,age,shelter,image_url,profile_url
Buddy,Dog,2,Charlie's Animal Rescue Centre (CARE),https://i.imgur.com/L42y5J3.jpg,https://www.charlies-care.com/
Misty,Cat,1,The Voice of Stray Dogs (VOSD),https://i.imgur.com/3ZUeF5j.jpg,https://vosd.in/
Rocky,Dog,5,Precious Paws Foundation,https://i.imgur.com/qLntFUm.jpg,https://preciouspawsfoundation.org/
Cleo,Cat,3,Animal Aid Alliance,https://i.imgur.com/8xL1vVd.jpg,https://animalaidalliance.org/
Max,Dog,4,Karuna Animal Shelter,https://i.imgur.com/w4i9e5p.jpg,https://karunaanimalshelter.org/
"""

@st.cache_data
def load_pet_data():
    return pd.read_csv(StringIO(PET_DATA_STRING))

# GitHub Activity Fetcher
@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_github_activity(username="akshatan17"):
    url = f"https://api.github.com/users/{username}/events/public"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Failed to fetch GitHub activity: {e}")
        return None

# Initialize Session State
if 'selected_blog' not in st.session_state:
    st.session_state.selected_blog = 0

# Reusable Functions
def section_header(title, subtitle):
    st.markdown(f'<div class="section-header"><h1>{title}</h1><p>{subtitle}</p></div>', unsafe_allow_html=True)

def skill_bar(name, level_percent, level_text):
    return f'<div class="skill-item"><div class="skill-name">{name}</div><div class="skill-bar-container"><div class="skill-bar" style="width: {level_percent}%;"></div></div><div class="skill-level">{level_text}</div></div>'

def display_image_gallery(folder_path):
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path, exist_ok=True)
        st.info(f"The folder '{folder_path}' was created. Add your images to see them here.")
        return

    image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))])
    
    if not image_files:
        st.info(f"No images found in the '{folder_path}' section yet. Check back soon!")
    else:
        cols = st.columns(3)
        for i, img_file in enumerate(image_files):
            with cols[i % 3]:
                st.image(os.path.join(folder_path, img_file), use_container_width=True)

# --- TAB DEFINITIONS ---
tab_titles = ["👤 About Me", "💻 Projects", "🐾 Find a Friend", "🎨 Art & More", "📜 Certificates", "✍️ Blog"]
tabs = st.tabs(tab_titles)

# --- ABOUT ME TAB ---
with tabs[0]:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2.5], gap="large")
    with col1:
        if os.path.exists("pfp.jpg"):
            st.image("pfp.jpg", use_container_width=True, output_format='JPEG')
        else:
            st.warning("Please add 'pfp.jpg' to your directory.")

    with col2:
        st.markdown("<h1 style='font-size: 3rem; margin-bottom: 0.5rem;'>Akshata Nagaraj</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #4e342e; margin-top: 0; font-weight: 400;'>Full Stack Developer | Creative Coder | Animal Lover</h3>", unsafe_allow_html=True)
        st.markdown("<p class='intro-text'>I’m a full stack developer who enjoys creating thoughtful, user-focused tools. Whether I’m coding something helpful or hanging out with animals, I love building things that make a difference.</p>", unsafe_allow_html=True)
        
        # Download Resume Button
        resume_path = "Akshata_Nagaraj_Resume.pdf"
        if os.path.exists(resume_path):
            with open(resume_path, "rb") as pdf_file:
                st.download_button(label="📄 Download My Resume", data=pdf_file.read(), file_name="Akshata_Nagaraj_Resume.pdf", mime='application/octet-stream')
        else:
            st.info("Add 'Akshata_Nagaraj_Resume.pdf' to enable the download button.")

    st.divider()

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("<div class='section-title'>🧠 Skills & Expertise</div>", unsafe_allow_html=True)
        st.markdown(skill_bar("Python", 90, "Advanced"), unsafe_allow_html=True)
        st.markdown(skill_bar("Java", 80, "Proficient"), unsafe_allow_html=True)
        st.markdown(skill_bar("HTML/CSS", 85, "Proficient"), unsafe_allow_html=True)
        st.markdown(skill_bar("SQL", 85, "Proficient"), unsafe_allow_html=True)
        st.markdown(skill_bar("C", 70, "Intermediate"), unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='section-title'>🔗 Connect & Activity</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class="icon-link">📧 <a href="mailto:akshatanagaraj1704@gmail.com">akshatanagaraj1704@gmail.com</a></div>
            <div class="icon-link">📞 +91 99025 83700</div>
            <div class="icon-link"><img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="GitHub"><a href="https://github.com/akshatan17" target="_blank">GitHub</a></div>
            <div class="icon-link"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn"><a href="https://www.linkedin.com/in/akshata-nagaraj-4147842b8/" target="_blank">LinkedIn</a></div>
            """, unsafe_allow_html=True)

        st.markdown("<h5 style='margin-top:2rem; color: var(--primary-color);'>🧑‍💻 Latest GitHub Activity</h5>", unsafe_allow_html=True)
        activity = get_github_activity()
        if activity:
            for event in activity[:3]:
                event_type = event['type'].replace("Event", "")
                repo_name = event['repo']['name']
                st.markdown(f"*{event_type}* on **{repo_name}**")
        else:
            st.write("Could not load GitHub activity.")

    st.markdown('</div>', unsafe_allow_html=True)

# --- PROJECTS TAB ---
with tabs[1]:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    section_header("My Projects", "A selection of my recent work and explorations in code.")
    
    st.markdown("<div class='card'><h3>🔍 RAG PDF Assistant (Hiveminds Internship)</h3><p>I developed a full-stack Retrieval-Augmented Generation (RAG) application to allow users to chat with their PDF documents. I handled the backend logic for document processing, integrated the Gemini AI API, and built the UI with Streamlit.</p><p><strong>Technologies:</strong> Python, Streamlit, Gemini AI, LangChain, RAG</p></div>", unsafe_allow_html=True)

    st.markdown("<div class='card'><h3>😊 Real-Time Facial Expression Detector</h3><p>I built a Python application using OpenCV to capture video and a pre-trained CNN model to analyze and classify facial expressions like 'Happy', 'Sad', and 'Neutral' in real-time.</p><p><strong>Technologies:</strong> Python, OpenCV, TensorFlow/Keras</p>", unsafe_allow_html=True)
    
    # --- Code Snippet Showcase ---
    with st.expander("Explore a code snippet from this project"):
        st.markdown("This function uses OpenCV to draw a bounding box and put the detected emotion text on the video frame.")
        st.code("""
import cv2
def draw_on_frame(frame, face_coords, emotion_text):
    (x, y, w, h) = face_coords
    # Draw rectangle around the face
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # Put the emotion text above the rectangle
    cv2.putText(frame, emotion_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    return frame
        """, language="python")

    st.markdown("<div class='card'><h3>📚 EduTech Flashcard Generator</h3><p>An automation script that parses PDF textbooks using PyMuPDF to identify key terms and their definitions, automatically generating a printable set of flashcards to streamline studying.</p><p><strong>Technologies:</strong> Python, PyMuPDF, NLP (basic pattern matching)</p></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- FIND A FRIEND TAB ---
with tabs[2]:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    section_header("Find a Friend", "A showcase of some lovely animals from Bengaluru shelters waiting for a home. <br><i>This is a demo using representative data.</i>")
    
    pet_df = load_pet_data()
    animal_type = st.selectbox("Filter by animal type:", ["All"] + list(pet_df['type'].unique()))

    if animal_type != "All":
        filtered_df = pet_df[pet_df['type'] == animal_type]
    else:
        filtered_df = pet_df

    for _, row in filtered_df.iterrows():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        c1, c2 = st.columns([1, 2.5], gap="large")
        with c1:
            st.image(row['image_url'])
        with c2:
            st.markdown(f"### {row['name']}")
            st.markdown(f"**{row['type']} • {row['age']} years old**")
            st.markdown(f"At **{row['shelter']}**")
            st.link_button("Learn More & Adopt ↗️", row['profile_url'])
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- ART & MORE TAB ---
with tabs[3]:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    section_header("Art & More", "My creative side, from digital art to photography and generative coding.")
    
    st.markdown("<div class='section-title' style='text-align:center;'>🎨 Generative Art Playground</div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Play with the controls below to create your own unique patterns!</p>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        seed = st.slider("Drag to change the pattern", 1, 100, 42, key="art_seed")
    with c2:
        color_map = st.selectbox("Select a color scheme", ["viridis", "plasma", "inferno", "magma", "cividis"])

    # Generate the art
    rng = np.random.default_rng(seed)
    size = 256
    data = np.zeros((size, size))
    for _ in range(rng.integers(10, 50)):
        x, y = rng.integers(0, size, 2)
        sx, sy = rng.integers(10, 80, 2)
        amp = rng.random() * 2
        data[max(0, x-sx):min(size, x+sx), max(0, y-sy):min(size, y+sy)] += amp
    
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(data, cmap=color_map, interpolation='quadric')
    ax.axis('off')
    st.pyplot(fig)

    st.divider()
    
    with st.expander("🖼️ View My Artworks Gallery"):
        display_image_gallery("artworks")
        
    with st.expander("📷 View My Photo Gallery"):
        display_image_gallery("photos")
        
    st.markdown('</div>', unsafe_allow_html=True)

# --- CERTIFICATES TAB ---
with tabs[4]:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    section_header("My Certificates", "A collection of my professional certifications.")
    display_image_gallery("certificates")
    st.markdown('</div>', unsafe_allow_html=True)

# --- BLOG TAB ---
with tabs[5]:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    section_header("Personal Blog", "Thoughts, reflections, and stories from my journey.")
    
    selected_index = st.session_state.selected_blog
    selected_post = blog_posts[selected_index]
    
    st.markdown(f"<div class='card'><div class='blog-content'><h3>{selected_post['title']}</h3><em>Published: {selected_post['date']}</em><hr><p>{selected_post['content']}</p></div></div>", unsafe_allow_html=True)
    
    prev_col, counter_col, next_col = st.columns([2, 8, 1.8])
    if prev_col.button("⬅️ Previous Post", use_container_width=True, disabled=(selected_index <= 0)):
        st.session_state.selected_blog -= 1
        st.rerun()
    counter_col.markdown(f"<p style='text-align: center; margin-top: 0.5rem;'>Post {selected_index + 1} of {len(blog_posts)}</p>", unsafe_allow_html=True)
    if next_col.button("Next Post ➡️", use_container_width=True, disabled=(selected_index >= len(blog_posts) - 1)):
        st.session_state.selected_blog += 1
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown('<div class="footer">Made with ❤️ & Python using Streamlit | © 2025 Akshata Nagaraj</div>', unsafe_allow_html=True)