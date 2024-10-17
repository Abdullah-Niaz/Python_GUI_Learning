import streamlit as st

st.title("Stream Text Input")
 
name = st.text_input("Enter Your Name: ")
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
