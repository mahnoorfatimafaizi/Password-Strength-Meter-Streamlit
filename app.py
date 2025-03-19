import streamlit as st
import re
import random

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
        color: #333333;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
        color: #333333;
        border-radius: 5px;
        border: 1px solid #cccccc;
    }
    .stSuccess {
        background-color: #d4edda;
        color: #155724;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #c3e6cb;
    }
    .stWarning {
        background-color: #fff3cd;
        color: #856404;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ffeeba;
    }
    .stInfo {
        background-color: #d1ecf1;
        color: #0c5460;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #bee5eb;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (!@#$%^&*).")

    if score == 4:
        return "✅ Strong password!", feedback, score
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", feedback, score
    else:
        return "❌ Weak Password - Improve it using the suggestions above.", feedback, score

def generate_strong_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    return "".join(random.sample(characters, 12))

st.title("🔐 Password Strength Checker")
password = st.text_input("Enter your password:", type="password", placeholder="Type your password here...")


col1, col2 = st.columns(2)
with col1:
    check_button = st.button("Check Strength")
with col2:
    generate_button = st.button("Generate Password")

if check_button and password:
    strength, feedback, score = check_password_strength(password)
    st.subheader(strength)
    st.progress(score / 4)  
    if feedback:
        st.warning("\n".join(feedback))
    if "Weak" in strength:
        st.info(f"💡 Suggested Strong Password: `{generate_strong_password()}`")

if generate_button:
    generated_password = generate_strong_password()
    st.success(f"🔑 Generated Strong Password: `{generated_password}`")