import streamlit as st
import altair as alt
from posterFunctions import black_circle2, black_circle

#go to menu
def selectedToMenu():
    st.session_state['screen'] = "menu"

#go to main page
def selectedToMain():
    st.session_state['screen'] = "main"

#creating chart
def loadScreen():
    #setting title layout
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

    #accessing the value for the song which was selected in the selection box
    selectedSong = st.session_state.songOptions
    #isolating the number at the start of the option, to get index
    number = selectedSong.split()
    index = int(number[0][0]) -1

    #accessing all the charts for the specific Music object
    centralSpectroid_chart = st.session_state['songs'][index].spectralCentroid
    zero_chart = st.session_state['songs'][index].zeroCrossingRate
    tempo_chart = st.session_state['songs'][index].tempo
    contrast_chart = st.session_state['songs'][index].contrast
    flatness_chart = st.session_state['songs'][index].flatness
    blackCircle = alt.layer(black_circle(), black_circle2())

    st.markdown('<p class="centered-text">Scroll down to see entire poster and instructions on saving.</p>', unsafe_allow_html=True)

    #displaying all the charts so that they are layered together
    firstlChart = alt.layer(centralSpectroid_chart, zero_chart).resolve_scale(color = 'independent')
    titleC = st.session_state['songs'][index].name + " by " + st.session_state['songs'][index].artist
    secondChart = alt.layer(flatness_chart, blackCircle, tempo_chart,firstlChart, contrast_chart).resolve_scale(color='independent').properties(title=titleC)
    st.altair_chart(secondChart, use_container_width= True)
    st.button("Menu", on_click=selectedToMenu)
    st.button("Quit", on_click=selectedToMain)
