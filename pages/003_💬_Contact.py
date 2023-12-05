import streamlit as st

st.set_page_config(
    page_title="Contact",
    page_icon="💬",
)
# st.markdown("""
# <style>
# .st-emotion-cache-czk5ss.e16jpq800
# {
#     visibility: hidden;
# }

# .styles_terminalButton__JBj5T
# {
#     visibility: hidden;
# }
# </style>            
# """, unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.title("Contact")