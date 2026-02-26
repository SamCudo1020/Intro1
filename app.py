import streamlit as st
from PIL import Image 

st.title("Esta es mi primera app en la nube")

st.header("En este espacio comienzo a desarrollar mis aplicaciones.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('carita_feliz.jpg')
st.image(image, caption='Interfaces multimodales')
                   
