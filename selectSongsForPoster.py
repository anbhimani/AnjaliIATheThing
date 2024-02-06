import streamlit as st

#to go to the final poster
def selectedPoster():
    st.session_state['screen'] = "selectedPoster"

#load the selection options page
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
    st.markdown('<h1 class="title-text">SONG SELECTION</h1>', unsafe_allow_html=True)

    songsAndArtists = []

    #looping through all Music objects
    for i in range(len(st.session_state['songs'])):
        #isolating to get the name and artist and concatenate to form a sentence
        fullName = str(i+1) + ". " + st.session_state['songs'][i].name + " by " + st.session_state['songs'][i].artist
        songsAndArtists.append(fullName)

    #create a selection box with list of all the songs
    st.session_state.songOptions = st.selectbox("Please select the song you would like a poster for", songsAndArtists)

    #show the user what they selected
    st.write('You selected:', st.session_state.songOptions)

    #option to move on to see the final poster
    st.button("Next", on_click=selectedPoster)

