import streamlit as st
from app_utils.monty_hall import monty_hall_tab
from app_utils.birthday_paradox import birthday_paradox_tab
from app_utils.two_envelopes import two_envelopes_tab
from app_utils.sleeping_beauty import sleeping_beauty_tab
from app_utils.simpsons_paradox import simpsons_paradox_tab

st.set_page_config(page_title="🧠 Probability Paradoxes Playground", layout="wide")
st.title("🧩 Probability Paradoxes Playground")

st.markdown("""
Welcome! Explore and play with some of the most famous paradoxes in probability theory. Each tab below lets you interact with a different paradox, see simulations, and read explanations.
""")

tabs = st.tabs([
    "Monty Hall",
    "Birthday Paradox",
    "Two Envelopes Paradox",
    "Sleeping Beauty Problem",
    "Simpson's Paradox"
])

with tabs[0]:
    monty_hall_tab()
with tabs[1]:
    birthday_paradox_tab()
with tabs[2]:
    two_envelopes_tab()
with tabs[3]:
    sleeping_beauty_tab()
with tabs[4]:
    simpsons_paradox_tab() 