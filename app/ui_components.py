import streamlit as st
import pandas as pd
import plotly.express as px
from utils import get_summary_stats

def country_selector():
    return st.multiselect(
        "Select countries to compare",
        ["Benin", "Sierra Leone", "Togo"],
        default=["Benin", "Sierra Leone", "Togo"]
    )

def metric_selector():
    return st.selectbox(
        "Select metric",
        ["GHI", "DNI", "DHI", "WS", "WSgust", "Tamb", "RH"]
    )

def plot_type_selector():
    return st.selectbox(
        "Select plot type",
        ["Boxplot", "Histogram", "Line", "Scatter"]
    )

def boxplot_section(dfs, metric):
    st.subheader(f"Boxplot of {metric} by Country")
    data = []
    for country, df in dfs.items():
        if metric in df:
            temp = df[[metric]].copy()
            temp["Country"] = country
            data.append(temp)
    if data:
        plot_df = pd.concat(data)
        fig = px.box(plot_df, x="Country", y=metric, color="Country")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available for selected metric or countries.")

def histogram_section(dfs, metric):
    st.subheader(f"Histogram of {metric} by Country")
    data = []
    for country, df in dfs.items():
        if metric in df:
            temp = df[[metric]].copy()
            temp["Country"] = country
            data.append(temp)
    if data:
        plot_df = pd.concat(data)
        fig = px.histogram(plot_df, x=metric, color="Country", barmode="overlay", nbins=30)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available for selected metric or countries.")

def line_section(dfs, metric):
    st.subheader(f"Line Chart of {metric} Over Index (by Country)")
    data = []
    for country, df in dfs.items():
        if metric in df:
            temp = df[[metric]].copy()
            temp["Country"] = country
            temp["Index"] = range(len(temp))
            data.append(temp)
    if data:
        plot_df = pd.concat(data)
        fig = px.line(plot_df, x="Index", y=metric, color="Country", markers=True)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available for selected metric or countries.")

def scatter_section(dfs, metric):
    st.subheader(f"Scatter Plot of {metric} (by Country)")
    # For scatter, we'll plot metric vs. index
    data = []
    for country, df in dfs.items():
        if metric in df:
            temp = df[[metric]].copy()
            temp["Country"] = country
            temp["Index"] = range(len(temp))
            data.append(temp)
    if data:
        plot_df = pd.concat(data)
        fig = px.scatter(plot_df, x="Index", y=metric, color="Country")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available for selected metric or countries.")

def summary_table(dfs, metric):
    st.subheader(f"Summary Table: {metric}")
    stats_df = get_summary_stats(dfs, metric)
    st.dataframe(stats_df, use_container_width=True)

def observations_section(dfs, metric, plot_type):
    st.subheader("Key Observations")
    st.markdown(f"""
    - Current view: **{plot_type}** for **{metric}**.
    - Compare distributions, trends, and outliers across selected countries.
    - Use different plot types and metrics to discover deeper insights!
    """)