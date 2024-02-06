import menu, instructions, createPosterNew, examples, createPosterOptions, uploadedPoster, selectedPoster,selectSongsForPoster
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from readFile import read_file
from editData import *
import altair as alt
import pickle
from PIL import Image

#setting up font and style for whole streamlit app
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			}
			</style>
			"""

st.markdown(streamlit_style, unsafe_allow_html=True)

#hide streamlit footer thing at the bottom
hide_menu_style = """
        <style>
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

#first welcome page
def loadScreen():
    #title layout
    st.markdown(
        """
        <span style="color: #121212;">This is some text</span>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
            .custom-divider::before {
                content: '';
                display: block;
                height: 1px; /* Adjust this value to make the divider thicker */
                background-color: #e0e0e0; /* Divider color */
            }
        </style>
        """
        "<div class='custom-divider'></div>",
        unsafe_allow_html=True
    )

    #visuca image for front
    image = Image.open('BlueComp.png')

    st.image(image)

    st.markdown(
        """
        <style>
            .custom-divider::before {
                content: '';
                display: block;
                height: 1px; /* Adjust this value to make the divider thicker */
                background-color: #e0e0e0; /* Divider color */
            }
        </style>
        """
        "<div class='custom-divider'></div>",
        unsafe_allow_html=True
    )

    st.markdown(
    """
    <style>
    .centered-text {
        color: #e0e0e0;  /* Replace with your desired color */
        font-size: 20px; /* Replace with your desired font size */
        text-align: center;
        margin-bottom: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    st.markdown('<p class="centered-text">The ability to visualize music.</p>', unsafe_allow_html=True)

    st.markdown(
        """
        <style>
            .custom-divider::before {
                content: '';
                display: block;
                height: 1px; /* Adjust this value to make the divider thicker */
                background-color: #e0e0e0; /* Divider color */
            }
        </style>
        """
        "<div class='custom-divider'></div>",
        unsafe_allow_html=True
    )

    #button to go to menu
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        st.button(label = "Start!", on_click=mainToMenu)

#changing session state to go to menu
def mainToMenu():
    st.session_state['screen'] = "menu"

#set it to a default of "main"
if 'screen' not in st.session_state:
    st.session_state['screen'] = "main"

#create the "songs" list
if 'songs' not in st.session_state:
    st.session_state['songs'] = []

if st.session_state['screen'] == "main":
    #loading data in data.txt file
    try:
        pickle_off = open('data.txt', 'rb')
        st.session_state['songs'] = pickle.load(pickle_off)
    except FileNotFoundError:
        pass
    except EOFError:
        pass
    loadScreen()

#based on session state, specific loadscreen function is called to open new page
elif st.session_state['screen'] == "menu":
    menu.loadScreen()
elif st.session_state['screen'] == "instructions":
    instructions.loadScreen()
elif st.session_state['screen'] == "creationOption":
    createPosterOptions.loadScreen()
elif st.session_state['screen'] == "uploadSong":
    createPosterNew.loadScreen()
elif st.session_state['screen'] == "examples":
    examples.loadScreen()
elif st.session_state['screen'] == "uploadedPoster":
    uploadedPoster.loadScreen()
elif st.session_state['screen'] == "selectSong":
    selectSongsForPoster.loadScreen()
elif st.session_state['screen'] == "selectedPoster":
    selectedPoster.loadScreen()


