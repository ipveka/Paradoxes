import streamlit as st
import random
import plotly.graph_objects as go

st.set_page_config(page_title="Sleeping Beauty", page_icon="😴", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS with button styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Stunning Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 20px;
        font-size: 15px;
        font-weight: 600;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    .stButton > button:active {
        transform: translateY(0) scale(0.98);
    }
    
    .stButton > button:disabled {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        opacity: 0.6;
        cursor: not-allowed;
        transform: none;
        box-shadow: 0 2px 8px rgba(102, 126, 234, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# Navigation Bar
col_nav1, col_nav2, col_nav3, col_nav4, col_nav5, col_nav6 = st.columns(6)
with col_nav1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
with col_nav2:
    if st.button("🎁 Monty Hall", use_container_width=True):
        st.switch_page("pages/monty_hall.py")
with col_nav3:
    if st.button("🎂 Birthday", use_container_width=True):
        st.switch_page("pages/birthday_paradox.py")
with col_nav4:
    if st.button("✉️ Envelopes", use_container_width=True):
        st.switch_page("pages/two_envelopes.py")
with col_nav5:
    st.button("😴 Beauty", use_container_width=True, disabled=True)
with col_nav6:
    if st.button("📊 Simpson's", use_container_width=True):
        st.switch_page("pages/simpsons_paradox.py")

st.divider()

st.title("😴 Sleeping Beauty Problem")
st.markdown("### *A puzzle of self-locating belief*")

with st.container(border=True):
    st.subheader("🛌 The Experiment")
    st.markdown("""
    1. Sleeping Beauty is put to sleep on Sunday.
    2. A fair coin is tossed.
    3. **If Heads:** She is awakened once (Monday).
    4. **If Tails:** She is awakened twice (Monday & Tuesday), but her memory of Monday is erased.
    
    When she wakes up, she is asked:  
    **"What is the probability that the coin landed Heads?"**
    """)
    st.info("🤔 **The Conflict:** Is it 1/2 (fair coin) or 1/3 (more awakenings on Tails)?")

with st.container(border=True):
    st.subheader("💤 Run Simulation")
    trials = st.slider("Number of simulation runs:", 100, 10000, 1000, key="sb_trials_slider")
    
    if st.button("🚀 Run Simulation", key="sb_btn", type="primary", use_container_width=True):
        progress_bar = st.progress(0)
        
        heads_count = 0
        tails_count = 0
        total_awakenings = 0
        
        for i in range(trials):
            if i % 100 == 0:
                progress_bar.progress((i + 1) / trials)
            
            coin = random.choice(["heads", "tails"])
            if coin == "heads":
                total_awakenings += 1
                heads_count += 1
            else:
                total_awakenings += 2
                tails_count += 2
        
        progress_bar.progress(1.0)
        progress_bar.empty()
        
        prob_heads = heads_count / total_awakenings
        prob_tails = tails_count / total_awakenings
        
        col_res1, col_res2, col_res3 = st.columns(3)
        with col_res1:
            st.metric(label="P(Heads | Awake)", value=f"{prob_heads * 100:.2f}%", delta=f"{prob_heads - 0.3333:.2f}% vs 1/3")
        
        with col_res2:
            st.metric(label="P(Tails | Awake)", value=f"{prob_tails * 100:.2f}%")
        
        with col_res3:
            st.metric(label="Total Awakenings", value=f"{total_awakenings}")
        
        st.success(f"✨ Simulation Result: {prob_heads:.4f} (Close to 1/3)")
        st.markdown("**Interpretation:** If you bet on Heads every time you wake up, you will win 1/3 of the time.")
        
        # Visualization
        fig = go.Figure(data=[
            go.Bar(
                x=['Halfer (1/2)', 'Thirder (1/3)', 'Simulation'],
                y=[50, 33.33, prob_heads * 100],
                marker_color=['#FF6B6B', '#4ECDC4', '#667eea'],
                text=[f'50.0%', f'33.3%', f'{prob_heads * 100:.1f}%'],
                textposition='auto',
            )
        ])
        
        fig.update_layout(
            title='Probability Comparison: Halfer vs Thirder vs Simulation',
            yaxis_title='Probability of Heads (%)',
            yaxis=dict(range=[0, 60]),
            height=400,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)

with st.expander("📚 Why is this a paradox? (Click to expand)"):
    st.markdown("""
    ### The Explanation
    
    This problem divides philosophers and mathematicians into two camps:
    
    1.  **Halfers (1/2):** The coin is fair. No new information about the coin toss itself is gained just by waking up. Therefore, P(Heads) = 1/2.
    2.  **Thirders (1/3):** Imagine the experiment is repeated many times. There are twice as many "waking moments" when the coin is Tails. If you are in a waking moment, you are twice as likely to be in a Tails-world.
    
    **Simulation supports the Thirders:** If you make a bet every time you wake up, betting on Tails wins twice as often.
    
    **Further reading:** [Wikipedia: Sleeping Beauty problem](https://en.wikipedia.org/wiki/Sleeping_Beauty_problem)
    """)

# Footer
st.markdown('''
<div style="margin-top: 60px;">
    <p style="text-align: center; color: #718096; font-size: 15px; line-height: 1.7; max-width: 700px; margin: 0 auto 24px;">
        Explore the most mind-bending puzzles in probability theory through interactive simulations. 
        Discover why our intuition often fails when dealing with uncertainty, and see the mathematics that reveals the truth.
    </p>
    <div style="text-align: center; padding: 32px 0; color: #718096; font-size: 14px;">Built with Streamlit • <a href="https://github.com/ipveka/paradoxes" style="color: #667eea;">ipveka/paradoxes</a></div>
</div>
''', unsafe_allow_html=True)
