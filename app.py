import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Nike Sales Dashboard", layout="wide")
st.title("Nike Sales Dashboard")

# Sample data
data = pd.DataFrame({
    'Region': ['North', 'South', 'East', 'West'],
    'Sales': [200, 150, 300, 250],
    'Profit': [50, 40, 80, 60]
})

col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Region")
    st.bar_chart(data.set_index('Region')['Sales'])

with col2:
    st.subheader("Profit by Region")
    st.line_chart(data.set_index('Region')['Profit'])

