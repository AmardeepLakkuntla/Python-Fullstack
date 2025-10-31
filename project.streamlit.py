import streamlit as st
import requests
 
res = requests.get("https://dummyjson.com/products")
 
if res.status_code == 200:
    res = res.json()
    products = res["products"]
 
 
cols = st.columns([1,2,1])
 
with cols[1]:
    st.title("Product Store")
    search_phrase = st.text_input("Search")
 
for i in products:
 
    if search_phrase.lower() in i["title"].lower():
 
        with st.container(border=True):
             rows = st.columns([4,2])
 
        with rows[0]:
            st.write(f"{i["title"]}")
            st.write(f"BRAND: {i['brand']}")
            st.write(f"CATEGORY: {i["category"]}")
            st.write(f"RATING: {i["rating"]}")
            st.write(f"DESCRIPTION: {i["description"]}")
   
        with rows[1]:
            st.image(i["thumbnail"])
    else:
        st.error("Failed to fetch products")
 
 
 
 
         