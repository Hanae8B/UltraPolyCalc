import os
import pandas as pd
import streamlit as st

st.set_page_config(page_title="UltraPolyCalc - Polymer Property Explorer")

st.title("UltraPolyCalc - Polymer Property Explorer")

data_path = os.path.join("data", "polymers.csv")

if not os.path.exists(data_path):
    st.error(f"Error: Polymer data file not found at '{data_path}'.\nPlease make sure 'polymers.csv' exists in the 'data' folder.")
    st.stop()

# Load polymer data
polymers_df = pd.read_csv(data_path)

# Convert columns to correct types
polymers_df["MolecularWeight"] = pd.to_numeric(polymers_df["MolecularWeight"], errors="coerce")
polymers_df["GlassTransitionTemp"] = pd.to_numeric(polymers_df["GlassTransitionTemp"], errors="coerce")
polymers_df["Density"] = pd.to_numeric(polymers_df["Density"], errors="coerce")

# Remove rows with missing values in key columns to avoid errors
polymers_df = polymers_df.dropna(subset=["MolecularWeight", "GlassTransitionTemp", "Density"])

# Sidebar filters
st.sidebar.header("Filter Polymers")

min_mw = st.sidebar.number_input(
    "Min Molecular Weight (g/mol)",
    min_value=float(polymers_df["MolecularWeight"].min()),
    max_value=float(polymers_df["MolecularWeight"].max()),
    value=float(polymers_df["MolecularWeight"].min())
)

max_mw = st.sidebar.number_input(
    "Max Molecular Weight (g/mol)",
    min_value=float(polymers_df["MolecularWeight"].min()),
    max_value=float(polymers_df["MolecularWeight"].max()),
    value=float(polymers_df["MolecularWeight"].max())
)

min_tg = st.sidebar.number_input(
    "Min Glass Transition Temp (°C)",
    min_value=float(polymers_df["GlassTransitionTemp"].min()),
    max_value=float(polymers_df["GlassTransitionTemp"].max()),
    value=float(polymers_df["GlassTransitionTemp"].min())
)

max_tg = st.sidebar.number_input(
    "Max Glass Transition Temp (°C)",
    min_value=float(polymers_df["GlassTransitionTemp"].min()),
    max_value=float(polymers_df["GlassTransitionTemp"].max()),
    value=float(polymers_df["GlassTransitionTemp"].max())
)

min_density = st.sidebar.number_input(
    "Min Density (g/cm³)",
    min_value=float(polymers_df["Density"].min()),
    max_value=float(polymers_df["Density"].max()),
    value=float(polymers_df["Density"].min())
)

max_density = st.sidebar.number_input(
    "Max Density (g/cm³)",
    min_value=float(polymers_df["Density"].min()),
    max_value=float(polymers_df["Density"].max()),
    value=float(polymers_df["Density"].max())
)

# Validate input ranges
if min_mw > max_mw:
    st.sidebar.error("Min Molecular Weight cannot be greater than Max Molecular Weight.")
if min_tg > max_tg:
    st.sidebar.error("Min Glass Transition Temp cannot be greater than Max Glass Transition Temp.")
if min_density > max_density:
    st.sidebar.error("Min Density cannot be greater than Max Density.")

# Filter polymers based on inputs
filtered_df = polymers_df[
    (polymers_df["MolecularWeight"] >= min_mw) & (polymers_df["MolecularWeight"] <= max_mw) &
    (polymers_df["GlassTransitionTemp"] >= min_tg) & (polymers_df["GlassTransitionTemp"] <= max_tg) &
    (polymers_df["Density"] >= min_density) & (polymers_df["Density"] <= max_density)
]

st.markdown(f"### Polymers matching filter criteria: {len(filtered_df)}")

if len(filtered_df) > 0:
    st.dataframe(filtered_df.reset_index(drop=True))
else:
    st.write("No polymers matched the filter criteria.")

if st.checkbox("Show all polymers"):
    st.markdown("### All Polymers")
    st.dataframe(polymers_df.reset_index(drop=True))