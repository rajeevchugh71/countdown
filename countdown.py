import streamlit as st
import time
from datetime import datetime

# 1. Set up the page title
st.set_page_config(page_title="Countdown Timer", page_icon="⏳")

# --- BACKGROUND IMAGE SETUP ---
# Replace the link below with the "Image Address" of the specific photo you want.
# I have put a placeholder image of a Grey Skoda Enyaq here for you.
background_image_url = "https://www.elektrischeautolease.nl/app/uploads/2022/04/2022123.png"

# This little block of code injects CSS (web design styles) into the app
# It sets the background image and forces all text to be white
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    
    /* Make all the big headers white */
    h1 {{
        color: white !important;
        text-shadow: 2px 2px 4px #000000; /* Adds a shadow so text pops */
    }}
    
    /* Make the smaller text labels white */
    p {{
        color: white !important;
        font-weight: bold;
        text-shadow: 1px 1px 2px #000000;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("⏳ Countdown to May 17, 2026")

# 2. Define target date
target_date = datetime(2026, 5, 17, 0, 0, 0)

# 3. Create placeholder
timer_placeholder = st.empty()

# 4. Start the loop
while True:
    now = datetime.now()
    time_left = target_date - now

    if time_left.total_seconds() < 0:
        timer_placeholder.success("The date has arrived!")
        break

    days = time_left.days
    seconds = time_left.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds_display = seconds % 60

    # 5. Display with BIG WHITE text
    with timer_placeholder.container():
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(f"<h1 style='text-align: center; font-size: 60px;'>{days}</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Days</p>", unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"<h1 style='text-align: center; font-size: 60px;'>{hours}</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Hours</p>", unsafe_allow_html=True)
            
        with col3:
            st.markdown(f"<h1 style='text-align: center; font-size: 60px;'>{minutes}</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Minutes</p>", unsafe_allow_html=True)
            
        with col4:
            st.markdown(f"<h1 style='text-align: center; font-size: 60px;'>{seconds_display}</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Seconds</p>", unsafe_allow_html=True)

    time.sleep(1)