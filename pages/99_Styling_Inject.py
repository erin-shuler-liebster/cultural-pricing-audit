import streamlit as st

def local_css():
    st.markdown("""
        <style>
        .stApp {
            background-color: #f8f9fa;
            font-family: 'Helvetica Neue', sans-serif;
        }
        h1, h2 {
            color: #1c3f60;
        }
        .css-1d391kg { padding-top: 1rem; }
        </style>
    """, unsafe_allow_html=True)

local_css()
