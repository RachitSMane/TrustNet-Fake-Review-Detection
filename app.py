import streamlit as st
import requests
from auth import register_user, authenticate

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="TrustNet Platform", layout="wide")

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# -----------------------------
# LOGIN PAGE
# -----------------------------

def login_page():

    st.title("🔐 TrustNet Login")

    tab1, tab2 = st.tabs(["Login", "Register"])

    # LOGIN
    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            if authenticate(username, password):
                st.session_state.logged_in = True
                st.session_state.user = username
                st.success("Login successful")
                st.rerun()

            else:
                st.error("Invalid username or password")

    # REGISTER
    with tab2:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Register"):

            if register_user(new_user, new_pass):
                st.success("Account created. Please login.")

            else:
                st.error("Username already exists")


# -----------------------------
# MAIN APP
# -----------------------------

def main_app():

    st.sidebar.write(f"Logged in as **{st.session_state.user}**")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    page = st.sidebar.selectbox(
        "Navigation",
        ["Review Analyzer", "Analytics Dashboard", "Pricing"]
    )

    # -----------------------------
    # REVIEW ANALYZER
    # -----------------------------
    if page == "Review Analyzer":

        st.title("🕵️ Fake Review Detection System")

        review = st.text_area("Enter Review")

        rating = st.slider("Rating", 1, 5, 5)

        if st.button("Analyze Review"):

            response = requests.post(
                f"{API_URL}/analyze",
                json={"review": review, "rating": rating}
            )

            result = response.json()

            score = result["score"]
            flag = result["flag"]
            probability = result["ml_fake_probability"]
            reasons = result["reasons"]

            st.divider()

            if flag == "GREEN":
                st.success("🟢 Genuine Review")

            elif flag == "YELLOW":
                st.warning("🟡 Suspicious Review")

            else:
                st.error("🔴 Fake Review")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Score", score)
                st.progress(score / 100)

            with col2:
                st.metric("ML Fake Probability", round(probability * 100))
                st.progress(probability)

            st.write("### Reasons")

            for r in reasons:
                st.write("•", r)

    # -----------------------------
    # ANALYTICS DASHBOARD
    # -----------------------------
    elif page == "Analytics Dashboard":

        st.title("📊 Fraud Analytics")

        st.metric("Reviews Analyzed", "15,200")
        st.metric("Fake Reviews Detected", "1,820")
        st.metric("Fraud Rate", "11.9%")

        st.bar_chart({
            "Genuine": 12000,
            "Suspicious": 1300,
            "Fake": 1820
        })

    # -----------------------------
    # PRICING PAGE
    # -----------------------------
    elif page == "Pricing":

        st.title("💼 TrustNet Pricing")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader("Go")
            st.markdown("### ₹399 / month")
            st.write("Small businesses")
            st.write("✔ 5k reviews/month")
            st.write("✔ Basic AI detection")

        with col2:
            st.subheader("Plus")
            st.markdown("### ₹1,999 / month")
            st.write("Growing e-commerce stores")
            st.write("✔ 50k reviews/month")
            st.write("✔ API access")
            st.write("✔ Analytics dashboard")

        with col3:
            st.subheader("Pro")
            st.markdown("### ₹19,900 / month")
            st.write("Large marketplaces")
            st.write("✔ Unlimited reviews")
            st.write("✔ Real-time monitoring")
            st.write("✔ Enterprise support")


# -----------------------------
# ROUTER
# -----------------------------

if not st.session_state.logged_in:
    login_page()

else:
    main_app()