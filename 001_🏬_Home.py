import streamlit as st

st.set_page_config(
    page_title="PortFolio App",
    page_icon="👋",
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
st.title("Welcome!")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered", st.session_state["my_input"])