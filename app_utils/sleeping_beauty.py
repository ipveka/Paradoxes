import streamlit as st
import random

def sleeping_beauty_tab():
    st.header("😴 Sleeping Beauty Problem")
    st.markdown("""
    ## The Sleeping Beauty Problem
    Sleeping Beauty is put to sleep. A fair coin is tossed:
    - If heads, she is awakened once (Monday).
    - If tails, she is awakened twice (Monday and Tuesday), but with memory erased after Monday.
    When she wakes, what is the probability the coin was heads?
    """)
    trials = st.slider("Number of simulation runs:", 100, 10000, 1000, key="sb_trials_slider")
    if st.button("Run Simulation!", key="sb_btn"):
        heads_count = 0
        total_awakenings = 0
        for _ in range(trials):
            coin = random.choice(["heads", "tails"])
            if coin == "heads":
                total_awakenings += 1
                heads_count += 1
            else:
                total_awakenings += 2
        prob_heads = heads_count / total_awakenings
        st.success(f"Probability it was heads upon waking: {prob_heads * 100:.2f}%")
        st.info("The answer is debated: 'thirder' position says 1/3, 'halfer' says 1/2. Simulation supports 1/3.")
    st.markdown("""
    ---
    ### Why is this a paradox?
    The answer seems to depend on how you count possibilities: is it 1/2 or 1/3? Philosophers and mathematicians still debate the correct answer. This paradox explores the difference between subjective and objective probability, and how to update beliefs when you have limited information about your own situation.
    
    **Key insight:** The problem highlights the difference between subjective and objective probability, and how to update beliefs with self-locating uncertainty. It is a central example in the philosophy of probability.
    
    **Further reading:** [Wikipedia: Sleeping Beauty problem](https://en.wikipedia.org/wiki/Sleeping_Beauty_problem)
    
    **Source:** [ipveka/paradoxes](https://github.com/ipveka/paradoxes)
    """) 