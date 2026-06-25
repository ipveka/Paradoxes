import streamlit as st
import plotly.graph_objects as go

from components import inject_css, render_nav, render_footer

st.set_page_config(page_title="Simpson's Paradox", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")

inject_css()

render_nav("pages/simpsons_paradox.py")

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

render_footer()
