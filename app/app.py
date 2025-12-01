import streamlit as st

st.set_page_config(
    page_title="Probability Paradoxes",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Import and run home page
from pages import home
home.show()
