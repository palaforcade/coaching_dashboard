import streamlit as st

# Set page config
st.set_page_config(page_title="Hello World App", page_icon="👋", layout="wide")

# Main title
st.title("👋 Hello World!")
st.markdown("---")

# Welcome message
st.header("Welcome to my Streamlit App")
st.write("This is a simple Hello World application built with Streamlit.")

# Interactive elements
st.subheader("Let's interact!")

# Text input
user_name = st.text_input("What's your name?", "World")
st.write(f"Hello, {user_name}! 👋")

# Slider
age = st.slider("How old are you?", 0, 100, 25)
st.write(f"You are {age} years old!")

# Selectbox
favorite_color = st.selectbox(
    "What's your favorite color?",
    ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"],
)
st.write(f"Your favorite color is {favorite_color}!")

# Button
if st.button("Click me!"):
    st.balloons()
    st.success("🎉 You clicked the button! 🎉")

# Sidebar
st.sidebar.header("About")
st.sidebar.info(
    """
This is a simple Hello World Streamlit app.
It demonstrates basic Streamlit components and interactions.
"""
)

# Footer
st.markdown("---")
st.markdown("*Built with ❤️ using Streamlit*")
