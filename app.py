import streamlit as st

dashboard = st.Page(
    "course/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True
)
chat = st.Page(
    "chats/chats.py", title="Individual training", icon=":material/chat:"
)

pg = st.navigation(
    {
        "courses": [dashboard],
        "chats": [chat],
    }
)
pg.run()