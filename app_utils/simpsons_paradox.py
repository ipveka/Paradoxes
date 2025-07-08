import streamlit as st
import numpy as np
import pandas as pd

def simpsons_paradox_tab():
    st.header("📊 Simpson's Paradox")
    st.markdown("""
    ## Simpson's Paradox
    A trend appears in different groups of data but reverses when the groups are combined.  
    This paradox shows how misleading aggregated data can be.
    """)
    st.info("""
    **Paradox:** Aggregated data can hide or reverse trends present in subgroups, leading to misleading conclusions.
    """)
    st.subheader("Example: University Admissions")
    data = {
        'Department': ['A', 'A', 'B', 'B'],
        'Gender': ['Male', 'Female', 'Male', 'Female'],
        'Admitted': [80, 20, 30, 70],
        'Total': [100, 100, 100, 100]
    }
    df = pd.DataFrame(data)
    df['Rate'] = df['Admitted'] / df['Total']
    st.dataframe(df)
    total_male = df[df['Gender']=='Male']['Admitted'].sum()
    total_female = df[df['Gender']=='Female']['Admitted'].sum()
    total_male_total = df[df['Gender']=='Male']['Total'].sum()
    total_female_total = df[df['Gender']=='Female']['Total'].sum()
    overall_male_rate = total_male / total_male_total
    overall_female_rate = total_female / total_female_total
    st.info(f"Overall male admission rate: {overall_male_rate*100:.1f}%\nOverall female admission rate: {overall_female_rate*100:.1f}%")
    st.markdown("""
    ---
    ### Why is this a paradox?
    Simpson's Paradox warns us to always check for hidden variables before drawing conclusions from data. The aggregated data can tell a very different story from the subgroup data.
    
    **Key insight:** Always look for confounding variables and analyze data at multiple levels.
    
    **Further reading:** [Wikipedia: Simpson's paradox](https://en.wikipedia.org/wiki/Simpson%27s_paradox)
    
    **Source:** [ipveka/paradoxes](https://github.com/ipveka/paradoxes)
    """) 