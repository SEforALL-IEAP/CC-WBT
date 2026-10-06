import streamlit as st

def show():
    st.image("public/financce_logo.png", width=360)
    st.title("Welcome to the Financial Clean Cooking Platform")

    st.image("public/home_image.png", width=500)
    
    if st.button("Select scenario"):
        st.session_state.page = "country_selector"
        st.rerun()