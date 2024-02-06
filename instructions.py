import streamlit as st
from PIL import Image

def instructionsToMenu():
    st.session_state['screen'] = "menu"

def instructionsToMain():
    st.session_state['screen'] = "main"

#instructions and aim page
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
    .instructions-text {
        color: #7ca8d6;
        font-family: 'Gotham', sans-serif;
        font-weight: 500;
        text-align: left;
        font-size: 30px;
        margin-bottom: 0px;
    }
    .body-text {
        color: #e0e0e0;
        font-family: 'Gotham', sans-serif;
        font-weight: 500;
        text-align: left;
        font-size: 18px;
        margin-bottom: 0px;
    </style>
    """,
    unsafe_allow_html=True
)

    st.markdown('<h1 class="title-text">INSTRUCTIONS AND AIM </h1>', unsafe_allow_html=True)
    st.markdown('<p class="instructions-text">Instructions: </p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">1) Go to "menu"</p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">2) Go to "create a poster" </p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">3) Choose if you would like to upload or select a song </p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">4) Upload/select a song, and see the final poster! </p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">5) Save the poster as a PNG for later... </p>', unsafe_allow_html=True)
    st.divider()
    
    st.markdown('<p class="instructions-text">Aim: </p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">This program was created with the purpose of being used in music classes. Music is a very complex subject for students, because a lot of the musical concepts are too difficult to grasp. There are ample musical elements, and understanding how they change in one song compared to another is not easy to understand when numbers are thrown at students. This program therefore tries to create visual posters of songs, that can be used to help explain how different musical elements change in a particular song over time.</p>', unsafe_allow_html=True)
    st.divider()

    st.markdown('<p class="instructions-text">Algorithm Explanation: </p>', unsafe_allow_html=True)
    st.markdown('<p class="body-text">This program was created with the purpose of being used in music classes. Music is a very complex subject for students, because a lot of the musical concepts are too difficult to grasp. There are ample musical elements, and understanding how they change in one song compared to another is not easy to understand when numbers are thrown at students. This program therefore tries to create visual posters of songs, that can be used to help explain how different musical elements change in a particular song over time.</p>', unsafe_allow_html=True)
    st.divider()
    st.markdown('<p class="body-text">The music data is represented over time in a clockwise manner.</p>', unsafe_allow_html=True)
    st.divider()
    st.markdown('<p class="body-text">Based on how high the tempo is, the blue circular pattern is thicker, so for slower tempos the blue pattern is thinner.</p>', unsafe_allow_html=True)
    st.divider()
    st.markdown('<p class="body-text">If the spectral flatness is higher, then looking at the circular bar plot, the bars are longer and also a darker shade of purple</p>', unsafe_allow_html=True)
    st.divider()
    st.markdown('<p class="body-text">When the spectral centroid is higher, the pink sectors in the pie chart are darker</p>', unsafe_allow_html=True)
    st.divider()
    st.markdown('<p class="body-text">When the zero crossing rate is higher, the yellow dots in the circular scatter plot are darker and further away from the center</p>', unsafe_allow_html=True)
    st.divider()
    st.markdown('<p class="body-text">When the spectral contrast is higher, the green dots are darker and further away from the center</p>', unsafe_allow_html=True)
    st.divider()

    st.button("Quit", on_click=instructionsToMain())
    st.button("Menu", on_click=instructionsToMenu())




