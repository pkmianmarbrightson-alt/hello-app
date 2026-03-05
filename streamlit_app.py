import streamlit as st

st.set_page_config(page_title="Mianmar Brightson Portfolio", page_icon="💻", layout="wide")

# PROFILE SECTION
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("photo.jpeg", width=200)   # put your photo in same folder
    st.markdown("<h1 style='text-align:center;'>Mianmar Brightson P K</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;color:gray;'>Python Developer | Aspiring IT Professional</h3>", unsafe_allow_html=True)

st.markdown("---")

# ABOUT
st.header("Profile")

st.write("""
A passionate IT fresher looking for an opportunity to start my career in a challenging environment.
I aim to enhance my technical knowledge and develop practical skills while contributing to team success.
""")

st.markdown("---")

# EDUCATION
st.header("Education")

col1, col2 = st.columns(2)

with col1:
    st.subheader("BA Economics")
    st.write("Bharath Institute of Higher Education and Research")
    st.write("2022 - 2025 | 70%")

with col2:
    st.subheader("HSC")
    st.write("Perunthalaivar Kamarajar Matriculation HS School")
    st.write("2019 - 2020 | 68%")

st.markdown("---")

# SKILLS
st.header("Technical Skills")

skills = [
    "Python", "SQL", "HTML", "CSS",
    "Flask", "Django", "MySQL",
    "Git", "VS Code", "OOP",
    "Data Structures", "File Handling"
]

st.write(", ".join(skills))

st.markdown("---")

# PROJECTS
st.header("Projects")

col1, col2 = st.columns(2)

with col1:
    st.subheader("File Organizer")
    st.write("""
- Python application to organize files automatically  
- Used **OS and Shutil modules**  
- Creates folders for Images, Videos, Documents
""")

with col2:
    st.subheader("Resume Generator")
    st.write("""
- Command-line tool using **Python OOP**  
- Collects user input  
- Generates formatted resume file
""")

st.markdown("---")

# CONTACT
st.header("Contact")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("📞 9884986356")

with col2:
    st.write("📧 pkmianmarbrightson@gmail.com")

with col3:
    st.write("📍 Chennai")

st.markdown("---")

st.markdown("<p style='text-align:center;'>© 2026 Mianmar Brightson P K</p>", unsafe_allow_html=True)
