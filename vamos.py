import streamlit as st 
import pandas as pd


st.set_page_config (page_title= "Santyapp", layout= "wide")


with st.container():
    st.header("hellooooooo")
    st.title ("Mi gran app")
    st.write("GUAPO, PODEROSO, ASOMBROSO")
    st.empty()
    
with st.container ():
    st.write ("---")
    st.header ("CR7")
    st.write("Cristiano Ronaldo")
    st.image (r'C:\Users\Gamer Edition i5 Xtr\Desktop\Santy\Computación - 2\_102469653_gettyimages-962792890.jpg.webp', caption= 'Cristiano Ronaldo')

with st.container():
    st.write("---")
    st.header ("Mi Margot") 
    st.write ("Margot Robbie mi gran crush Harley Quinn")
    st.image (r'C:\Users\Gamer Edition i5 Xtr\Desktop\Santy\Computación - 2\f.elconfidencial.com_original_619_1d5_d12_6191d5d12df3c69a30c1d39a753ca46f.jpg', caption= 'Harley Quinn')

    
