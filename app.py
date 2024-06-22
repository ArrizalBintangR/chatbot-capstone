import streamlit as st
import os
from streamlit_navigation_bar import st_navbar
import pages as pg
import uuid

# st.set_page_config(page_title="NIRVITA, Your AI Dermatologist Assistant", page_icon="🌟", initial_sidebar_state="collapsed")
hide_sidebar_style = """
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="stSidebarNav"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)
pages = ["Home", "Feature", "About"]
styles = {
    "nav": {
        "background-color": "#95D2B3",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "color": "#365E32",
        "font-weight": "bold",
        "padding": "14px",
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}
page = st_navbar(
    pages,
    styles=styles,
    options=options
)

functions = {
    "Home": pg.show_home,
    "Feature": pg.show_feature,
    "About": pg.show_about,
}

go_to = functions.get(page)
if go_to:
    go_to()
