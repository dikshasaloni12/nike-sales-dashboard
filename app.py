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

import pandas as pd

df = pd.read_csv("your_data.csv")  # replace with your actual filename or data source

st.sidebar.header("Filter Options")
selected_region = st.sidebar.selectbox("Select Region", df['Region'].unique())
selected_category = st.sidebar.selectbox("Select Category", df['Category'].unique())

filtered_df = df[(df['Region'] == selected_region) & (df['Category'] == selected_category)]

st.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")
st.metric("Total Profit", f"${filtered_df['Profit'].sum():,.2f}")
st.metric("Units Sold", f"{filtered_df['Units'].sum():,}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Month")
    monthly_sales = filtered_df.groupby('Month')['Sales'].sum()
    st.line_chart(monthly_sales)

with col2:
    st.subheader("Profit by Category")
    category_profit = filtered_df.groupby('Category')['Profit'].sum()
    st.bar_chart(category_profit)

import seaborn as sns
import matplotlib.pyplot as plt

st.subheader("Sales Heatmap by Region and Month")
heatmap_data = filtered_df.pivot_table(index='Region', columns='Month', values='Sales', aggfunc='sum')

fig, ax = plt.subplots()
sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="YlGnBu", ax=ax)
st.pyplot(fig)

from sklearn.linear_model import LinearRegression

# Example: Predict future sales based on month
X = filtered_df[['Month']]
y = filtered_df['Sales']
model = LinearRegression().fit(X, y)
future_months = pd.DataFrame({'Month': [13, 14, 15]})
predictions = model.predict(future_months)

st.subheader("Sales Forecast")
st.write(f"Predicted Sales for Month 13: ${predictions[0]:,.2f}")


