import streamlit as st

# Set page configuration
st.set_page_config(page_title="Ms. Sana Mateen's Portfolio", page_icon=":woman_teacher:", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
            color: #007bff;
            margin-bottom: 10px;
        }
        .header {
            text-align: center;
            font-size: 1.8em;
            color: #495057;
        }
        .section-title {
            font-size: 1.5em;
            font-weight: bold;
            color: #198754;
            border-bottom: 2px solid #198754;
            padding-bottom: 5px;
            margin-top: 20px;
        }
        .custom-list li {
            font-size: 1.2em;
            margin-bottom: 8px;
            padding: 8px;
            background-color: #e9ecef;
            border-radius: 5px;
            transition: all 0.3s;
        }
        .custom-list li:hover {
            background-color: #d4edda;
        }
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
st.sidebar.image("./prof.jpg", caption="Ms. Sana Mateen", use_container_width=True)


# About Me Section
with st.expander("📌 About Me", expanded=True):
    st.write("""
    I am an **Assistant Professor** in the **CSE Department** at the **College of Engineering and Technology** with **6 years** of experience.
    I hold a **Master’s Degree** in **Computer Science** from **Shadan Women's College of Engineering and Technology**.
    I am proficient in **Python**, **Perl**, **Java**, and the **MERN Stack**. I am passionate about **Ethical Hacking** and **Cybersecurity**.
    """)

# Highlights Section
with st.expander("🏆 Highlights", expanded=True):
    st.write("""
    - ✅ **UGC NET 2025** Qualified Assistant Professor in **Computer Science**.
    - ✅ **TSSET** Qualified Assistant Professor in **Computer Science**.
    """)

# Skills Section
with st.expander("💻 Skills", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🛠 Technical Skills")
        st.write("""
        - 🐍 Python  
        - 📊 Machine Learning  
        - 📐 SKLEARN  
        - 📊 MATPLOTLIB  
        - 🔢 NUMPY  
        - 📚 PANDAS  
        """)
    with col2:
        st.subheader("🌐 Web Development Skills")
        st.write("""
        - ☕ Java  
        - 💻 MERN Stack  
        - 💾 MYSQL  
        - ⚛️ React  
        - 🚀 Node.js  
        - 🌐 Express.js  
        """)

# Ethical Hacking Tools
with st.expander("🛡 Ethical Hacking Tools", expanded=False):
    ethical_hacking_tools = [
        "🔍 Nmap", "🔧 Metasploit Framework", "🔒 Nikto",
        "🐞 Burp Suite", "🛠 SQLMap", "📷 Wireshark", "🛡️ Nessus"
    ]
    for tool in ethical_hacking_tools:
        st.write(f"- {tool}")

# NPTEL Certifications
with st.expander("📜 NPTEL Certifications & Achievements", expanded=False):
    nptel_certifications = [
        "🏆 Top 2% in Joy of Computing using Python",
        "📊 Top 2% in Python for Data Science",
        "🤖 Top 5% in Introduction to Machine Learning",
        "🛡️ NPTEL Elite Certification in Ethical Hacking",
        "💻 NPTEL Elite Certification in Machine Learning (Hindi)",
        "☕ NPTEL Elite Certification in Programming in Java"
    ]
    for cert in nptel_certifications:
        st.write(f"- {cert}")

# GitHub Repositories
with st.expander("📂 Top GitHub Repositories", expanded=False):
    repositories = [
        {"name": "Artificial Intelligence", "description": "Used libraries like Pandas, NumPy, and Matplotlib.", "url": "https://github.com/mssanamateen/Artificial-Intelligence-Lab"},
        {"name": "Machine-Learning-Models", "description": "A collection of machine learning models implemented using Python and Scikit-learn.", "url": "https://github.com/mssanamateen/Mathematical-Foundations-of-ML"}
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
