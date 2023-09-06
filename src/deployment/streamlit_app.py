import base64
import streamlit as st
from streamlit_option_menu import option_menu
from model import tuberculosis_page, cancer_page, pneumonia_page, covid_page
from config import PROJECT_BACKGROUND, PROJECT_GOALS, PROJECT_PROBLEM

# Set Streamlit page configuration
st.set_page_config(
    page_title="Omdena Myanmar",
    page_icon="🇲🇲",
    initial_sidebar_state="expanded"
)

# Function to set page background
def set_page_background(png_file):
    @st.cache_data()
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: scroll;
        }}
        </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Function to hide Streamlit style elements
def hide_streamlit_style():
    hide_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """
    st.markdown(hide_style, unsafe_allow_html=True)

# Set the page background
set_page_background('assets/background.webp')

# Hide Streamlit style elements
hide_streamlit_style()

# CSS styles
css_style = {
    "icon": {"color": "white"},
    "nav-link": {"--hover-color": "grey"},
    "nav-link-selected": {"background-color": "#4ABF7E"},
}

# Loading assets
# img_banner = Image.open("assets/banner.png")
# img_logo = Image.open("assets/logo.png")
img_banner = "assets/banner.png"
img_logo = "assets/logo.png"

# Main menu options
selected = option_menu(
    menu_title=None,
    options=["Home", "Models", "About", "Contributors"],
    icons=["house", "gear", "info-circle", "people"],
    styles=css_style,
    orientation="horizontal"
)

# Function for the model page
def model_page():
    st.sidebar.image("assets/logo.png")
    st.sidebar.write("<h1>Identifying Diseases in Chest X-Rays & COVID-19 Detection</h1><br>", unsafe_allow_html=True)
    selected_task = st.sidebar.selectbox("Select Task", ["Cancer Detection",  "Tuberculosis Detection", "Covid Detection", "Pneumonia Detection"])
    
    if selected_task == "Cancer Detection":
        cancer_page()
    elif selected_task == "Tuberculosis Detection":
        tuberculosis_page()
    elif selected_task == "Pneumonia Detection":
        pneumonia_page()
    elif selected_task == "Covid Detection":
        covid_page()

# Function for the home page
def home_page():
    st.write("# Identifying Diseases in Chest X-Rays & COVID-19 Detection", unsafe_allow_html=True)
    st.image(img_banner)

    st.write(PROJECT_PROBLEM, unsafe_allow_html=True)
    st.write(PROJECT_GOALS, unsafe_allow_html=True)

# Function for the about page
def about_page():
    st.write(PROJECT_BACKGROUND, unsafe_allow_html=True)

# Function for the contributors page
def contributors_page():
    st.success("Thank you everyone")

# Display selected page
if selected == "Home":
    home_page()
elif selected == "Models":
    model_page()
elif selected == "About":
    about_page()
elif selected == "Contributors":
    contributors_page()
