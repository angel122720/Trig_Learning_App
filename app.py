import streamlit as st
import math
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(page_title="Advanced Trig Explorer", layout="centered")

st.title("📐 Advanced Oblique Triangle Explorer")
st.write("A professional tool for exploring the Law of Sines and Cosines.")

# Sidebar for Inputs
st.sidebar.header("Triangle Dimensions")
a = st.sidebar.number_input("Side a (Opposite to ∠A)", value=7.0)
b = st.sidebar.number_input("Side b (Adjacent to ∠A)", value=10.0)
angle_A = st.sidebar.slider("Angle A (Degrees)", 1, 179, 30)

# Calculations
h = b * math.sin(math.radians(angle_A))
st.subheader("Analysis & Results")

col1, col2 = st.columns(2)
with col1:
    st.metric("Height (h)", round(h, 2))
with col2:
    if angle_A < 90:
        if a < h: status = "No Triangle"
        elif a == h: status = "One Right Triangle"
        elif a >= b: status = "One Triangle"
        else: status = "Ambiguous Case (2 Triangles)"
    else:
        status = "One Triangle" if a > b else "No Triangle"
    st.metric("Outcome", status)

# Drawing the Visualization
fig, ax = plt.subplots()
plt.style.use('dark_background')
# (Simplified visual for web)
ax.plot([0, b * math.cos(math.radians(angle_A))], [0, h], color='#FF4081', marker='o')
ax.axhline(0, color='white', alpha=0.3)
st.pyplot(fig)
