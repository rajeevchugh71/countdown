import streamlit as st
import time
from datetime import datetime

# 1. Set up the page config
st.set_page_config(page_title="Countdown Timer", page_icon="⏳")

# --- BACKGROUND IMAGE SETUP ---
# Replace this with your specific Skoda Enyaq Graphite Grey image URL
background_image_url = "https://www.elektrischeautolease.nl/app/uploads/2022/04/2022123.png"

st.markdown(
    f"""
    <style>
    .stApp {{
        /* We add a linear-gradient here to create a dark tint (0.5 opacity) over the image */
        background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("{background_image_url}");
        
        /* 'cover' makes it fill the screen */
        background-size: cover;
        
        /* 'center' ensures the middle of the car (usually the subject) is in focus */
        background-position: center center;
        
        /* 'fixed' is the key for mobile: it keeps the background steady */
        background-attachment: fixed;
        
        background-repeat: no-repeat;
    }}
    
    /* Make headers white */
    h1 {{
        color: white !important;
        text-shadow: 2px 2px 4px #000000;
        margin-bottom: 0px;
    }}
    
    /* Make labels white */
    p {{
        color: white !important;
        font-weight: bold;
        font-size: 18px;
        text-shadow: 1px 1px 2px #000000;
        margin-top: -10px; /* Pulls the label closer to the number */
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

    with timer_placeholder.container():
        # Using columns to arrange them side-by-side
        # On mobile, Streamlit might stack these if they get too squeezed, 
        # but usually 4 numbers fit fine.
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown(f"<h1 style='text-align: center; font-size: 40px;'>{days}</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Days</p>", unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"<h1 style='text-align: center; font-size: 40px;'>{hours}</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Hours</p>", unsafe_allow_html=True)
            
        with col3:
            st.markdown(f"<h1 style='text-align: center; font-size: 40px;'>{minutes}</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Mins</p>", unsafe_allow_html=True)
            
        with col4:
            st.markdown(f"<h1 style='text-align: center; font-size: 40px;'>{seconds_display}</h1>", unsafe_allow_html=True)
            st.markdown("<p style='text-align: center;'>Secs</p>", unsafe_allow_html=True)

    time.sleep(1)