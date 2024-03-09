import streamlit as st
from streamlit_free_text_select import st_free_text_select

options = [
    "Option 1",
    "Option 2",
    "Option 3",
    "Option 4",
    "Option 5",
    "Option 6",
    "Option 7",
    "Option 8",
    "Option 9",
    "Option 10",
    "Option 11",
    "Option 12",
    "Option 13",
    "Option 14",
    "Option 15",
    "Option 16",
    "Option 17",
    "Option 18",
    "Option 19",
    "Option 20",
]

value = st_free_text_select(
    label="Free text select",
    options=options,
    format_func=lambda x: x.lower(),
    placeholder="enter question",
    disabled=False,
    delay=300,
)
st.write("Free text select value:", value)
