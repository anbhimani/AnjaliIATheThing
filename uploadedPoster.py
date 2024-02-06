import streamlit as st
import altair as alt
from posterFunctions import black_circle, black_circle2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#go to menu
def uploadToMenu():
    st.session_state['screen'] = "menu"

#go to main
def uploadToMain():
    st.session_state['screen'] = "menu"

#load the final poaster
def loadScreen():
    #title layout
    st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gotham:wght@400;500&display=swap');
    .title-text {
        color: #298CF4;
        font-family: 'Gotham', sans-serif;
        font-weight:800;
        text-align: center;
        font-size: 55px;
        margin-top: -50px;
        padding-top: 0px;
    }
    .centered-text {
        color: #e0e0e0;  /* Replace with your desired color */
        font-size: 18px; /* Replace with your desired font size */
        text-align: center;
        margin-bottom: 25px;
    </style>
    """,
    unsafe_allow_html=True
)

    st.markdown('<h1 class="title-text">POSTER</h1>', unsafe_allow_html=True)

    #get all the charts from the object
    centralSpectroid_chart = st.session_state['songs'][-1].spectralCentroid
    zero_chart = st.session_state['songs'][-1].zeroCrossingRate
    tempo_chart = st.session_state['songs'][-1].tempo
    contrast_chart = st.session_state['songs'][-1].contrast
    flatness_chart = st.session_state['songs'][-1].flatness
    blackCircle = alt.layer(black_circle(), black_circle2())

    #dispaly all the charts on the screen
    st.markdown('<p class="centered-text">Scroll down to see entire poster and instructions on saving.</p>', unsafe_allow_html=True)
    firstlChart = alt.layer(centralSpectroid_chart, zero_chart).resolve_scale(color = 'independent')
    titleC = st.session_state['songs'][-1].name + " by " + st.session_state['songs'][-1].artist
    secondChart = alt.layer(flatness_chart, blackCircle, tempo_chart,firstlChart, contrast_chart).resolve_scale(color='independent').properties(title=titleC)
    st.altair_chart(secondChart, use_container_width= True)
    st.button("Quit", on_click=uploadToMain)
    st.button("Menu", on_click=uploadToMenu)

