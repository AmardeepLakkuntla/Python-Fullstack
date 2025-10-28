import streamlit as st 


cols=st.columns([0.3 , 3 , 0.3])


    
with cols[1]:
    st.subheader("musicon")
    with st.container(border=True):
      cols1=st.columns([3, 2])
      with cols1[0]:
        title="The Twilight sad - There's A girl in the corer"
        st.write(title[:34 ] + '.......')
      with cols1[1]:
        st.write("https://img.youtube.com/vi/l8H38U4nZag/hqdefault.jpg")
          
        
      

