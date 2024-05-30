# 실행작업
# streamlit run streamlit1.py
# How to Convert a Streamlit App to an .EXE Executable
import streamlit as st

st.title("Hello World!")

st.markdown("This runs entirely in the browser : computer: ")

st.markdown("You can embed Streamlit apps in a static Github page!")

import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

st.markdown("Link in the description below!")