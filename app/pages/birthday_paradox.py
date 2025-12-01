import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Birthday Paradox", page_icon="🎂", layout="wide", initial_sidebar_state="collapsed")

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
    st.button("🎂 Birthday", use_container_width=True, disabled=True)
with col_nav4:
    if st.button("✉️ Envelopes", use_container_width=True):
        st.switch_page("pages/two_envelopes.py")
with col_nav5:
    if st.button("😴 Beauty", use_container_width=True):
        st.switch_page("pages/sleeping_beauty.py")
with col_nav6:
    if st.button("📊 Simpson's", use_container_width=True):
        st.switch_page("pages/simpsons_paradox.py")

st.divider()

st.title("🎂 Birthday Paradox Simulator")
st.markdown("### *The mathematics of coincidence*")

with st.container(border=True):
    st.subheader("🎈 The Question")
    st.markdown("""
    In a group of **N** people, what is the probability that at least two of them share the same birthday?
    
    Most people guess that you need a huge group (like 180+) to have a 50% chance.
    
    **Let's test your intuition!**
    """)
    st.info("💡 **Fun Fact:** You only need **23** people to reach a >50% probability!")

# Probability Curve Visualization
with st.container(border=True):
    st.subheader("📈 Probability Curve")
    
    # Calculate theoretical probabilities
    group_sizes = list(range(1, 101))
    probabilities = []
    
    for n in group_sizes:
        if n == 1:
            prob = 0
        else:
            # Calculate probability of at least one match
            prob_no_match = 1
            for i in range(n):
                prob_no_match *= (365 - i) / 365
            prob = 1 - prob_no_match
        probabilities.append(prob * 100)
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=group_sizes,
        y=probabilities,
        mode='lines',
        name='Probability',
        line=dict(color='#667eea', width=3),
        fill='tozeroy',
        fillcolor='rgba(102, 126, 234, 0.2)',
        hovertemplate='<b>Group Size: %{x}</b><br>Probability: %{y:.2f}%<extra></extra>'
    ))
    
    # Add 50% line
    fig.add_hline(y=50, line_dash="dash", line_color="red", 
                 annotation_text="50% threshold", annotation_position="right")
    
    # Add 23 people marker
    fig.add_vline(x=23, line_dash="dot", line_color="green",
                 annotation_text="23 people (50.7%)", annotation_position="top")
    
    fig.update_layout(
        title='Probability of Shared Birthday by Group Size',
        xaxis_title='Number of People',
        yaxis_title='Probability (%)',
        yaxis=dict(range=[0, 100]),
        height=450,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=14),
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)

with st.container(border=True):
    st.subheader("🧪 Run Experiment")
    
    col_input1, col_input2 = st.columns(2)
    with col_input1:
        group_size = st.slider("Number of people in the group:", 2, 100, 23, key="birthday_group")
    with col_input2:
        trials = st.slider("Number of simulation runs:", 100, 10000, 1000, key="birthday_trials")
    
    if st.button("🚀 Run Simulation", key="birthday_btn", type="primary", use_container_width=True):
        progress_bar = st.progress(0)
        
        matches = 0
        for i in range(trials):
            if i % 100 == 0:
                progress_bar.progress((i + 1) / trials)
            
            birthdays = np.random.randint(1, 366, group_size)
            if len(set(birthdays)) < group_size:
                matches += 1
        
        progress_bar.progress(1.0)
        progress_bar.empty()
        
        probability = matches / trials
        
        # Calculate theoretical probability
        if group_size == 1:
            theoretical_prob = 0
        else:
            prob_no_match = 1
            for i in range(group_size):
                prob_no_match *= (365 - i) / 365
            theoretical_prob = 1 - prob_no_match
        
        col_res1, col_res2, col_res3 = st.columns(3)
        with col_res1:
            st.metric(label="Simulated Probability", value=f"{probability * 100:.2f}%")
        
        with col_res2:
            st.metric(label="Theoretical Probability", value=f"{theoretical_prob * 100:.2f}%")
        
        with col_res3:
            difference = abs(probability - theoretical_prob) * 100
            st.metric(label="Difference", value=f"{difference:.2f}%", delta=f"±{difference:.2f}%")
        
        if probability > 0.5:
            st.success(f"✨ In {matches} out of {trials} groups, at least two people shared a birthday!")
        else:
            st.info(f"In {matches} out of {trials} groups, at least two people shared a birthday.")

with st.expander("📚 Why is this a paradox? (Click to expand)"):
    st.markdown("""
    ### The Explanation
    
    It's not really a paradox in the logical sense, but a **veridical paradox**—a result that feels wrong but is proven to be true.
    
    The key is that we aren't looking for a match with *you* specifically. We are looking for a match between *any pair* of people in the group.
    
    - With **23 people**, there are **253 possible pairs** (`23 * 22 / 2`).
    - The probability that *no one* shares a birthday decreases very rapidly as you add more people (and thus more pairs).
    
    **Formula:**
    $$ P(match) = 1 - P(no\_match) $$
    $$ P(no\_match) = \\frac{365}{365} \\times \\frac{364}{365} \\times \\dots \\times \\frac{365-n+1}{365} $$
    
    **Further reading:** [Wikipedia: Birthday problem](https://en.wikipedia.org/wiki/Birthday_problem)
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
