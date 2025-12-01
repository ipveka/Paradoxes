# Application Structure

This document explains the architecture and organization of the Probability Paradoxes app.

## Directory Structure

```
Paradoxes/
├── app/
│   ├── app.py                 # Entry point (redirects to home)
│   └── pages/
│       ├── home.py            # Main landing page
│       ├── monty_hall.py      # Monty Hall simulator
│       ├── birthday_paradox.py # Birthday Paradox simulator
│       ├── two_envelopes.py   # Two Envelopes simulator
│       ├── sleeping_beauty.py # Sleeping Beauty simulator
│       └── simpsons_paradox.py # Simpson's Paradox simulator
├── .streamlit/
│   └── config.toml            # Streamlit configuration (theme, etc.)
├── docs/
│   ├── concepts.md            # Mathematical concepts explained
│   ├── structure.md           # This file
│   └── deploy.md              # Deployment guide
├── run_app.py                 # Launcher script
├── requirements.txt           # Python dependencies
├── README.md                  # Project overview
└── LICENSE                    # MIT License
```

## Architecture Overview

### Entry Point Flow

1. **`run_app.py`** - Launcher script
   - Installs dependencies from `requirements.txt`
   - Launches Streamlit app pointing to `app/app.py`

2. **`app/app.py`** - Main entry
   - Redirects to `pages/home.py` using `st.switch_page()`

3. **`pages/home.py`** - Home page
   - Displays hero section
   - Navigation buttons to paradox pages

4. **Paradox Pages** - Individual simulators
   - Each page is self-contained
   - Top navigation bar for easy switching

### Technology Stack

**Core Framework:**
- **Streamlit** - Web app framework
- **Python 3.11+** - Programming language

**Visualization:**
- **Plotly** - Interactive charts
- **Matplotlib** - Static plots (if needed)

**Data Processing:**
- **NumPy** - Numerical computations
- **Pandas** - Data manipulation (Simpson's Paradox)

**Styling:**
- **Custom CSS** - Gradient backgrounds, button effects
- **Streamlit Theming** - Light theme with custom colors

## Page Architecture

### Common Structure

Each paradox page follows this pattern:

```python
import streamlit as st
import [required libraries]

# 1. Page Configuration
st.set_page_config(
    page_title="...",
    page_icon="...",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS Styling
st.markdown("""<style>...</style>""", unsafe_allow_html=True)

# 3. Navigation Bar
# 6 buttons: Home + 5 paradoxes

# 4. Page Title & Subtitle
st.title("...")
st.markdown("### ...")

# 5. Content Sections (in containers)
with st.container(border=True):
    # The Setup
    # The Simulation
    # The Results

# 6. Explanation (expandable)
with st.expander("Why is this a paradox?"):
    # Mathematical explanation
```

### Navigation System

**Top Navigation Bar:**
- Present on every page (including home)
- 6 buttons in a row
- Current page button is disabled
- Uses `st.switch_page()` for navigation

**Navigation Flow:**
```
Home ←→ Monty Hall
  ↓        ↓
  ↓    Birthday Paradox
  ↓        ↓
  ↓    Two Envelopes
  ↓        ↓
  ↓    Sleeping Beauty
  ↓        ↓
  └→ Simpson's Paradox
```

## Design System

### Color Palette

**Primary Gradient:**
- Start: `#667eea` (Purple)
- End: `#764ba2` (Deep Purple)

**Background:**
- Main: `linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)`
- Containers: `#FFFFFF` (White)

**Text:**
- Primary: `#2D3748` (Dark Gray)
- Secondary: `#4A5568` (Medium Gray)
- Tertiary: `#718096` (Light Gray)

**Accent Colors:**
- Success: `#4ECDC4` (Teal)
- Warning: `#FF6B6B` (Red)
- Info: `#6C63FF` (Indigo)

### Typography

**Headings:**
- Hero Title: 56px, weight 800
- Page Title: Default Streamlit h1
- Section Headers: Default Streamlit h3

**Body Text:**
- Description: 17px, line-height 1.7
- Card Text: 15px, line-height 1.6
- Button Text: 15-18px, weight 600-700

### Button Styling

**Effects:**
- Gradient background with reversal on hover
- Shine sweep animation (pseudo-element)
- Lift & scale transformation
- Enhanced drop shadow
- Smooth cubic-bezier transitions

**States:**
- Default: Gradient with shadow
- Hover: Reversed gradient, lifted, enhanced shadow
- Active: Pressed down, reduced shadow
- Disabled: Gray gradient, no effects

## Component Patterns

### Simulation Pattern

Most paradoxes follow this simulation pattern:

```python
# Input Controls
strategy = st.radio(...)
trials = st.slider(...)

# Run Button
if st.button("🚀 Run Simulation", type="primary"):
    # Progress Bar
    progress_bar = st.progress(0)
    
    # Simulation Loop
    for i in range(trials):
        # Update progress
        if i % 100 == 0:
            progress_bar.progress((i + 1) / trials)
        
        # Run simulation logic
        ...
    
    # Clear progress
    progress_bar.empty()
    
    # Display Results
    st.metric(...)
    
    # Visualization
    st.plotly_chart(fig)
```

### Visualization Pattern

Using Plotly for interactive charts:

```python
import plotly.graph_objects as go

fig = go.Figure(data=[...])

fig.update_layout(
    title='...',
    xaxis_title='...',
    yaxis_title='...',
    height=400,
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent
)

st.plotly_chart(fig, use_container_width=True)
```

## State Management

### Session State Usage

**Two Envelopes Page:**
```python
st.session_state.envelope_picked = 'A'
st.session_state.show_result = True
st.session_state.revealed = False
```

**Why:**
- Maintains state between button clicks
- Enables reveal mechanism
- Allows "Play Again" functionality

### Page Navigation

**Using `st.switch_page()`:**
```python
if st.button("🏠 Home"):
    st.switch_page("pages/home.py")
```

**Path Convention:**
- From any page to home: `"pages/home.py"`
- From any page to paradox: `"pages/[name].py"`

## Configuration

### Streamlit Config (`.streamlit/config.toml`)

```toml
[client]
showSidebarNavigation = false

[theme]
base="light"
primaryColor="#6C63FF"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#31333F"
font="sans serif"
```

**Key Settings:**
- Sidebar navigation disabled (using custom nav)
- Light theme base
- Custom purple primary color
- Clean, modern font

## Performance Considerations

### Optimization Strategies

1. **Progress Updates:**
   - Update every 100 iterations, not every iteration
   - Reduces UI overhead during simulations

2. **Chart Rendering:**
   - Use `use_container_width=True` for responsive charts
   - Transparent backgrounds for better integration

3. **State Management:**
   - Minimal use of session state
   - Clear state when appropriate

4. **CSS:**
   - Single CSS block per page
   - Efficient selectors
   - Hardware-accelerated animations (transform, opacity)

## Extensibility

### Adding a New Paradox

1. Create `app/pages/new_paradox.py`
2. Follow the common structure pattern
3. Add navigation button to all pages
4. Update `home.py` with new button
5. Add documentation to `concepts.md`

### Customizing Styling

**Global Changes:**
- Edit `.streamlit/config.toml` for theme
- Update CSS in each page for consistency

**Page-Specific:**
- Modify CSS in individual page files
- Add custom animations or effects

## Dependencies

### Core (`requirements.txt`)

```
streamlit      # Web framework
numpy          # Numerical computing
matplotlib     # Plotting (backup)
scipy          # Scientific computing
pandas         # Data manipulation
plotly         # Interactive charts
```

### Version Compatibility

- Python 3.11+
- Streamlit 1.49+
- Plotly 5.0+

## Best Practices

### Code Organization

- **One paradox per file** - Easy to maintain
- **Consistent structure** - Predictable layout
- **Self-contained pages** - No shared state between paradoxes

### Styling

- **CSS in markdown blocks** - Streamlit convention
- **Consistent color palette** - Professional appearance
- **Responsive design** - Works on different screen sizes

### User Experience

- **Progress feedback** - Users know simulation is running
- **Clear navigation** - Easy to explore all paradoxes
- **Educational content** - Explanations in expanders
- **Interactive visualizations** - Engaging and informative

---

## Summary

The app is built with **simplicity and modularity** in mind:
- Each paradox is independent
- Common patterns are reused
- Navigation is consistent
- Styling is cohesive
- Code is maintainable

This architecture makes it easy to add new paradoxes, update styling, or modify individual pages without affecting others.
