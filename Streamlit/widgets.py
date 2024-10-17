import streamlit as st
import pandas as pd
st.title("Stream Text Input")

name = st.text_input("Enter Your Name: ")
age = st.slider("Select Your Age: ", 0, 100, 20)
st.write("Your Age is ", age)
options = ['python', 'c', 'c++', 'java', 'js']
choice = st.selectbox("Choose your Favourite Language: ", options)
st.write("You Select is : ", choice)
if name:
    sst = name.strip()
    spt = name.split()
    countif = 0
    countelse = 0
    for i in range(len(name)):
        if name[i] == 'a':
            ifblock = name[i]
            st.write(ifblock)
            countif += 1
            break
        else:
            elseblock = "not found "
            st.write(elseblock)
            countelse += 1
    st.write(countif)
    st.write(countelse)
    total = countif + countelse
    st.write("Number of Total times: ", total)
    st.write(sst)
    st.write(spt)


data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "Country": ["USA", "UK", "Australia", "Germany"]
}

df = pd.DataFrame(data)
df.to_csv("SampleData.csv")

st.write(df)


uploaded_file = st.file_uploader("Choose CSV file", type='CSV')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
