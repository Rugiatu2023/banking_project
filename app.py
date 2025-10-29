import streamlit as st
import pandas as pd
import plotly.express as px

# ================================
# PAGE CONFIG
# ================================
st.set_page_config(page_title="Banking RFM Dashboard", layout="wide")
st.title("🏦 Banking Customer Segmentation Dashboard")
st.markdown("Analyze customer segments based on Recency, Frequency, and Monetary (RFM) values.")

# ================================
# LOAD DATA
# ================================
df = pd.DataFrame({
    'CustomerID': range(1, 21),
    'Recency': [10, 20, 30, 40, 25, 35, 15, 45, 5, 50, 23, 12, 18, 33, 48, 28, 8, 38, 42, 22],
    'Frequency': [5, 3, 6, 2, 8, 4, 7, 3, 9, 2, 5, 6, 7, 4, 2, 5, 9, 3, 2, 6],
    'Monetary': [500, 300, 650, 200, 900, 450, 700, 250, 950, 180, 520, 600, 680, 400, 220, 550, 980, 290, 240, 610],
    'RFM_Score': [7, 6, 8, 5, 9, 7, 8, 6, 9, 5, 7, 8, 8, 6, 5, 7, 9, 6, 5, 8],
    'RFM_Segment': ['Gold', 'Silver', 'Gold', 'Bronze', 'Platinum', 'Silver', 'Gold', 'Silver', 'Platinum', 'Bronze',
                    'Gold', 'Gold', 'Gold', 'Silver', 'Bronze', 'Gold', 'Platinum', 'Silver', 'Bronze', 'Gold']
})

# ================================
# TAB SETUP
# ================================
tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Visualizations", "💡 Customer Insights"])

# ================================
# TAB 1: OVERVIEW
# ================================
with tab1:
    st.subheader("📊 Overview of RFM Data")
    st.dataframe(df)

    st.write("#### Summary Statistics")
    st.write(df.describe())

# ================================
# TAB 2: VISUALIZATIONS
# ================================
with tab2:
    st.subheader("📈 RFM Visualizations")

    fig_scatter = px.scatter(
        df,
        x='Frequency',
        y='Monetary',
        color='RFM_Segment',
        hover_data=['CustomerID', 'RFM_Score'],
        title="Frequency vs Monetary (Interactive)",
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig_scatter.update_layout(
        legend_title_text='RFM Segment',
        legend=dict(itemsizing='constant', title_font=dict(size=12))
    )

    st.plotly_chart(fig_scatter, use_container_width=True)

# ================================
# TAB 3: CUSTOMER INSIGHTS
# ================================
with tab3:
    st.markdown("---")
    st.subheader("💡 Customer Insights")

    colA, colB, colC = st.columns(3)

    with colA:
        st.write("### 💰 Top 10 Highest Spenders")
        top_spenders = df.nlargest(10, 'Monetary')[['CustomerID', 'Monetary', 'RFM_Segment']]
        st.dataframe(top_spenders)

    with colB:
        st.write("### 🔁 Most Frequent Buyers")
        most_frequent = df.nlargest(10, 'Frequency')[['CustomerID', 'Frequency', 'RFM_Segment']]
        st.dataframe(most_frequent)

    with colC:
        st.write("### ⏳ Least Recent Customers")
        least_recent = df.nlargest(10, 'Recency')[['CustomerID', 'Recency', 'RFM_Segment']]
        st.dataframe(least_recent)
