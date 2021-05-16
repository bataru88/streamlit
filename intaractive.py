import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit入門')


st.write('Display Image')

#if st.checkbox('showImage'):
#    img = Image.open('おに.JPG')
#    st.image(img,caption='おにぎり',use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)
'あなたが好きな数字は',option,'です。'

st.write('Interactive Wigts')
text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味は',text,'です。'

condition = st.slider('あなたの今の調子は？',0,100,50)
'コンディション:',condition