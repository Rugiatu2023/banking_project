import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Page setup ---
st.set_page_config(page_title="RFM Customer Segmentation", layout="wide")

st.title("💎 RFM Customer Segmentation Dashboard")
st.markdown("Visualizing customer groups based on Recency, Frequency, and Monetary values.")

# --- Load the RFM clustered data ---
@st.cache_data
def load_data():
   return pd.read_csv("output/rfm_results.csv")
st.write("Columns:", df.columns.tolist())


df = load_data()
st.success("✅ Data loaded successfully!")

# --- Dataset preview ---
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

# --- Summary by Segment ---
st.subheader("📊 Average RFM Values per Segment")
summary = df.groupby("Segment")[["Recency", "Frequency", "Monetary", "RFM_Score"]].mean().round(2)
st.dataframe(summary)

# --- Heatmap ---
st.subheader("🌡️ Heatmap of Average RFM Values")
fig, ax = plt.subplots(figsize=(6,4))
sns.heatmap(summary, annot=True, cmap="YlGnBu", fmt=".1f", ax=ax)
st.pyplot(fig)

# --- Scatter Plot ---
st.subheader("💰 Recency vs Monetary by Segment")
fig2, ax2 = plt.subplots(figsize=(8,6))
sns.scatterplot(data=df, x="Recency", y="Monetary", hue="Segment", palette="viridis", s=80)
st.pyplot(fig2)

st.caption("Built with Streamlit · Data: Banking RFM Project · Author: Rugiatu Bah")
