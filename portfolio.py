import streamlit as st

# Set the page config (Optional: You can set a custom icon, layout, etc.)
st.set_page_config(page_title="Ms. Sana Mateen's Portfolio", page_icon=":woman_teacher:", layout="wide")

# Title and Header Section
st.title("Welcome to My Portfolio :wave:")
st.header("Ms. Sana Mateen")
st.subheader("Assistant Professor | CSE Department | College of Engineering and Technology")

# Add a profile picture
st.sidebar.image("./prof.jpg", width=150)  # Replace with your own image URL

# About Me Section
st.markdown("""
I am an **Assistant Professor** in the **CSE Department** at the **College of Engineering and Technology** with **6 years** of experience.
I hold a **Master’s Degree** in **Computer Science** from **Shadan Women's College of Engineering and Technology**.  
I am proficient in **Python**, **Perl**, **Java**, and the **MERN Stack**.  
I am passionate about **Ethical Hacking** and **Cybersecurity** and love helping students learn and grow in these fields.
""")

# Highlights Section
st.markdown("### Highlights")
st.markdown("""
- **UGC NET 2025** Qualified Assistant Professor in **Computer Science**.
- **TSSET** Qualified for Assistant Professor.
""")

# Skills Section with Icons in Two Columns
st.header("Skills")

# Create two columns for skills
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Technical Skills")
    skills_col1 = {
        "Python": "🐍", 
        "Machine Learning": "📊", 
        "SKLEARN": "📐", 
        "MATPLOTLIB": "📊", 
        "NUMPY": "🔢", 
        "PANDAS": "📚"
    }
    for skill, icon in skills_col1.items():
        st.markdown(f"- {icon} **{skill}**")

with col2:
    st.markdown("### Web Development Skills")
    skills_col2 = {
        "Java": "☕", 
        "MERN Stack": "💻", 
        "MYSQL": "💾", 
        "React": "⚛️", 
        "Node.js": "🚀", 
        "Express.js": "🌐"
    }
    for skill, icon in skills_col2.items():
        st.markdown(f"- {icon} **{skill}**")

# Ethical Hacking Tools Section
st.header("Ethical Hacking Tools")
st.markdown("""
As part of my **Cybersecurity** and **Ethical Hacking** passion, I have hands-on experience with the following tools:
""")

ethical_hacking_tools = [
    "Nmap :mag_right:", 
    "Metasploit Framework :wrench:", 
    "Nikto :lock:", 
    "Burp Suite :bug:", 
    "SQLMap :hammer:", 
    "Wireshark :camera:", 
    "Nessus :shield:"
]

for tool in ethical_hacking_tools:
    st.markdown(f"- {tool}")

# NPTEL Certifications Section with Icons
st.header("NPTEL Certifications & Achievements")
st.markdown("""
I have achieved the following **NPTEL** certifications and accomplishments:
""")

# NPTEL Achievements with Icons
nptel_certifications = [
    {"name": "Top 2% in Joy of Computing using Python", "icon": "🏆"},
    {"name": "Top 2% in Python for Data Science", "icon": "📊"},
    {"name": "Top 5% in Introduction to Machine Learning", "icon": "🤖"},
    {"name": "NPTEL Elite Certification in Ethical Hacking", "icon": "🛡️"},
    {"name": "NPTEL Elite Certification in Machine Learning (Hindi)", "icon": "💻"},
    {"name": "NPTEL Elite Certification in Programming in Java", "icon": "☕"}
]

for cert in nptel_certifications:
    st.markdown(f'<p style="font-size: 14px;">{cert["icon"]} {cert["name"]}</p>', unsafe_allow_html=True)


# Certifications Section (Other Certifications)
st.header("Other Certifications")
st.write("Here are some of my certifications from LinkedIn and other platforms:")

# Example Certifications
certifications = [
    {
        "name": "Ethical Hacking and Cybersecurity",
        "issued_by": "LinkedIn",
    },
    {
        "name": "Data Science and Machine Learning",
        "issued_by": "Coursera",
    },
    {
        "name": "Full Stack Web Development",
        "issued_by": "Udemy",
    }
]

# Display Certifications
for cert in certifications:
    st.markdown(f"### {cert['name']}")
    st.markdown(f"- **Issued by**: {cert['issued_by']}")

# Subjects Taught Section
st.header("Subjects Taught")
st.markdown("""
As an **Assistant Professor** in the **CSE Department**, I have taught the following subjects:
""")

# List of Subjects Taught
subjects_taught = [
    "Cybersecurity",
    "Java Programming",
    "Web Technologies",
    "Artificial Intelligence (AI)",
    "Machine Learning (ML)",
    "Computer Networks (CN)",
    "Internet of Things (IoT)",
    "CCNA",
    "Database Management Systems (DBMS)"
]

# Display Subjects
for subject in subjects_taught:
    st.markdown(f"- **{subject}**")

# Top GitHub Repositories Section
st.header("Top GitHub Repositories")
st.write("Here are some of my top repositories on GitHub:")

# List of top repositories
repositories = [
    {
        "name": "Artificial Intelligence",
        "description": "As part of curriculum used libraries like Pandas, NumPy, and Matplotlib.",
        "url": "https://github.com/mssanamateen/Artificial-Intelligence-Lab"
    },
 
    {
        "name": "Machine-Learning-Models",
        "description": "A collection of machine learning models and algorithms implemented using Python and Scikit-learn.",
        "url": "https://github.com/mssanamateen/Mathematical-Foundations-of-ML"
    },
]

# Display Repositories
for repo in repositories:
    st.subheader(f"[{repo['name']}]({repo['url']})")
    st.write(f"{repo['description']}")
    
# Add a link to GitHub for more projects
st.markdown("[Visit my GitHub for more projects](https://github.com/mssanamateen)")


# Footer Section with Social Media Links (Optional)
st.markdown("""
---
Connect with me:
- [LinkedIn](https://www.linkedin.com/in/sana-mateen-6a15b05a/)
- [GitHub](https://github.com/mssanamateen)
""")
