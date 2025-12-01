import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Simpson's Paradox", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")

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
    if st.button("😴 Beauty", use_container_width=True):
        st.switch_page("pages/sleeping_beauty.py")
with col_nav6:
    st.button("📊 Simpson's", use_container_width=True, disabled=True)

st.divider()

st.title("📊 Simpson's Paradox")
st.markdown("### *When the whole contradicts the parts*")

with st.container(border=True):
    st.subheader("📉 The Phenomenon")
    st.markdown("""
    A trend appears in different groups of data but **disappears or reverses** when these groups are combined.
    
    This paradox highlights the danger of relying solely on aggregated data without considering underlying variables.
    """)
    st.warning("⚠️ **Warning:** Aggregated statistics can be misleading!")

with st.container(border=True):
    st.subheader("🏫 Example: University Admissions")
    st.markdown("Two departments (A and B) are accepting students. Let's look at the acceptance rates by gender.")
    
    # Data
    dept_a_male_apply = 100
    dept_a_male_accept = 80  # 80%
    dept_a_female_apply = 20
    dept_a_female_accept = 18  # 90%
    
    dept_b_male_apply = 20
    dept_b_male_accept = 10  # 50%
    dept_b_female_apply = 100
    dept_b_female_accept = 60  # 60%
    
    # Calculate rates
    dept_a_male_rate = (dept_a_male_accept / dept_a_male_apply) * 100
    dept_a_female_rate = (dept_a_female_accept / dept_a_female_apply) * 100
    dept_b_male_rate = (dept_b_male_accept / dept_b_male_apply) * 100
    dept_b_female_rate = (dept_b_female_accept / dept_b_female_apply) * 100
    
    # Department-level visualization
    fig_dept = go.Figure()
    
    fig_dept.add_trace(go.Bar(
        name='Male',
        x=['Department A', 'Department B'],
        y=[dept_a_male_rate, dept_b_male_rate],
        marker_color='#667eea',
        text=[f'{dept_a_male_rate:.0f}%', f'{dept_b_male_rate:.0f}%'],
        textposition='auto',
        hovertemplate='<b>Male</b><br>Acceptance Rate: %{y:.1f}%<extra></extra>'
    ))
    
    fig_dept.add_trace(go.Bar(
        name='Female',
        x=['Department A', 'Department B'],
        y=[dept_a_female_rate, dept_b_female_rate],
        marker_color='#f093fb',
        text=[f'{dept_a_female_rate:.0f}%', f'{dept_b_female_rate:.0f}%'],
        textposition='auto',
        hovertemplate='<b>Female</b><br>Acceptance Rate: %{y:.1f}%<extra></extra>'
    ))
    
    fig_dept.update_layout(
        title='Acceptance Rates by Department',
        yaxis_title='Acceptance Rate (%)',
        yaxis=dict(range=[0, 100]),
        barmode='group',
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=14),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig_dept, use_container_width=True)
    
    st.info("👩 **In both departments, women have a HIGHER acceptance rate than men!**")
    
    st.divider()
    
    # Aggregation
    total_male_apply = dept_a_male_apply + dept_b_male_apply
    total_male_accept = dept_a_male_accept + dept_b_male_accept
    total_female_apply = dept_a_female_apply + dept_b_female_apply
    total_female_accept = dept_a_female_accept + dept_b_female_accept
    
    male_rate = (total_male_accept / total_male_apply) * 100
    female_rate = (total_female_accept / total_female_apply) * 100
    
    st.subheader("📊 Aggregated Results (The Paradox)")
    
    # Overall visualization
    fig_overall = go.Figure()
    
    fig_overall.add_trace(go.Bar(
        x=['Overall'],
        y=[male_rate],
        name='Male',
        marker_color='#667eea',
        text=[f'{male_rate:.1f}%'],
        textposition='auto',
        hovertemplate='<b>Male Overall</b><br>Acceptance Rate: %{y:.1f}%<br>Accepted: ' + f'{total_male_accept}/{total_male_apply}<extra></extra>'
    ))
    
    fig_overall.add_trace(go.Bar(
        x=['Overall'],
        y=[female_rate],
        name='Female',
        marker_color='#f093fb',
        text=[f'{female_rate:.1f}%'],
        textposition='auto',
        hovertemplate='<b>Female Overall</b><br>Acceptance Rate: %{y:.1f}%<br>Accepted: ' + f'{total_female_accept}/{total_female_apply}<extra></extra>'
    ))
    
    fig_overall.update_layout(
        title='Overall Acceptance Rates',
        yaxis_title='Acceptance Rate (%)',
        yaxis=dict(range=[0, 100]),
        barmode='group',
        height=350,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=14),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig_overall, use_container_width=True)
    
    if male_rate > female_rate:
        st.error(f"🤯 **PARADOX REVEALED:** Even though women had a higher rate in BOTH departments, men have a higher rate overall ({male_rate:.1f}% vs {female_rate:.1f}%)!")
    else:
        st.info("No paradox with these numbers.")
    
    st.markdown("""
    ### 🔍 Why did this happen?
    
    - **Men** applied overwhelmingly to Department A (100 vs 20) which has a **high acceptance rate** (80%).
    - **Women** applied overwhelmingly to Department B (100 vs 20) which has a **low acceptance rate** (60%).
    
    The **weighted average** pulls the female rate down because most of their applications were in the difficult department, 
    even though they outperformed men in both departments individually!
    """)

with st.expander("📚 Why is this a paradox? (Click to expand)"):
    st.markdown("""
    ### The Explanation
    
    Simpson's Paradox occurs when a trend present in different groups is reversed when the groups are combined.
    
    It usually happens because of a **confounding variable** (in this case, the difficulty of the department) that is unevenly distributed across the groups.
    
    **Key Lesson:** Always check for hidden variables! Aggregated data can lie.
    
    **Real-World Example:** This actually happened at UC Berkeley in 1973, where overall admission rates appeared to favor men, 
    but when broken down by department, most departments actually favored women. The difference was that women applied to 
    more competitive departments.
    
    **Further reading:** [Wikipedia: Simpson's paradox](https://en.wikipedia.org/wiki/Simpson%27s_paradox)
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
