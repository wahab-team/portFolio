import streamlit as st

st.set_page_config(
    page_title="Projects",
    page_icon="📚",
)
st.markdown("""
<style>
.st-emotion-cache-czk5ss.e16jpq800
{
    visibility: hidden;
}

.styles_terminalButton__JBj5T
{
    visibility: hidden;
}
</style>            
""", unsafe_allow_html=True)
st.title("Projects")

st.write("You have entered", st.session_state["my_input"])