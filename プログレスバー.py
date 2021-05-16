import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit入門')


st.write('プログレスバーの表示')

'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!!!!'


#if st.checkbox('showImage'):
#    img = Image.open('おに.JPG')
#    st.image(img,caption='おにぎり',use_column_width=True)

#option = st.selectbox(
#    'あなたが好きな数字を教えてください',
#    list(range(1,11))
#)
#'あなたが好きな数字は',option,'です。'

#sidebarで要素をサイドバーにうつす

#st.write('Interactive Wigts')
#text = st.sidebar.text_input('あなたの趣味を教えてください。')
#'あなたの趣味は',text,'です。'
#
#condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)
#'コンディション:',condition

left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ内容を書く')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ内容を書く')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ内容を書く')

