import streamlit as st
import requests
import pandas as pd

def get_repo_data(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

repo_data = get_repo_data("wahabu", "wahabu")

if repo_data:
    st.title(repo_data["name"])
    st.write("Description:", repo_data["description"])
    st.write("Forks Count:", repo_data["forks_count"])
    st.write("Stars:", repo_data["stargazers_count"])
    # I will add more info as needed
else:
    st.error("Error fetching repo data")


st.title("PortFolio App")
st.write("This is my App")
button1 = st.button("Click Here")

if button1:
    st.write("This is some text.")
    
like = st.checkbox("Do you like this app?")
button2 = st.button("Submit")
if button2:
    if like:
        st.write("Thanks. I like it too.")
    else:
        st.write("I'm sorry. You have bad tastes.")
        
st.header("Start of the Radio Button Section")
animal = st.radio("What animal is your favorite?", ("Lion", "Tiger", "Bear"))
button3 = st.button("Submit Animal")
if button3:
    st.write(animal)
    if animal == "Lion":
        st.write("ROAR!")
        
st.header("Start of the Selectbox Section")
animal_2 = st.selectbox("What animal is your favorite?", ("Lion", "Tiger", "Bear"))
button4 = st.button("Submit Animal 2")
if button4:
    st.write(animal_2)
    if animal_2 == "Lion":
        st.write("ROAR!")
        
st.header("Start of the Multiselect Section")
options = st.multiselect("What animals do you like?", ["Lion", "Tiger", "Bear"])
button5 = st.button("Print Animals")
if button5:
    st.write(options)
    
st.header("Start of the Slider Section")
epochs_num = st.slider("How many epochs?, 2, 100, 10")
if st.button("Slider Button"):
    st.write(epochs_num)
    
st.header("Start of the Text Input Section")
user_text = st.text_input("What's your favorite movie?", "Avatar")
if st.button("Text Button"):
    st.write(user_text)
    
user_num = st.number_input("What's your favorite number?")
if st.button("Number Button"):
    st.write(user_num)

def run_sentiment_analysis(txt):
    st.write(f"Analysis Done.{txt}")

txt = st.text_area('Text to analyze', '''It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair''')
st.write('Sentiment:', run_sentiment_analysis(txt))
