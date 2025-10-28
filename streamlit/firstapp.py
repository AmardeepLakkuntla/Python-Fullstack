import streamlit as st

st.title("DAILOUGE RAJA🎬🎞️✮")
st.write("This is first dailouge" )
 
Dialouge=st.text_input("what is your favorite dailouge?")
st.button("click me")
Movie=st.text_input("movie name?")
st.button("click me2")
Actor=st.text_input("enter the actor name?")
st.button("click me3")

if Dialouge and Movie and Actor:
    st.write(f" {Dialouge} in {Movie} by {Actor} was awesome!")