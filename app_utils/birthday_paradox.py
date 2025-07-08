import streamlit as st
import numpy as np

def birthday_paradox_tab():
    st.header("🎂 Birthday Paradox Simulator")
    st.markdown("""
    ## The Birthday Paradox
    In a group of people, what are the chances that at least two share the same birthday?  
    Surprisingly, with just 23 people, there's over a 50% chance!
    """)
    group_size = st.slider("Number of people in the group:", 2, 100, 23, key="birthday_group")
    trials = st.slider("Number of simulation runs:", 100, 10000, 1000, key="birthday_trials")
    if st.button("Run Simulation!", key="birthday_btn"):
        matches = 0
        for _ in range(trials):
            birthdays = np.random.randint(1, 366, group_size)
            if len(set(birthdays)) < group_size:
                matches += 1
        probability = matches / trials
        st.success(f"In {matches} out of {trials} simulations, at least two people shared a birthday.")
        st.info(f"Estimated probability: {probability * 100:.2f}%")
    st.markdown("""
    ---
    ### Why is this a paradox?
    Our intuition underestimates how quickly the probability grows. With just 23 people, there's over a 50% chance of a shared birthday, due to the rapid growth in the number of possible pairs. This paradox demonstrates the counterintuitive nature of combinatorics and probability in everyday situations.
    
    **Key insight:** Probability grows with the number of pairs, not just the number of people. The paradox is a great illustration of how human intuition often fails with large numbers and combinations.
    
    **Further reading:** [Wikipedia: Birthday problem](https://en.wikipedia.org/wiki/Birthday_problem)
    
    **Source:** [ipveka/paradoxes](https://github.com/ipveka/paradoxes)
    """) 