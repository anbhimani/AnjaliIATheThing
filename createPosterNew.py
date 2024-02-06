import streamlit as st
from librosaCall import extractFeatures
from readFile import read_file
from editData import *
from music import Music
import pickle, uploadedPoster
from tempfile import NamedTemporaryFile
import os
from posterFunctions import*

#go to menu
def creationToMenu():
    st.session_state['screen'] = "menu"

#move to poster page
def completedUpload():
    st.session_state['screen'] = "uploadedPoster"

#screen
def loadScreen():
    #layout for title text
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

    st.markdown('<h1 class="title-text">Poster Creation</h1>', unsafe_allow_html=True)
    #to go menu
    st.button("Menu", on_click=creationToMenu)
    #text for user
    songName = st.text_input('Song name')
    songArtist = st.text_input('Artist (firstname lastname)')

    #upload button for user to then select song
    upload_file = st.file_uploader("Click here to upload a song (in mp3 format)", type="mp3")

    #once upload completed
    if upload_file != None:
        #take file path and cut it to get just the audio file itself
        with open(os.path.join("tempDir",upload_file.name),"wb") as f:
            f.write(upload_file.getbuffer())
        st.success("tempDir/" + upload_file.name)
        #using librosa library to extract features
        extractFeatures("tempDir/" + str(upload_file.name))

        #reading in the music data
        s1 = read_file('output/file.csv')

        #splitting each feature into seperate lists
        zeroDraft = s1[0]
        tempoDraft = s1[1]
        spectralDraft = s1[2]
        contrastDraft = s1[3]
        flatnessDraft = s1[4]

        #editing the data to get it to the right length
        zeroCross1, tempo1, spectralCentroid, contrast, flatness1 = dataCut(zeroDraft, tempoDraft, spectralDraft, contrastDraft, flatnessDraft)

        #getting all of the altair charts
        zero_chart_plot = zeroCrossPattern(zeroCross1, zeroDraft)
        spectralCentroid_chart_plot = spectralCentroidPattern(spectralCentroid, spectralDraft)
        tempo_chart_plot = tempoPattern(tempo1, tempoDraft)
        contrast_chart_plot = contrastPattern(contrast, contrastDraft)
        flatness_chart_plot = flatnessPattern(flatness1, flatnessDraft)

        #creating a new Music object with each chart as its attribute
        song = Music(songName, songArtist, zero_chart_plot, tempo_chart_plot, spectralCentroid_chart_plot, contrast_chart_plot, flatness_chart_plot)

        #appending the song to the list 'songs' in session_state
        length1 = len(st.session_state['songs'])
        st.session_state['songs'].append(song)

        #try to open the data text, and dump songs list; could cause error if first time
        try:
            with open('data.txt', 'wb') as fh:
                pickle.dump(st.session_state['songs'], fh)
        except:
            pass

        #remove/delete the song that was uploaded
        os.remove("tempDir/" + str(upload_file.name))

        #open data file and load it
        file = open("data.txt","rb")
        try:
            songsList = pickle.load(file)
        except EOFError:
            pass
        file.close()

        #if the length of the songs list has increased, then done with processing, so allow user to go to next page
        if len(st.session_state['songs']) == length1+1:
            st.button("Next", on_click=completedUpload())
