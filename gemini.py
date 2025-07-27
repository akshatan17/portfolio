import streamlit as st
import os

# --- Page Config ---
st.set_page_config(
    page_title="Akshata Nagaraj | Portfolio",
    layout="wide",
    page_icon="🌿"
)

# --- Custom CSS for Enhanced UI ---
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
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* --- Tab Styles --- */
    .stTabs [role="tablist"] {
        justify-content: center;
        gap: 2rem;
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
    
    /* --- General Content Styles --- */
    .tab-title {
        text-align: center;
        font-size: 2.8rem !important;
        font-weight: 700;
        color: var(--primary-color) !important;
        padding-top: 2rem;
    }
    .tab-subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: var(--text-color);
        margin-bottom: 3rem;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
    }

    /* --- Card Styles (for Projects & Blog) --- */
    .project-card {
        background-color: var(--card-bg);
        padding: 2rem;
        border-radius: 10px;
        margin-top: 1.5rem;
        border: 1px solid var(--border-color);
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.08);
    }
    .project-card h3 { margin-top: 0; }
    .project-links a { margin-right: 15px; font-size: 1rem; }
    
    /* --- Specific Element Styles for "About Me" --- */
    .profile-pic {
        border-radius: 50%;
        object-fit: cover;
        width: 180px;
        height: 180px;
        border: 5px solid var(--card-bg);
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .intro-text {
        font-size: 1.1rem;
        line-height: 1.8;
        margin-top: 1rem;
    }
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
    
    /* --- NEW Blog Navigation Styles --- */
    .blog-container {
        max-width: 800px;
        margin: auto;
    }
    .blog-content h3 { margin-top: 0; }
    .blog-content em { color: var(--secondary-color); }
    .blog-nav-arrows {
        display: flex;
        justify-content: space-between;
        margin-top: 1.5rem;
    }

    /* --- Footer --- */
    .footer { margin-top: 5rem; padding-bottom: 2rem; text-align: center; font-size: 0.9rem; color: var(--secondary-color); }
    /* --- Custom Button Styles for Blog Navigation --- */
.stButton > button {
    background-color: var(--primary-color);
    color: white;
    border: 2px solid var(--primary-color);
    border-radius: 25px;
    padding: 8px 20px;
    font-weight: 600;
    transition: all 0.3s ease;
}
/*Buttons*/
.stButton > button:hover {
    background-color: var(--secondary-color);
    border-color: var(--secondary-color);
    color: white;
}

.stButton > button:disabled {
    background-color: #a88d83;
    color: #a0a0a0;
    border-color: #e0e0e0;
}
    </style>
""", unsafe_allow_html=True)

# --- Data for Blog Posts ---
blog_posts = [
    {
        "title": "How I Fell in Love with Coding",
        "date": "July 20, 2025",
        "content": """
        My journey into coding began with Scratch — a playful platform where I first discovered how logic and creativity come together. What started as dragging colorful blocks to animate stories soon sparked a deeper curiosity about how things work beneath the surface.
        <br><br>
        As I moved on from Scratch to real-world programming languages, I faced the same initial hurdles: confusing syntax, cryptic errors, and code that refused to run. But gradually, I realized coding wasn’t just about getting things right; it was about problem-solving. Each bug challenged me, each project pushed my creativity. Watching an idea take shape into a working application felt nothing short of empowering — a way to build, create, and make things happen.
        <br><br>
        More than the technical skills, I fell in love with the community — the collaboration, the constant exchange of ideas, and the ever-evolving tech landscape. Today, coding is more than just a skill for me. It’s a passion, a platform to innovate, and a powerful tool to create meaningful impact.
        """
    },
    {
        "title": "The Art of Problem Solving",
        "date": "July 28, 2025",
        "content": """
        At its core, programming is not about writing code; it's about solving problems. The code is just the tool we use to implement the solution. I've learned that the most effective developers are not the ones who know the most syntax, but the ones who are best at breaking down complex challenges into small, manageable steps.
        <br><br>
        My process always starts with a pen and paper, not a keyboard. I sketch out the logic, define the inputs and outputs, and consider the edge cases. This "low-tech" approach saves countless hours of debugging later on. It forces clarity of thought before a single line of code is written.
        <br><br>
        This methodical approach has been invaluable, whether I'm designing a database schema, building an API, or debugging a tricky UI issue. It's a universal skill that extends far beyond the world of software development.
        """
    },
    {
        "title": "More Than a Pet: A Dog Named Betty",
        "date": "August 5, 2025",
        "content": """
        Some passions are discovered in a classroom or a workshop, but my love for animals began with a wagging tail and the warmest, most trusting eyes I had ever seen. It began with Betty, my cousin's dog. I remember being a child, and the sheer joy she would radiate was infectious. She wasn't just a pet; she was family. I loved her with all my heart.
        <br><br>
        Betty was my gateway. Through her, I learned the language of unconditional love and loyalty. That profound connection didn't just make me a dog lover; it opened my eyes and my heart to all animals. I began to see the same spark of life, the same capacity for feeling, in every creature. Caring for them, whether it's a stray cat on the street or a bird with a broken wing, feels like the most natural thing in the world to me.
        <br><br>
        This love has grown into a lifelong dream. One day, I hope to establish my own NGO dedicated to animal welfare—a sanctuary for the voiceless that provides shelter, medical care, and a voice for those who cannot speak for themselves. That dream, sparked by one wonderful dog, stays with me every day.
        """
    }
]

# --- Initialize Session State for Blog ---
if 'selected_blog' not in st.session_state:
    st.session_state.selected_blog = 0

# --- Reusable function for skill bars ---
def skill_bar(name, level_percent, level_text):
    return f"""
    <div class="skill-item">
        <div class="skill-name">{name}</div>
        <div class="skill-bar-container"><div class="skill-bar" style="width: {level_percent}%;"></div></div>
        <div class="skill-level">{level_text}</div>
    </div>
    """

# --- Tab Definitions ---
tab_titles = ["👤 About Me", "💻 Projects", "🎨 Artworks", "📷 Photos", "📜 Certificates", "✍️ Blog"]
tabs = st.tabs(tab_titles)

# --- ABOUT ME TAB ---
with tabs[0]:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2.5], gap="large")
    with col1:
        if os.path.exists("pfp.jpg"):
            st.image("pfp.jpg", use_container_width=True, output_format='JPEG')
        else:
            st.markdown('<div style="width:180px; height:180px; background-color:#ddd; border-radius:50%; display:flex; align-items:center; justify-content:center; text-align:center; font-size:1rem; color:#555;">Your Photo Here</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("<h1 style='font-size: 3rem; margin-bottom: 0.5rem;'>Akshata Nagaraj</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #4e342e; margin-top: 0; font-weight: 400;'>Full Stack Developer | Creative Coder | Animal Lover</h3>", unsafe_allow_html=True)
        st.markdown("<p class='intro-text'>I’m a full stack developer who enjoys creating thoughtful, user-focused tools. Whether I’m coding something helpful or hanging out with animals, I love building things that make a difference.</p>", unsafe_allow_html=True)
    
    st.divider()

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("<div class='section-title'>🧠 Skills & Expertise</div>", unsafe_allow_html=True)
        st.markdown("<h5>Languages 🧑‍💻</h5>", unsafe_allow_html=True)
        st.markdown(skill_bar("Python", 90, "Advanced"), unsafe_allow_html=True)
        st.markdown(skill_bar("Java", 80, "Proficient"), unsafe_allow_html=True)
        st.markdown(skill_bar("HTML/CSS", 85, "Proficient"), unsafe_allow_html=True)
        st.markdown(skill_bar("C", 70, "Intermediate"), unsafe_allow_html=True)
        
        st.markdown("<h5 style='margin-top: 2rem;'>Databases 💾</h5>", unsafe_allow_html=True)
        st.markdown(skill_bar("SQL", 85, "Proficient"), unsafe_allow_html=True)
        st.markdown(skill_bar("MySQL", 80, "Proficient"), unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='section-title'>🔗 Connect with Me</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class="icon-link"><img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" alt="GitHub"><a href="https://github.com/akshatan17" target="_blank">GitHub</a></div>
            <div class="icon-link"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn"><a href="https://www.linkedin.com/in/akshata-nagaraj-4147842b8/" target="_blank">LinkedIn</a></div>
            <div class="icon-link"><img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" alt="Instagram"><a href="https://instagram.com/akshata_1704" target="_blank">Instagram</a></div>
            <div class="icon-link">📧 <a href="mailto:akshatanagaraj1704@gmail.com">akshatanagaraj1704@gmail.com</a></div>
            <div class="icon-link">📞 +91 99025 83700</div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# --- PROJECTS TAB ---
with tabs[1]:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("<h1 class='tab-title'>My Projects</h1>", unsafe_allow_html=True)
    st.markdown("<p class='tab-subtitle'>A selection of my recent work and explorations in code.</p>", unsafe_allow_html=True)
    st.markdown("""
    <div class='project-card'>
        <h3>🔍 RAG PDF Assistant (Hiveminds Internship)</h3>
        <p><strong>Problem & Goal:</strong> Users needed a way to quickly find answers within large PDF documents without reading them entirely. The goal was to build an intuitive chat-based interface for this purpose.</p>
        <p><strong>My Role & Solution:</strong> I developed a full-stack Retrieval-Augmented Generation (RAG) application. I handled the backend logic in Python for document processing and chunking, integrated the Gemini AI API for question-answering, and built the user interface with Streamlit. The tool allows users to upload a PDF and interact with a chatbot to get instant, context-aware answers.</p>
        <p><strong>Outcome:</strong> The final product is a highly responsive and user-friendly tool that significantly speeds up information retrieval from dense documents.</p>
        <p><strong>Technologies:</strong> Python, Streamlit, Gemini AI, LangChain, RAG</p>
    </div>
    <div class='project-card'>
        <h3>😊 Real-Time Facial Expression Detector</h3>
        <p><strong>Problem & Goal:</strong> To explore the practical application of computer vision and machine learning by creating a tool that can recognize human emotions from a live video feed.</p>
        <p><strong>My Role & Solution:</strong> I built a Python application using OpenCV to capture video from a webcam. I then integrated a pre-trained deep learning model (based on CNNs) to analyze facial landmarks and classify expressions into categories like 'Happy', 'Sad', 'Neutral', and 'Surprised'. The app overlays the detected emotion directly onto the video feed in real-time.</p>
        <p><strong>Outcome:</strong> A functional proof-of-concept that accurately identifies basic emotions, serving as a strong foundation for more complex affective computing projects.</p>
        <p><strong>Technologies:</strong> Python, OpenCV, TensorFlow/Keras, Machine Learning</p>
    </div>
    <div class='project-card'>
        <h3>📚 EduTech Flashcard Generator</h3>
        <p><strong>Problem & Goal:</strong> Students often spend hours manually creating flashcards from their study materials. This project aimed to automate the process by generating flashcards directly from PDF textbooks or notes.</p>
        <p><strong>My Role & Solution:</strong> I developed a Python script that uses PDF parsing libraries (like PyMuPDF) to extract text content. I then implemented a simple algorithm to identify key terms and their corresponding definitions (e.g., bolded words and the following sentence) to structure them as flashcards. The output is a clean, printable set of study cards.</p>
        <p><strong>Outcome:</strong> The tool effectively automates a tedious study task, allowing students to generate learning materials in minutes instead of hours.</p>
        <p><strong>Technologies:</strong> Python, PyMuPDF, NLP (basic pattern matching)</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Reusable function for image galleries ---
def display_image_gallery(folder_path, title, subtitle):
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown(f"<h1 class='tab-title'>{title}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='tab-subtitle'>{subtitle}</p>", unsafe_allow_html=True)
    if not os.path.isdir(folder_path):
        st.warning(f"The folder '{folder_path}' was not found. Please create it and add your images.")
        st.markdown('</div>', unsafe_allow_html=True)
        return
    image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))])
    if not image_files:
        st.info("No images found in this section yet. Check back soon!")
    else:
        for i in range(0, len(image_files), 3):
            cols = st.columns(3, gap="medium")
            for j in range(3):
                if i + j < len(image_files):
                    img_path = os.path.join(folder_path, image_files[i + j])
                    with cols[j]:
                        st.image(img_path, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Calling the function for each image tab ---
with tabs[2]:
    display_image_gallery("artworks", "My Artworks", "A gallery of my creative pieces.")
with tabs[3]:
    display_image_gallery("photos", "Photo Gallery", "A few moments from my life.")
with tabs[4]:
    display_image_gallery("certificates", "My Certificates", "A collection of my professional certifications.")

# --- BLOG TAB ---
with tabs[5]:
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown("<h1 class='tab-title'>Personal Blog</h1>", unsafe_allow_html=True)
    st.markdown("<p class='tab-subtitle'>Thoughts, reflections, and stories from my journey.</p>", unsafe_allow_html=True)

    # --- Container for the blog post and navigation ---
    st.markdown("<div class='blog-container'>", unsafe_allow_html=True)
    
    # Display the selected blog post
    selected_post = blog_posts[st.session_state.selected_blog]
    st.markdown(f"""
    <div class="project-card">
        <div class="blog-content">
            <h3>{selected_post['title']}</h3>
            <em>Published: {selected_post['date']}</em>
            <hr>
            <p>{selected_post['content']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- Arrow Navigation ---
    st.markdown("<div class='blog-nav-arrows'>", unsafe_allow_html=True)
    
    # Create columns for the buttons
    prev_col, counter_col, next_col = st.columns([2, 8, 1.5])

    with prev_col:
        if st.session_state.selected_blog > 0:
            if st.button("⬅️ Previous Post"):
                st.session_state.selected_blog -= 1
                st.rerun()

    with counter_col:
        st.markdown(f"<p style='text-align: center; margin-top: 0.5rem;'>{st.session_state.selected_blog + 1} of {len(blog_posts)}</p>", unsafe_allow_html=True)

    with next_col:
        if st.session_state.selected_blog < len(blog_posts) - 1:
            if st.button("Next Post ➡️"):
                st.session_state.selected_blog += 1
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True) # Close blog-nav-arrows
    st.markdown("</div>", unsafe_allow_html=True) # Close blog-container
    st.markdown('</div>', unsafe_allow_html=True) # Close fade-in

# --- Footer ---
st.markdown("""
<div class="footer">
Made with ❤️ & Python using Streamlit | © 2025 Akshata Nagaraj 
</div>
""", unsafe_allow_html=True)