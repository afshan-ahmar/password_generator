import streamlit as st
import random
import string

def generate_password(length, use_digits, use_specials):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.set_page_config(page_title="🔒 Password Generator", page_icon="🔑", layout="centered")
st.markdown("""
    <style>
        body {
            background-color: #1e1e2e;
        }
        .stApp {
            background-color: #cbf0f0;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0px 0px 20px rgba(255, 87, 51, 0.5);
        }
        h1 {
            color: #ff5733;
            text-align: center;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #ff5733;
            color: white;
            border-radius: 10px;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color: #ff4500;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🔐 Secure Password Generator</h1>", unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.header("🔧 Customize Your Password")
password_length = st.sidebar.slider("Password Length", min_value=6, max_value=32, value=12)
use_digits = st.sidebar.checkbox("🔢 Include Numbers", value=True)
use_specials = st.sidebar.checkbox("🔣 Include Special Characters", value=True)

if st.button("🔄 Generate Password", key="generate"):
    password = generate_password(password_length, use_digits, use_specials)
    st.success(f"### ✅ Your Secure Password: `{password}`")
    st.write("🔑 **Ensure to store it safely!**")

st.markdown("---")
st.info("Use the sidebar to customize your password settings and enhance security.")
