import streamlit as st
import pandas as pd
from pathlib import Path
import time

# Page setup
st.set_page_config(page_title="PSW", layout="wide")

EXCEL_FILE = r"D:\Test dashboard\PSW.xlsx"

# JavaScript-based auto-refresh every 10 seconds
refresh_interval = 10
st.markdown(f"""
    <script>
        setTimeout(function() {{
            window.location.reload();
        }}, {refresh_interval * 1000});
    </script>
""", unsafe_allow_html=True)

st.title("📊 PSW")

# Load data function (no caching)
def load_data(file_path):
    return pd.read_excel(file_path)

# Check if file exists
file_path = Path(EXCEL_FILE)
if not file_path.exists():
    st.error(f"Excel file not found at: {EXCEL_FILE}")
else:
    data = load_data(file_path)

    #st.subheader("Raw Data")


    st.dataframe(data, use_container_width=True)

    #st.subheader("Summary Statistics")
    #st.write(data.describe())

    #if "Category" in data.columns and "Amount" in data.columns:
        #st.subheader("Total Amount by Category")
        #category_totals = data.groupby("Category")["Amount"].sum().reset_index()
        #st.bar_chart(category_totals.set_index("Category"))

#st.info(f"⏱️ This page auto-refreshes every {refresh_interval} seconds.")
st.rerun()
