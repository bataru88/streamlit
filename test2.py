import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit入門')

st.write('DataFrame')
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.78],
   columns=('lat','lon')
)
#st.dataframe(df)
#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)
st.map(df)

st.write('Display Image')
img = Image.open('おに.JPG')
st.image(img,caption='おにぎり',use_column_width=True)

"""
# 章
## 節
### 項

'''python
import streamlit as st
import numpy as np
import pandas as pd
'''
"""