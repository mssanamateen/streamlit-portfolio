import streamlit as st

# Set page config
st.set_page_config(page_title="Ms. Sana Mateen's Portfolio", page_icon=":woman_teacher:", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
        /* Background and text color */
        body {
            background-color: #f8f9fa;
            color: #343a40;
        }
        /* Center title */
        .title {
            text-align: center;
            color: #007bff;
            font-size: 2.5em;
            font-weight: bold;
        }
        /* Header styling */
        .header {
            text-align: center;
            font-size: 1.8em;
            color: #495057;
        }
        /* Profile image */
        .profile-pic {
            display: block;
            margin: 0 auto;
            border-radius: 50%;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
        }
        /* Section titles */
        .section-title {
            font-size: 1.5em;
            font-weight: bold;
            color: #198754;
            border-bottom: 2px solid #198754;
            padding-bottom: 5px;
        }
        /* List styling */
        .custom-list {
            list-style-type: none;
            padding-left: 0;
        }
        .custom-list li {
            font-size: 1.2em;
            margin-bottom: 8px;
            padding: 8px;
            background-color: #e9ecef;
            border-radius: 5px;
        }
        /* Footer */
        .footer {
            text-align: center;
            font-size: 1.2em;
            padding-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Header Section
st.markdown('<p class="title">Welcome to My Portfolio 👋</p>', unsafe_allow_html=True)
st.markdown('<p class="header">Ms. Sana Mateen</p>', unsafe_allow_html=True)
st.markdown('<p class="header">Assistant Professor | CSE Department | College of Engineering and Technology</p>', unsafe_allow_html=True)

# Sidebar - Profile Image
st.sidebar.image("./prof.jpg", width=150, caption="Ms. Sana Mateen", use_container_width=True)


# About Me Section
st.markdown('<p class="section-title">About Me</p>', unsafe_allow_html=True)
st.markdown("""
I am an **Assistant Professor** in the **CSE Department** at the **College of Engineering and Technology** with **6 years** of experience.  
I hold a **Master’s Degree** in **Computer Science** from **Shadan Women's College of Engineering and Technology**.  
I am proficient in **Python**, **Perl**, **Java**, and the **MERN Stack**.  
I am passionate about **Ethical Hacking** and **Cybersecurity** and love helping students learn and grow in these fields.
""")

# Highlights Section
st.markdown('<p class="section-title">Highlights</p>', unsafe_allow_html=True)
st.markdown("""
- ✅ **UGC NET 2025** Qualified Assistant Professor in **Computer Science**.
- ✅ **TSSET** Qualified for Assistant Professor.
""")

# Skills Section
st.markdown('<p class="section-title">Skills</p>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🛠 Technical Skills")
    st.markdown("""
    - 🐍 **Python**  
    - 📊 **Machine Learning**  
    - 📐 **SKLEARN**  
    - 📊 **MATPLOTLIB**  
    - 🔢 **NUMPY**  
    - 📚 **PANDAS**  
    """)

with col2:
    st.markdown("### 🌐 Web Development Skills")
    st.markdown("""
    - ☕ **Java**  
    - 💻 **MERN Stack**  
    - 💾 **MYSQL**  
    - ⚛️ **React**  
    - 🚀 **Node.js**  
    - 🌐 **Express.js**  
    """)

# Ethical Hacking Tools
st.markdown('<p class="section-title">Ethical Hacking Tools</p>', unsafe_allow_html=True)
ethical_hacking_tools = [
    "🔍 Nmap",
    "🔧 Metasploit Framework",
    "🔒 Nikto",
    "🐞 Burp Suite",
    "🛠 SQLMap",
    "📷 Wireshark",
    "🛡️ Nessus"
]

st.markdown('<ul class="custom-list">' + ''.join([f"<li>{tool}</li>" for tool in ethical_hacking_tools]) + '</ul>', unsafe_allow_html=True)

# NPTEL Certifications
st.markdown('<p class="section-title">NPTEL Certifications & Achievements</p>', unsafe_allow_html=True)
nptel_certifications = [
    "🏆 Top 2% in Joy of Computing using Python",
    "📊 Top 2% in Python for Data Science",
    "🤖 Top 5% in Introduction to Machine Learning",
    "🛡️ NPTEL Elite Certification in Ethical Hacking",
    "💻 NPTEL Elite Certification in Machine Learning (Hindi)",
    "☕ NPTEL Elite Certification in Programming in Java"
]
st.markdown('<ul class="custom-list">' + ''.join([f"<li>{cert}</li>" for cert in nptel_certifications]) + '</ul>', unsafe_allow_html=True)

# Other Certifications
st.markdown('<p class="section-title">Other Certifications</p>', unsafe_allow_html=True)
other_certifications = [
    "🔐 Ethical Hacking and Cybersecurity - LinkedIn",
    "📊 Data Science and Machine Learning - Coursera",
    "💻 Full Stack Web Development - Udemy"
]
st.markdown('<ul class="custom-list">' + ''.join([f"<li>{cert}</li>" for cert in other_certifications]) + '</ul>', unsafe_allow_html=True)

# Subjects Taught
st.markdown('<p class="section-title">Subjects Taught</p>', unsafe_allow_html=True)
subjects_taught = [
    "🔒 Cybersecurity",
    "☕ Java Programming",
    "🌐 Web Technologies",
    "🤖 Artificial Intelligence",
    "📊 Machine Learning",
    "🔗 Computer Networks",
    "🌎 Internet of Things (IoT)",
    "🖥️ CCNA",
    "💾 Database Management Systems (DBMS)"
]
st.markdown('<ul class="custom-list">' + ''.join([f"<li>{subject}</li>" for subject in subjects_taught]) + '</ul>', unsafe_allow_html=True)

# GitHub Repositories
st.markdown('<p class="section-title">Top GitHub Repositories</p>', unsafe_allow_html=True)
repositories = [
    {
        "name": "Artificial Intelligence",
        "description": "As part of curriculum used libraries like Pandas, NumPy, and Matplotlib.",
        "url": "https://github.com/mssanamateen/Artificial-Intelligence-Lab"
    },
    {
        "name": "Machine-Learning-Models",
        "description": "A collection of machine learning models implemented using Python and Scikit-learn.",
        "url": "https://github.com/mssanamateen/Mathematical-Foundations-of-ML"
    }
]

for repo in repositories:
    st.markdown(f"🔗 **[{repo['name']}]({repo['url']})** - {repo['description']}")

st.markdown("[👉 Visit my GitHub for more projects](https://github.com/mssanamateen)")

# Footer
st.markdown("""
    <p class="footer">
        🔗 Connect with me: 
        <a href="https://www.linkedin.com/in/sana-mateen-6a15b05a/" target="_blank">LinkedIn</a> |
        <a href="https://github.com/mssanamateen" target="_blank">GitHub</a>
    </p>
""", unsafe_allow_html=True)

