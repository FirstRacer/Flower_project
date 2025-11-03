# flower_web.py
import random
import streamlit as st

# List of beautiful flowers 🌸🌻🌺
flowers = [
    "🌸 Cherry Blossom", "🌼 Daisy", "🌻 Sunflower", "🌹 Rose", "🌷 Tulip", "💐 Lotus",
    "🌺 Hibiscus", "🌻 Marigold", "🌹 Jasmine", "🌼 Daffodil", "🌸 Peony", "🌺 Orchid",
    "🌷 Lily", "🌼 Camellia", "🌻 Dahlia", "🌸 Poppy", "🌺 Violet", "🌷 Iris", "🌼 Magnolia",
    "🌹 Carnation", "💐 Lavender", "🌸 Geranium", "🌺 Zinnia", "🌻 Petunia", "🌷 Azalea",
    "🌼 Chrysanthemum", "🌸 Bluebell", "🌺 Hydrangea", "🌹 Gardenia"
]

# Pretty color choices
colors = ["#e60026", "#ff66b2", "#ff8c00", "#006400", "#32cd32", "#ff1493", "#ff0000", "#ffd700"]

# Streamlit page setup
st.set_page_config(page_title="Name to Flower", page_icon="🌷", layout="centered")

st.markdown("<h1 style='text-align:center; color:#d10000;'>🌷 Name to Flower Generator 🌷</h1>", unsafe_allow_html=True)
st.write("")

name = st.text_input("Enter your name:", max_chars=40)

if st.button("💐 Get My Flower 💐"):
    if not name.strip():
        st.warning("Please enter your name first!")
    else:
        flower = random.choice(flowers)
        color = random.choice(colors)
        st.markdown(f"<h3 style='text-align:center; color:#006400;'>Hello {name}! 🌸 Your flower is 🌸</h3>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align:center; color:{color}; font-family:Lucida Handwriting;'> {flower} </h2>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align:center; color:#b22222; font-style:italic;'>🌷 Let your name bloom into a flower 🌷</p>", unsafe_allow_html=True)
