import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data

st.set_page_config(layout="wide", page_title="Solar Comparison Dashboard")
df = load_data()

st.title("☀️ Solar Potential Comparison - Benin, Sierra Leone, Togo")

# Widget Inputs
countries = st.multiselect("Select countries", options=df['Country'].unique(), default=df['Country'].unique())
metric = st.selectbox("Select Metric", ['GHI', 'DNI', 'DHI'])

filtered_df = df[df['Country'].isin(countries)]

# Boxplot
st.subheader(f"{metric} Distribution by Country")
fig, ax = plt.subplots(figsize=(6, 2))  # 👈 smaller size
sns.boxplot(data=filtered_df, x='Country', y=metric, ax=ax, palette='Set2')
plt.tight_layout()
st.pyplot(fig)

# Summary Table
st.subheader("📊 Summary Statistics")
summary = filtered_df.groupby('Country')[[metric]].agg(['mean', 'median', 'std']).round(2)
st.dataframe(summary)

# Bar Chart: Average Metric by Country
st.subheader(f"📈 Average {metric} by Country")
avg = filtered_df.groupby('Country')[metric].mean().sort_values(ascending=False)
st.bar_chart(avg, use_container_width=True)

# Extra: Sample Count to support dominance of Togo
st.caption("🔢 Sample counts per country:")
st.dataframe(filtered_df['Country'].value_counts().rename_axis('Country').reset_index(name='Count'))
