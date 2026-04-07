import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("🔐 Auth System (JWT + OAuth2)")

menu = st.sidebar.selectbox("Menu", ["Signup", "Login"])

if menu == "Signup":
    st.subheader("Create Account")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Signup"):
        res = requests.post(f"{BASE_URL}/signup", json={
            "email": email,
            "password": password
        })
        try:
          data = res.json()
          st.json(data)
        except:
          st.error("Invalid response from server")
          st.text(res.text)

if menu == "Login":
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        res = requests.post(f"{BASE_URL}/login", json={
            "email": email,
            "password": password
        })
        data = res.json()

        st.json(data)

        if "refresh_token" in data:
            if st.button("Refresh Token"):
                refresh_res = requests.post(
                    f"{BASE_URL}/refresh",
                    params={"refresh_token": data["refresh_token"]}
                )
                st.write(refresh_res.json())