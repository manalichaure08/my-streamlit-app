import streamlit as st
import time
import os

# Set page title and configuration
st.set_page_config(
    page_title="Manali's Cute Poké-World",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Load custom CSS to style the app with a cute, pastel Pokémon aesthetic
def local_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600&family=Pacifico&display=swap');

    /* Background and global styles */
    .stApp {
        background: linear-gradient(135deg, #FFF9A6 0%, #FFD1DC 100%);
        font-family: 'Fredoka', sans-serif;
    }

    /* Change all default text to use Fredoka font */
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, label, input {
        font-family: 'Fredoka', sans-serif !important;
        color: #4A4A4A !important;
    }

    /* Main Container/Card styling */
    .cute-card {
        background: rgba(255, 255, 255, 0.85);
        border-radius: 24px;
        padding: 30px;
        box-shadow: 0 10px 30px rgba(255, 182, 193, 0.4);
        border: 4px solid #FFF;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    /* Title styling */
    .cute-title {
        font-family: 'Pacifico', cursive !important;
        color: #FF69B4 !important;
        font-size: 2.8rem;
        margin-bottom: 10px;
        text-shadow: 2px 2px #FFF;
    }

    .cute-subtitle {
        color: #FF8DA1 !important;
        font-size: 1.2rem;
        margin-bottom: 20px;
        font-weight: 600;
    }

    /* Button customization */
    div.stButton > button {
        background: linear-gradient(135deg, #FF8DA1 0%, #FFB6C1 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        border: 2px solid #FFF !important;
        border-radius: 25px !important;
        padding: 10px 35px !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(255, 141, 161, 0.4) !important;
        cursor: pointer;
        display: block;
        margin: 0 auto;
    }

    div.stButton > button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 6px 20px rgba(255, 141, 161, 0.6) !important;
        background: linear-gradient(135deg, #FFB6C1 0%, #FF8DA1 100%) !important;
    }

    div.stButton > button:active {
        transform: scale(0.98) !important;
    }

    /* Input box customization */
    .stTextInput>div>div>input {
        border-radius: 15px !important;
        border: 2px solid #FFB6C1 !important;
        background-color: rgba(255, 255, 255, 0.9) !important;
        padding: 10px 15px !important;
        color: #4A4A4A !important;
        font-size: 1rem !important;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #FF69B4 !important;
        box-shadow: 0 0 8px rgba(255, 105, 180, 0.3) !important;
    }

    /* Selectbox customization */
    .stSelectbox>div>div {
        border-radius: 15px !important;
        border: 2px solid #FFB6C1 !important;
        background-color: rgba(255, 255, 255, 0.9) !important;
    }

    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Progress bar customization */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #FFF9A6, #FF8DA1) !important;
    }
    </style>
    """, unsafe_allow_html=True)

local_css()

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 0

# Page content definition (lines, images, descriptions)
pages = [
    {
        "text": "Hi, I'm Manali! Welcome to the very first website I created! 💕🌸",
        "image": "assets/welcome_pikachu.png",
        "button": "Enter the Poké-Love Zone ✨"
    },
    {
        "text": "Are you a Pikachu? Because you are shockingly beautiful! ⚡💛",
        "image": "assets/welcome_pikachu.png",
        "button": "Catch my heart next! 👉"
    },
    {
        "text": "I think I need a Paralyze Heal, because you are stunningly gorgeous! 😵💖",
        "image": "assets/flirty_eevee.png",
        "button": "Keep going! 👉"
    },
    {
        "text": "Are you Jigglypuff? Because every time you sing, I fall asleep dreaming of you! 🎤🎶",
        "image": "assets/love_jigglypuff.png",
        "button": "Next adventure! 👉"
    },
    {
        "text": "Even a Master Ball couldn't catch how much I adore you! 🔮✨",
        "image": "assets/welcome_pikachu.png",
        "button": "One more! 👉"
    },
    {
        "text": "Are you a Ditto? Because you look exactly like my next partner! 🧬💕",
        "image": "assets/flirty_eevee.png",
        "button": "Reveal the final test! 🏆"
    }
]

# Title bar (always present, but styled cute)
st.markdown("<div class='cute-title' style='text-align: center;'>Manali's Poké-Love World</div>", unsafe_allow_html=True)
st.markdown("<div class='cute-subtitle' style='text-align: center;'>A super cute interactive website made with love 💖</div>", unsafe_allow_html=True)

# Main container
st.markdown("<div class='cute-card'>", unsafe_allow_html=True)

if st.session_state.page < len(pages):
    # Render the current step
    current_page = pages[st.session_state.page]
    
    # Display cute image if exists
    if os.path.exists(current_page["image"]):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(current_page["image"], use_container_width=True)
            
    st.markdown(f"<h3 style='margin-top: 15px; margin-bottom: 25px; line-height: 1.5;'>{current_page['text']}</h3>", unsafe_allow_html=True)
    
    # Next button
    if st.button(current_page["button"]):
        st.session_state.page += 1
        st.rerun()

else:
    # Final page: Interactive compatibility matcher!
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists("assets/love_jigglypuff.png"):
            st.image("assets/love_jigglypuff.png", use_container_width=True)
            
    st.markdown("<h3>💖 Poké-Love Compatibility Matcher 💖</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.05rem;'>Let's see if we are a perfect match! Enter your name below:</p>", unsafe_allow_html=True)
    
    # User Inputs
    user_name = st.text_input("Your Name:", placeholder="E.g., Ash Ketchum")
    fav_pokemon = st.selectbox(
        "Choose your favorite Pokemon partner:",
        ["Pikachu ⚡", "Eevee 🦊", "Jigglypuff 🎈", "Togepi 🥚", "Snorlax 💤", "Charizard 🔥"]
    )
    
    if st.button("Calculate Compatibility! 🔮"):
        if user_name.strip() == "":
            st.warning("Please enter your name first! 🌸")
        else:
            with st.spinner("Analyzing your Poké-waves... 🔄"):
                time.sleep(1.5)  # Cute delay for effect
                
            # Compatibility logic: deterministic based on user_name to make it feel like a real calculation
            name_sum = sum(ord(c) for c in user_name)
            score = 80 + (name_sum % 21)  # Ensure score is between 80% and 100% because we are positive!
            
            # Show balloons on success
            st.balloons()
            
            # Displays
            st.markdown(f"<h4>Compatibility Score for {user_name} & {fav_pokemon}:</h4>", unsafe_allow_html=True)
            st.progress(score / 100.0)
            st.markdown(f"<h2 style='color: #FF69B4 !important;'>{score}% MATCH! 💘</h2>", unsafe_allow_html=True)
            
            # Cute messages based on selection
            descriptions = {
                "Pikachu ⚡": "You and Pikachu are sparks flying! A shockingly electric match. ⚡💛",
                "Eevee 🦊": "You and Eevee have infinite potential! Together, you can adapt to any cute adventure. 🦊🌸",
                "Jigglypuff 🎈": "Jigglypuff sings the sweetest lullaby just for you! Sweet dreams guaranteed. 🎤💤",
                "Togepi 🥚": "A bundle of happiness! You bring good fortune and joy to each other. 🥚✨",
                "Snorlax 💤": "You are a match made in cozy heaven. Nap time is the best time! 💤🧸",
                "Charizard 🔥": "Your love is burning hot and super powerful! Unstoppable together. 🔥❤️"
            }
            st.info(descriptions[fav_pokemon])
            
            st.toast(f"Congratulations {user_name}! You caught a wild heart! 💖", icon="🎉")

    st.markdown("<hr style='border: 1px dashed #FFB6C1; margin-top: 25px; margin-bottom: 20px;'>", unsafe_allow_html=True)
    if st.button("Restart Journey 🔄"):
        st.session_state.page = 0
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
