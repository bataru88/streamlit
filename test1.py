import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit入門')

st.write('DataFrame')
df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})
st.dataframe(df)
st.table(df.style.highlight_max())

"""
# 章
## 節
### 項

'''python
import streamlit as st
import numpy as np
import pandas as pd
"""

