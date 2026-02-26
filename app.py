import streamlit as st
from PIL import Image 

st.title("Esta es mi primera app en la nube")

st.header("En este espacio comienzo a desarrollar mis aplicaciones.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('carita_feliz.jpg')
st.image(image, caption='Interfaces multimodales')
                   
texto = st.text_input('escribe algo','este es mi texto')
st.write('el texto escrito es', texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Tilin")
  st.write("nose jaja")
  resp =st.checkbox('Estoy deacuerdo')
  if resp:
    st.write('correcto!')

with col2:
  st.subheader("esta es la segunda columna")
  modo = st.radio("Que Modalidad es la principal",("visual","auditivo","tactil"))
  if modo == "visual":
    st.write("1")
  if modo == "auditiva":
    st.write("2")
  if modo == "tactil":
    st.write("3")
