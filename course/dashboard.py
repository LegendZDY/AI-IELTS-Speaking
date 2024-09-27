import streamlit as st

if 'images_count' not in st.session_state:
    st.session_state.images_count = 0

st.image("static/dash.png")
col1, col2, col3 = st.columns(3)
with col1:
    with st.container(height=140):
        st.subheader(":rainbow[Sport topic]")
        if st.button(":material/arrow_forward: :green[Go to train page]",key="3", use_container_width=True):
            st.session_state.images_count = 0
            st.switch_page("chats/chats.py")

with col2:
    with st.container(height=140):
        st.subheader(":rainbow[Online topic]")
        if st.button(":material/arrow_forward: :green[Go to train page]",key="2", use_container_width=True):
            st.session_state.images_count = 1
            st.switch_page("chats/chats.py")

with col3:
    with st.container(height=140):
        st.subheader(":rainbow[Cook topic]")
        if st.button(":material/arrow_forward: :green[Go to train page]",key="1", use_container_width=True):
            st.session_state.images_count = 2
            st.switch_page("chats/chats.py")
        

col4, col5, col6 = st.columns(3)
with col4:
    with st.container(height=140):
        st.subheader(":rainbow[Pets topic]")
        if st.button(":material/arrow_forward: :green[Go to train page]",key="4", use_container_width=True):
            st.session_state.images_count = 3
            st.switch_page("chats/chats.py")
with col5:
    with st.container(height=140):
        st.subheader(":rainbow[School topic]")
        if st.button(":material/arrow_forward: :green[Go to train page]",key="5", use_container_width=True):
            st.session_state.images_count = 4
            st.switch_page("chats/chats.py")
with col6:
    with st.container(height=140):
        st.subheader(":rainbow[Travel topic]")
        if st.button(":material/arrow_forward: :green[Go to train page]",key="6", use_container_width=True):
            st.session_state.images_count = 5
            st.switch_page("chats/chats.py")

