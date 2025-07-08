import streamlit as st
import random

def monty_hall_tab():
    st.header("🎁 Monty Hall Simulator")
    st.markdown("""
    ## The Monty Hall Problem
    You're on a game show! Behind one of three doors is a brand new 🚗...  
    Behind the other two? 🐐 goats.  
    
    You choose a door. The host (Monty) opens another door to show you a goat.  
    **Do you want to switch?**
    """)
    strategy = st.radio("Your move:", ["Stay with original door", "Switch after Monty opens a goat door"], key="monty_strategy")
    plays = st.slider("🎲 Number of simulated games:", 10, 10000, 100, key="monty_plays")
    if st.button("Run Simulation!", key="monty_hall_btn"):
        wins = 0
        for _ in range(plays):
            doors = [0, 0, 0]
            car_position = random.randint(0, 2)
            doors[car_position] = 1
            player_choice = random.randint(0, 2)
            available_doors = [i for i in range(3) if i != player_choice and doors[i] == 0]
            monty_opens = random.choice(available_doors)
            if strategy == "Switch after Monty opens a goat door":
                remaining_doors = [i for i in range(3) if i != player_choice and i != monty_opens]
                player_choice = remaining_doors[0]
            if doors[player_choice] == 1:
                wins += 1
        st.success(f"🏁 You won the car {wins} out of {plays} times!")
        st.info(f"🎯 Win rate: {wins / plays * 100:.2f}%")
        if strategy == "Switch after Monty opens a goat door":
            st.markdown("🤯 See? Switching gives you a ~66% win rate!")
        else:
            st.markdown("🐐 Staying gives you about a ~33% win rate. Not great.")
    st.markdown("""
    ---
    ### Why is this a paradox?
    Intuitively, it seems like switching or staying should be 50/50, but switching actually gives you a 2/3 chance of winning. The host's knowledge and action change the probabilities in a non-obvious way. This paradox highlights how our intuition can be misled by conditional probability and the importance of considering all available information.
    
    **Key insight:** Monty's action gives you information, making switching the better strategy. The problem is a classic example of how probability can defy our expectations.
    
    **Further reading:** [Wikipedia: Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem)
    
    **Source:** [ipveka/paradoxes](https://github.com/ipveka/paradoxes)
    """) 