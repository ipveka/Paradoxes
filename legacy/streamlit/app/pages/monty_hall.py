import streamlit as st
import random
import plotly.graph_objects as go
import time

from components import inject_css, render_nav, render_footer

st.set_page_config(page_title="Monty Hall", page_icon="🎁", layout="wide", initial_sidebar_state="collapsed")

inject_css("""
    .result-animation {
        animation: slideIn 0.5s ease-out;
    }

    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .metric-card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
        animation: fadeIn 0.6s ease;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
""")

render_nav("pages/monty_hall.py")

st.title("🎁 Monty Hall Simulator")
st.markdown("### *The classic game show problem*")

with st.container(border=True):
    st.subheader("🚪 The Setup")
    st.markdown("""
    You're on a game show! Behind one of three doors is a brand new **Car** 🚗.  
    Behind the other two? **Goats** 🐐.
    
    1. You pick a door.
    2. The host (Monty), who knows what's behind the doors, opens another door to reveal a goat.
    3. **The Big Question:** Do you stick with your original choice or switch to the remaining door?
    """)
    st.info("🤔 **Intuition:** It feels like 50/50, so why switch?")

with st.container(border=True):
    st.subheader("🎮 Run Simulation")
    
    col_input1, col_input2 = st.columns(2)
    with col_input1:
        strategy = st.radio("Choose your strategy:", ["Stay with original door", "Switch after Monty opens a goat door"], key="monty_strategy")
    with col_input2:
        plays = st.slider("Number of simulated games:", 10, 10000, 1000, key="monty_plays")
    
    if st.button("🚀 Run Simulation", key="monty_hall_btn", type="primary", use_container_width=True):
        # Progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        wins_stay = 0
        wins_switch = 0
        
        # Run simulations for both strategies
        for i in range(plays):
            if i % 100 == 0:
                progress_bar.progress((i + 1) / plays)
                status_text.text(f"Simulating game {i + 1}/{plays}...")
            
            doors = [0, 0, 0]
            car_position = random.randint(0, 2)
            doors[car_position] = 1
            player_choice = random.randint(0, 2)
            available_doors = [i for i in range(3) if i != player_choice and doors[i] == 0]
            monty_opens = random.choice(available_doors)
            
            # Stay strategy
            if doors[player_choice] == 1:
                wins_stay += 1
            
            # Switch strategy
            remaining_doors = [i for i in range(3) if i != player_choice and i != monty_opens]
            switch_choice = remaining_doors[0]
            if doors[switch_choice] == 1:
                wins_switch += 1
        
        progress_bar.progress(1.0)
        status_text.text("Simulation complete!")
        time.sleep(0.5)
        status_text.empty()
        progress_bar.empty()
        
        # Determine which strategy was used
        if strategy == "Switch after Monty opens a goat door":
            wins = wins_switch
        else:
            wins = wins_stay
        
        win_rate = wins / plays * 100
        
        # Display results with animation
        st.markdown('<div class="result-animation">', unsafe_allow_html=True)
        
        st.metric(
            label="Your Win Rate", 
            value=f"{win_rate:.2f}%", 
            delta=f"{win_rate - 33.33:.2f}% vs Random" if strategy == "Switch after Monty opens a goat door" else f"{win_rate - 66.66:.2f}% vs Optimal"
        )
        
        if strategy == "Switch after Monty opens a goat door":
            st.success(f"🏁 You won {wins} times! Switching is statistically superior (~66%).")
        else:
            st.warning(f"🏁 You won {wins} times. Staying only wins ~33% of the time.")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Interactive Bar Chart Comparison
        st.subheader("📊 Strategy Comparison")
        
        stay_rate = (wins_stay / plays) * 100
        switch_rate = (wins_switch / plays) * 100
        
        fig = go.Figure(data=[
            go.Bar(
                name='Stay',
                x=['Stay Strategy'],
                y=[stay_rate],
                marker_color='#FF6B6B',
                text=[f'{stay_rate:.1f}%'],
                textposition='auto',
                hovertemplate='<b>Stay Strategy</b><br>Win Rate: %{y:.2f}%<extra></extra>'
            ),
            go.Bar(
                name='Switch',
                x=['Switch Strategy'],
                y=[switch_rate],
                marker_color='#4ECDC4',
                text=[f'{switch_rate:.1f}%'],
                textposition='auto',
                hovertemplate='<b>Switch Strategy</b><br>Win Rate: %{y:.2f}%<extra></extra>'
            )
        ])
        
        fig.update_layout(
            title='Win Rate Comparison: Stay vs Switch',
            yaxis_title='Win Rate (%)',
            yaxis=dict(range=[0, 100]),
            showlegend=False,
            height=500,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=14),
            hovermode='x unified'
        )
        
        fig.add_hline(y=50, line_dash="dash", line_color="gray", 
                     annotation_text="50% (Random)", annotation_position="right")
        
        st.plotly_chart(fig, use_container_width=True)

with st.expander("📚 Why is this a paradox? (Click to expand)"):
    st.markdown("""
    ### The Explanation
    
    Intuitively, when two doors remain, it seems like the car could be behind either with equal probability (50/50). However, this ignores the **prior probability** and the **host's constraints**.
    
    - **Original Choice:** When you picked a door, you had a **1/3** chance of being right and a **2/3** chance of being wrong (car is behind one of the other two doors).
    - **Monty's Action:** Monty *must* open a door with a goat. He cannot open your door, and he cannot reveal the car.
    - **Information Gain:** If you picked the car (1/3 chance), Monty can open either of the other two doors. If you picked a goat (2/3 chance), Monty has only *one* specific door he can open.
    
    **Conclusion:** By switching, you effectively bet that your *original* choice was wrong (which is true 2/3 of the time). Therefore, switching wins 2/3 of the time!
    
    **Further reading:** [Wikipedia: Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem)
    """)

render_footer()
