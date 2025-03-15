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
st.set_page_config(page_title="Password Generator", page_icon="🔒", layout="centered")
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .stApp {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.2);
        }
        h1 {
            color: #ff5733;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🔐 Password Generator</h1>", unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.header("Customize Your Password")
password_length = st.sidebar.slider("Password Length", min_value=6, max_value=32, value=12)
use_digits = st.sidebar.checkbox("Include Numbers", value=True)
use_specials = st.sidebar.checkbox("Include Special Characters", value=True)

if st.button("Generate Password", key="generate"):
    password = generate_password(password_length, use_digits, use_specials)
    st.success(f"Your Generated Password: `{password}`")
    st.write("🔑 **Make sure to store it safely!**")

st.markdown("---")
st.info("Use the sidebar to customize your password settings.")
