# Application Structure

This document explains the architecture and organization of the Probability Paradoxes app.

## Directory Structure

```
Paradoxes/
├── app/
│   ├── app.py                 # Entry point (redirects to home)
│   ├── components.py          # Shared CSS, navigation bar, and footer helpers
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

**Data Processing:**
- **NumPy** - Numerical computations (Birthday simulation)

**Styling:**
- **Custom CSS** - Gradient backgrounds, button effects
- **Streamlit Theming** - Light theme with custom colors

## Page Architecture

### Shared Helpers (`app/components.py`)

The CSS, top navigation bar, and footer are identical across pages, so they
live in one module instead of being copy-pasted:

- `inject_css(extra="")` — injects the shared base styling (gradient
  background + animated buttons). Pages pass page-specific rules (e.g. the
  Monty Hall result animation) via the `extra` argument.
- `render_nav(current)` — renders the 6-button nav bar, disabling the button
  for the `current` page path.
- `render_footer()` — renders the shared footer.

The single source of truth for the nav order is the `PAGES` list in
`components.py`; adding an entry there updates the bar on every page at once.

### Common Structure

Each paradox page follows this pattern:

```python
import streamlit as st
import [required libraries]
from components import inject_css, render_nav, render_footer

# 1. Page Configuration
st.set_page_config(
    page_title="...",
    page_icon="...",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Styling + navigation (shared helpers)
inject_css()                       # optionally inject_css("...page-specific CSS...")
render_nav("pages/this_page.py")

# 3. Page Title & Subtitle
st.title("...")
st.markdown("### ...")

# 4. Content Sections (in containers)
with st.container(border=True):
    # The Setup
    # The Simulation
    # The Results

# 5. Explanation (expandable)
with st.expander("Why is this a paradox?"):
    # Mathematical explanation

# 6. Footer (shared helper)
render_footer()
```

### Navigation System

**Top Navigation Bar:**
- Present on every page (rendered via `render_nav()`)
- 6 buttons in a row, driven by the `PAGES` list in `components.py`
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
2. Follow the common structure pattern (use the shared helpers)
3. Add the new page to the `PAGES` list in `components.py` — this updates the
   nav bar on every page automatically
4. Update `home.py` with a launch button
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
numpy          # Numerical computing (Birthday simulation)
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
