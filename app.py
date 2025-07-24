import streamlit as st
st.title("Nike Sales Dashboard")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Nike Sales Dashboard", layout="wide")
st.title("Nike Sales Dashboard")

# Sample chart
data = pd.DataFrame({
    'Region': ['North', 'South', 'East', 'West'],
    'Sales': [120, 90, 150, 100]
})

st.subheader("Sales by Region")
st.bar_chart(data.set_index('Region'))
