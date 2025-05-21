import streamlit as st
import pandas as pd
from utils import load_country_data, get_summary_stats
from ui_components import (
    country_selector,
    metric_selector,
    plot_type_selector,
    boxplot_section,
    histogram_section,
    line_section,
    scatter_section,
    summary_table,
    observations_section
)

st.set_page_config(
    page_title="Solar Country Comparison Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Solar Challenge: Country Comparison Dashboard")
st.markdown("""
This dashboard lets you compare solar resource metrics across Benin, Sierra Leone, and Togo.
Select countries, metrics, and plot types below to visualize and compare.
""")

# ---- UI Controls above the graph ----
with st.container():
    # Countries selector, full width
    selected_countries = country_selector()

    # Put metric and plot type side-by-side
    col1, col2 = st.columns(2)
    with col1:
        selected_metric = metric_selector()
    with col2:
        selected_plot = plot_type_selector()

    st.caption("Data is loaded from local cleaned CSV")

# ---- Load data ----
dfs = load_country_data(selected_countries)

# ---- Render the selected plot type ----
if selected_plot == "Boxplot":
    boxplot_section(dfs, selected_metric)
elif selected_plot == "Histogram":
    histogram_section(dfs, selected_metric)
elif selected_plot == "Line":
    line_section(dfs, selected_metric)
elif selected_plot == "Scatter":
    scatter_section(dfs, selected_metric)

# ---- Main summary and observations ----
summary_table(dfs, selected_metric)
observations_section(dfs, selected_metric, selected_plot)