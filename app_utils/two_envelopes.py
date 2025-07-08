import streamlit as st
import random

def two_envelopes_tab():
    st.header("✉️ Two Envelopes Paradox")
    st.markdown("""
    ## The Two Envelopes Paradox
    You are given two envelopes, each containing money. One has twice as much as the other. You pick one at random.  
    Should you switch to the other envelope? The paradox: it seems you should always switch, but that can't be right!
    """)
    if st.button("Pick Envelopes!", key="envelopes_btn"):
        base = random.choice([10, 20, 50, 100, 200])
        envelopes = [base, base * 2]
        random.shuffle(envelopes)
        choice = random.choice([0, 1])
        st.write(f"You picked an envelope with ${envelopes[choice]}")
        st.write(f"The other envelope has ${envelopes[1 - choice]}")
        st.info("Paradox: By reasoning, it seems you should always switch, but this leads to a logical loop!")
    st.markdown("""
    ---
    ### Why is this a paradox?
    The expected value calculation seems to suggest you should always switch, but this leads to a logical loop. The reasoning ignores the prior distribution of amounts in the envelopes. This paradox exposes the subtleties of expectation and probability, and the importance of understanding the underlying assumptions in probabilistic reasoning.
    
    **Key insight:** The calculation is misleading because it doesn't account for how the amounts were chosen. The paradox is a reminder to carefully consider the setup of probability problems.
    
    **Further reading:** [Wikipedia: Two envelopes problem](https://en.wikipedia.org/wiki/Two_envelopes_problem)
    
    **Source:** [ipveka/paradoxes](https://github.com/ipveka/paradoxes)
    """) 