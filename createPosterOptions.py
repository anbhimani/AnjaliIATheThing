import streamlit as st

#go to page where song can be uploaded
def uploadPoster():
    st.session_state['screen'] = "uploadSong"

#go to page where song can be selected
def selectPoster():
    st.session_state['screen'] = "selectSong"

#go to main page
def posterToMain():
    st.session_state['screen'] = "main"

#go to menu page
def posterToMenu():
    st.session_state['screen'] = "menu"


#loads screen
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

    st.markdown('<h1 class="title-text">Create Your Own Poster</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    #3 buttons
    with col2:
        #upload your own song options
        st.button("Upload your own song", on_click=uploadPoster)
        #select a song option
        st.button("Choose from previously uploaded songs", on_click=selectPoster)
        #go to main page option
        st.button("Quit", on_click=posterToMain())
        st.button("Menu", on_click=posterToMenu())
