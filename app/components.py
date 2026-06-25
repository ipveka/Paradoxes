"""Shared UI helpers for the Probability Paradoxes app.

Centralizes the CSS, top navigation bar, and footer that every paradox page
relies on, so they live in one place instead of being copy-pasted per page.
"""
import streamlit as st

# Ordered list of (button label, target page path) for the top navigation bar.
# "app.py" is the home entry point; the rest live under pages/.
PAGES = [
    ("🏠 Home", "app.py"),
    ("🎁 Monty Hall", "pages/monty_hall.py"),
    ("🎂 Birthday", "pages/birthday_paradox.py"),
    ("✉️ Envelopes", "pages/two_envelopes.py"),
    ("😴 Beauty", "pages/sleeping_beauty.py"),
    ("📊 Simpson's", "pages/simpsons_paradox.py"),
]

# Base styling shared by every page: gradient background plus the animated
# button treatment. Pages can pass page-specific rules via inject_css(extra=...).
BASE_CSS = """
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
"""

FOOTER_HTML = """
<div style="margin-top: 60px;">
    <p style="text-align: center; color: #718096; font-size: 15px; line-height: 1.7; max-width: 700px; margin: 0 auto 24px;">
        Explore the most mind-bending puzzles in probability theory through interactive simulations.
        Discover why our intuition often fails when dealing with uncertainty, and see the mathematics that reveals the truth.
    </p>
    <div style="text-align: center; padding: 32px 0; color: #718096; font-size: 14px;">Built with Streamlit • <a href="https://github.com/ipveka/paradoxes" style="color: #667eea;">ipveka/paradoxes</a></div>
</div>
"""


def inject_css(extra: str = "") -> None:
    """Inject the shared base CSS, plus any page-specific rules in ``extra``."""
    st.markdown(f"<style>{BASE_CSS}{extra}</style>", unsafe_allow_html=True)


def render_nav(current: str) -> None:
    """Render the top navigation bar.

    ``current`` is the page path of the page being rendered (e.g.
    ``"pages/monty_hall.py"``); its button is shown disabled.
    """
    cols = st.columns(len(PAGES))
    for col, (label, target) in zip(cols, PAGES):
        with col:
            if target == current:
                st.button(label, use_container_width=True, disabled=True, key=f"nav_{target}")
            elif st.button(label, use_container_width=True, key=f"nav_{target}"):
                st.switch_page(target)
    st.divider()


def render_footer() -> None:
    """Render the shared page footer."""
    st.markdown(FOOTER_HTML, unsafe_allow_html=True)
