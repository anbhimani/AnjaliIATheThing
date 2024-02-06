import streamlit as st
import createPosterNew
from PIL import Image

#go from menu to instructions page
def menuToInstructions():
    st.session_state['screen'] = "instructions"

#go from menu to creating a poster page
def menuToCreation():
    st.session_state['screen'] = "creationOption"

#going from menu to seeing examples
def menuToExamples():
    st.session_state['screen'] = "examples"

def menuToMain():
    st.session_state['screen'] = "main"

#menu page
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
    </style>
    """,
    unsafe_allow_html=True
)

    st.markdown('<h1 class="title-text">MENU</h1>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col2:
        #adding a little gap
        st.markdown('<span style="font-size: 10px; color: #121212">This is smaller text.</span>', unsafe_allow_html=True)
        #all the buttons to go from the menu page to another page
        st.button("Intstructions/Aim", on_click=menuToInstructions)
        st.button("Create a poster", on_click=menuToCreation)
        st.button("Example posters", on_click=menuToExamples)
        st.button("Quit", on_click=menuToMain())
