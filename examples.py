import streamlit as st

#go to menu page
def exampleToMenu():
    st.session_state['screen'] = "menu"

#go to main page
def exampleToMain():
    st.session_state['screen'] = "main"
#examples screen
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

# Display the title with the custom color and font
    st.markdown('<h1 class="title-text">CHART EXAMPLES</h1>', unsafe_allow_html=True)
    st.image('image1.png', caption = 'Example 1')
    st.divider()
    st.image('image2.png', caption = 'Example 2')
    st.divider()
    st.image('image3.png', caption = 'Example 3')
    st.divider()
    st.image('image4.png', caption = 'Example 4')
    st.divider()

    st.button("Menu", on_click=exampleToMenu)
    st.button("Quit", on_click=exampleToMain)

