import streamlit as st

title = st.text_input("학번","이름")
if 'title' not in st.session_state :
    st.session_state.title = "title"
