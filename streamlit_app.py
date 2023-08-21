# Building a simple App

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st


st.title("Bilal Hussain's Journey to Data Scientist")
st.header('st.write')
st.write("---")
st.write('Hello, *world!* :sunglasses: ')
st.write(12345)

df = pd.DataFrame({
    "First Column" : [1, 2, 3, 4, 5],
    "Second Column" : [10, 20, 30, 40, 50]
})

st.write(df)

st.write('Below is a DataFrame:', df ,'Above is a dataframe.')

df2 = pd.DataFrame(
    np.random.randn(200, 3), 
    columns=['a', 'b', 'c']
)
c = alt.Chart(df2).mark_circle().encode(
    x= 'a', y= 'b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)