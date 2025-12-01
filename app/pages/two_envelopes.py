import streamlit as st
import random
import plotly.graph_objects as go

st.set_page_config(page_title="Two Envelopes", page_icon="✉️", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS with button styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    .envelope-animation {
        animation: bounce 0.6s ease;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
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
    st.button("✉️ Envelopes", use_container_width=True, disabled=True)
with col_nav5:
    if st.button("😴 Beauty", use_container_width=True):
        st.switch_page("pages/sleeping_beauty.py")
with col_nav6:
    if st.button("📊 Simpson's", use_container_width=True):
        st.switch_page("pages/simpsons_paradox.py")

st.divider()

st.title("✉️ Two Envelopes Paradox")
st.markdown("### *The switching dilemma*")

with st.container(border=True):
    st.subheader("💌 The Setup")
    st.markdown("""
    You are given two envelopes. 
    - One contains **$X**.
    - The other contains **$2X**.
    
    You pick one envelope at random and see it contains **$100**.
    
    **Should you switch to the other envelope?**
    """)
    st.info("""
    **The Reasoning Trap:**
    - 50% chance the other envelope has $50.
    - 50% chance the other envelope has $200.
    - Expected value = (0.5 × 50) + (0.5 × 200) = $125.
    - Since $125 > $100, you should switch... right?
    """)

with st.container(border=True):
    st.subheader("🎲 Play the Game")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🧧 Pick Envelope A", key="envelope_a", type="primary", use_container_width=True):
            st.session_state.envelope_picked = 'A'
            st.session_state.show_result = True
    
    with col2:
        if st.button("🧧 Pick Envelope B", key="envelope_b", type="primary", use_container_width=True):
            st.session_state.envelope_picked = 'B'
            st.session_state.show_result = True
    
    if 'show_result' in st.session_state and st.session_state.show_result:
        base = random.choice([10, 20, 50, 100, 200])
        envelopes = {'A': base, 'B': base * 2}
        
        # Randomly swap
        if random.random() > 0.5:
            envelopes = {'A': base * 2, 'B': base}
        
        picked = st.session_state.envelope_picked
        other = 'B' if picked == 'A' else 'A'
        
        amount_picked = envelopes[picked]
        other_amount = envelopes[other]
        
        st.markdown('<div class="envelope-animation">', unsafe_allow_html=True)
        st.success(f"✨ You picked Envelope {picked} with **${amount_picked}**")
        st.markdown('</div>', unsafe_allow_html=True)
        
        col_reveal1, col_reveal2 = st.columns(2)
        
        with col_reveal1:
            if st.button("🔍 Reveal Other Envelope", key="reveal", use_container_width=True):
                st.session_state.revealed = True
        
        with col_reveal2:
            if st.button("🔄 Play Again", key="reset", use_container_width=True):
                st.session_state.show_result = False
                st.session_state.revealed = False
                st.rerun()
        
        if 'revealed' in st.session_state and st.session_state.revealed:
            st.markdown(f"### Envelope {other} contains: **${other_amount}**")
            
            if other_amount > amount_picked:
                st.warning(f"📈 You would have gained ${other_amount - amount_picked} by switching!")
            else:
                st.success(f"📉 You would have lost ${amount_picked - other_amount} by switching!")
            
            # Visualization
            fig = go.Figure(data=[
                go.Bar(
                    x=[f'Your Pick (Env {picked})', f'Other (Env {other})'],
                    y=[amount_picked, other_amount],
                    marker_color=['#667eea', '#f093fb'],
                    text=[f'${amount_picked}', f'${other_amount}'],
                    textposition='auto',
                )
            ])
            
            fig.update_layout(
                title='Envelope Comparison',
                yaxis_title='Amount ($)',
                height=350,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                showlegend=False
            )
            
            st.plotly_chart(fig, use_container_width=True)

with st.expander("📚 Why is this a paradox? (Click to expand)"):
    st.markdown("""
    ### The Explanation
    
    The paradox arises from a misuse of the **Expected Value** calculation. 
    
    The reasoning "50% chance of 0.5X and 50% chance of 2X" assumes that *any* amount X is equally likely, which implies an infinite uniform distribution of money (impossible!).
    
    In reality, there is a specific probability distribution for the amount of money in the envelopes. Once you pick a specific value (like $100), you gain information about that distribution.
    
    **Key Insight:** You cannot assume a flat prior distribution over all possible values of money.
    
    **Further reading:** [Wikipedia: Two envelopes problem](https://en.wikipedia.org/wiki/Two_envelopes_problem)
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
