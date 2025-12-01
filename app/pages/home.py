"""Home page UI for Probability Paradoxes app."""
import streamlit as st

def show():
    """Display the home page."""
    
    # Custom CSS for stunning buttons and animations
    st.markdown("""
    <style>
        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Main container styling */
        .main {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }
        
        /* Hero section */
        .hero-title {
            font-size: 56px;
            font-weight: 800;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-align: center;
            margin-bottom: 16px;
            animation: fadeInDown 0.8s ease;
        }
        
        .hero-subtitle {
            font-size: 22px;
            color: #4A5568;
            text-align: center;
            margin-bottom: 12px;
            animation: fadeInUp 0.8s ease;
        }
        
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        /* Stunning Button Styling */
        .stButton > button {
            width: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 20px 28px;
            font-size: 18px;
            font-weight: 700;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
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
            transform: translateY(-4px) scale(1.02);
            box-shadow: 0 12px 28px rgba(102, 126, 234, 0.5);
            background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        }
        
        .stButton > button:active {
            transform: translateY(-2px) scale(0.98);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
        }
    </style>
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown('<h1 class="hero-title">🧩 Probability Paradoxes</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle"><em>Where intuition meets mathematics</em></p>', unsafe_allow_html=True)

    # Navigation Buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🎁 Monty Hall", key="monty_btn", use_container_width=True):
            st.switch_page("pages/monty_hall.py")
        
        if st.button("😴 Sleeping Beauty", key="beauty_btn", use_container_width=True):
            st.switch_page("pages/sleeping_beauty.py")

    with col2:
        if st.button("🎂 Birthday Paradox", key="birthday_btn", use_container_width=True):
            st.switch_page("pages/birthday_paradox.py")
        
        if st.button("📊 Simpson's Paradox", key="simpson_btn", use_container_width=True):
            st.switch_page("pages/simpsons_paradox.py")

    with col3:
        if st.button("✉️ Two Envelopes", key="envelope_btn", use_container_width=True):
            st.switch_page("pages/two_envelopes.py")

    # Footer with description
    st.markdown('''
    <div style="margin-top: 60px;">
        <p style="text-align: center; color: #718096; font-size: 15px; line-height: 1.7; max-width: 700px; margin: 0 auto 24px;">
            Explore the most mind-bending puzzles in probability theory through interactive simulations. 
            Discover why our intuition often fails when dealing with uncertainty, and see the mathematics that reveals the truth.
        </p>
        <div style="text-align: center; padding: 32px 0; color: #718096; font-size: 14px;">Built with Streamlit • <a href="https://github.com/ipveka/paradoxes" style="color: #667eea;">ipveka/paradoxes</a></div>
    </div>
    ''', unsafe_allow_html=True)
