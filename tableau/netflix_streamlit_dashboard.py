import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

# 💡 Styling + Branding (place this right after set_page_config)
st.markdown(
    """
    <style>
    body {
        background-color: white;
    }
    .main {
        background-color: white;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add Netflix Logo (make sure you have 'netflix_logo.png' in the same folder)
st.image("data:image/png;base64,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", width=250)

# 📌 Title + Article Header
st.title("🎬 Netflix Blockbuster Analytics Dashboard (2017–2025)")

st.markdown("""
## 📢 Netflix Revenue and Content Strategy Report (2017–2025)

This report explores how Netflix’s evolving content catalog—by genre, language, and format—has influenced quarterly revenues across the globe.  
It blends data storytelling with rich visuals to uncover strategic insights from 2017 to 2025.
""")

# 📌 Load Data
@st.cache_data
def load_data():
   df_content = pd.read_csv("tableau/netflix_simplified_with_quarter_expanded.csv")
   df_revenue = pd.read_csv("tableau/netflix_quarterly_revenue_2017_2025_complete.csv")
   return df_content, df_revenue

df_content, df_revenue = load_data()

# 📌 Sidebar Filters
st.sidebar.header("Filter Options")
year_range = st.sidebar.slider("Select Year Range", 2017, 2025, (2017, 2025))

# Unique genres and languages
# Limit to Top 10 most frequent genres
top_10_genres = (
    df_content["genres"]
    .value_counts()
    .head(10)
    .index
    .tolist()
)

available_genres = top_10_genres  # update the multiselect options
available_languages = df_content["language"].dropna().unique().tolist()

selected_genres = st.sidebar.multiselect("Select Genres", sorted(available_genres), default=available_genres[:5])
selected_languages = st.sidebar.multiselect("Select Languages", sorted(available_languages), default=available_languages[:5])

df_filtered = df_content[
    (df_content["release_year"].between(year_range[0], year_range[1])) &
    (df_content["genres"].isin(selected_genres)) &
    (df_content["language"].isin(selected_languages))
]

df_revenue_filtered = df_revenue[df_revenue["Year"].between(year_range[0], year_range[1])]

# =========================
# 📊 1. Media Type Trends
# =========================
st.subheader("Quarterly Netflix Releases by Media Type")
st.markdown("""
### Insight: Content Volume Split by Type  
This visualization shows the volume of **movies** vs. **TV shows** released per quarter.  
Movies consistently account for a larger share of releases, suggesting Netflix’s strategic focus on quick-hit content.  
TV releases remain stable with occasional spikes, which may align with seasonal series drops or global franchises.  
This chart helps assess whether Netflix is shifting its format strategy over time.
""")
media_type_df = df_filtered.groupby(["release_quarter", "media_type"])["title"].count().reset_index(name="count")

fig1 = px.bar(
    media_type_df,
    x="release_quarter",
    y="count",
    color="media_type",
    barmode="stack",
    title="Content Count by Media Type Over Time",
    hover_data={"release_quarter": True, "media_type": True, "count": True}
)
fig1.update_layout(xaxis_tickangle=45, height=450)
st.plotly_chart(fig1, use_container_width=True)

# =========================
# 📊 2. Releases vs Revenue
# =========================
st.subheader("Quarterly Releases vs Revenue Trend")
st.markdown("""
### Insight: Do More Releases Mean More Revenue?  
This dual-axis chart overlays **release count** (bars) with **revenue** (line) across quarters.  
While some revenue spikes align with high release volume (e.g., Q3 2022), others do not—hinting that **quality trumps quantity**.  
Revenue dips during quarters with high output may indicate underperformance or oversaturation.  
This view reveals how content planning impacts financial results over time.
""")
release_df = df_filtered.groupby("release_quarter")["title"].nunique().reset_index(name="release_count")
revenue_df = df_revenue_filtered[["Release_Quarter", "Revenue_Million"]].rename(columns={"Release_Quarter": "release_quarter"})
combined_df = pd.merge(release_df, revenue_df, on="release_quarter", how="left")

fig2 = px.line(
    combined_df,
    x="release_quarter",
    y="Revenue_Million",
    title="Netflix Revenue Trend",
    markers=True,
    labels={"Revenue_Million": "Revenue ($M)"},
    hover_data={"release_quarter": True, "Revenue_Million": True}
)
fig2.add_bar(x=combined_df["release_quarter"], y=combined_df["release_count"], name="Release Count", marker_color="green")

fig2.update_layout(xaxis_tickangle=45, yaxis_title="Revenue / Count", height=500)
st.plotly_chart(fig2, use_container_width=True)

# =========================
# 📊 3. Genre Trends
# =========================
st.subheader("Top Genre Trends by Quarter")
st.markdown("""
### Insight: Genre-Level Popularity Across Time  
This multi-line chart shows how **top 6 genres** evolved in release frequency across quarters.  
Genres like **Drama**, **Comedy**, and **Documentary** remain staples, while **Crime** and **Thriller** show bursty behavior.  
Fluctuations may be tied to real-world events, cultural shifts, or strategic programming.  
Analyzing genre trends helps optimize future content pipeline.
""")
top_genres = df_filtered["genres"].value_counts().nlargest(6).index
df_genre = df_filtered[df_filtered["genres"].isin(top_genres)]

genre_df = df_genre.groupby(["release_quarter", "genres"])["title"].count().reset_index(name="count")

fig3 = px.line(
    genre_df,
    x="release_quarter",
    y="count",
    color="genres",
    markers=True,
    title="Top 6 Genre Trends Over Time",
    hover_data={"release_quarter": True, "genres": True, "count": True}
)
fig3.update_layout(xaxis_tickangle=45, height=500)
st.plotly_chart(fig3, use_container_width=True)

# =========================
# 📊 4. Language Trends
# =========================
st.subheader("Language-Wise Content Trends (Top 6 Languages)")
st.markdown("""
### Insight: Language Diversity in Global Expansion  
Here, we explore how often Netflix releases content in the **top 6 languages** quarter over quarter.  
English leads predictably, but other languages like **Spanish**, **Hindi**, and **Korean** show significant growth.  
This illustrates Netflix’s push into **regional markets** and non-English speaking audiences.  
Language trends help validate localization efforts and demand forecasting.
""")
top_langs = df_filtered["language"].value_counts().nlargest(6).index
df_lang = df_filtered[df_filtered["language"].isin(top_langs)]

lang_df = df_lang.groupby(["release_quarter", "language"])["title"].count().reset_index(name="count")

fig4 = px.line(
    lang_df,
    x="release_quarter",
    y="count",
    color="language",
    markers=True,
    title="Top 6 Language Trends Over Time",
    hover_data={"release_quarter": True, "language": True, "count": True}
)
fig4.update_layout(xaxis_tickangle=45, height=500)
st.plotly_chart(fig4, use_container_width=True)

# =========================
# 📊 5. Popularity Distribution
# =========================
st.subheader(" Popularity Distribution Over Quarters")
st.markdown("""
### Insight: Measuring Audience Engagement  
This line chart shows **average content popularity** per quarter, acting as a proxy for engagement.  
Spikes typically occur around blockbuster launches or viral content waves (e.g., Q2 2022).  
Sudden drops may reflect filler content periods or lack of standout releases.  
This view is vital for assessing content **impact vs. quantity**.
""")
pop_df = df_filtered.groupby("release_quarter")["popularity"].mean().reset_index()

fig5 = px.line(
    pop_df,
    x="release_quarter",
    y="popularity",
    title="Average Popularity Over Time",
    markers=True,
    hover_data={"release_quarter": True, "popularity": True}
)
fig5.update_layout(xaxis_tickangle=45, yaxis_title="Average Popularity", height=500)
st.plotly_chart(fig5, use_container_width=True)

# =========================
# 📊 6. Revenue Efficiency
# =========================
st.subheader("Revenue Efficiency (Revenue per Unique Title)")
st.markdown("""
### Insight: Content ROI Optimization  
Revenue efficiency measures how much revenue each unique title contributes on average.  
High efficiency quarters imply fewer but more impactful releases; low efficiency may reflect **overproduction**.  
This KPI helps identify whether Netflix is investing in **high-quality, high-return** titles.  
A critical metric for guiding future **content budgeting and commissioning**.
""")
eff_df = combined_df.copy()
eff_df["efficiency"] = eff_df["Revenue_Million"] / eff_df["release_count"]

fig6 = px.line(
    eff_df,
    x="release_quarter",
    y="efficiency",
    title="Revenue Efficiency Over Time",
    markers=True,
    hover_data={"release_quarter": True, "efficiency": True}
)
fig6.update_layout(xaxis_tickangle=45, yaxis_title="Revenue / Title", height=500)
st.plotly_chart(fig6, use_container_width=True)

# =========================
# 📌 KPI Metrics Summary
# =========================
st.markdown("### Key Metrics Summary (Filtered)")

st.markdown("""
### Insight: Genre Evolution Year-by-Year  
This animated bar chart shows how the popularity of each genre shifts from 2017 to 2025.  
You can visually spot breakout years for genres like **Thriller**, **Sci-Fi**, or **Crime**.  
It reveals **temporal genre cycles**, which are useful for planning release schedules and marketing campaigns.  
A dynamic storytelling tool to present content strategy to stakeholders.
""")
col1, col2, col3 = st.columns(3)

col1.metric("Total Releases", len(df_filtered))
col2.metric("Top Genre", df_filtered["genres"].value_counts().idxmax() if not df_filtered.empty else "N/A")
col3.metric("Avg Popularity", f"{df_filtered['popularity'].mean():.1f}" if not df_filtered.empty else "N/A")

# =========================
# 📊 Animated Genre Race Over Time
# =========================
st.subheader(" Animated Genre Popularity Over Time")
st.markdown("""
### Insight: Genre Evolution Year-by-Year  
This animated bar chart shows how the popularity of each genre shifts from 2017 to 2025.  
You can visually spot breakout years for genres like **Thriller**, **Sci-Fi**, or **Crime**.  
It reveals **temporal genre cycles**, which are useful for planning release schedules and marketing campaigns.  
A dynamic storytelling tool to present content strategy to stakeholders.
""")
genre_year_df = df_filtered.groupby(["release_year", "genres"])["title"].count().reset_index(name="count")

if not genre_year_df.empty:
    fig_ani = px.bar(
        genre_year_df,
        x="genres",
        y="count",
        color="genres",
        animation_frame="release_year",
        range_y=[0, genre_year_df["count"].max() + 10],
        title="📊 Genre Popularity Evolution (Animated)",
        labels={"count": "Release Count", "genres": "Genre"},
        hover_data={"release_year": True, "count": True, "genres": True}
    )
    fig_ani.update_layout(xaxis_tickangle=45, height=500)
    st.plotly_chart(fig_ani, use_container_width=True)
else:
    st.warning("No data available for animated genre chart with selected filters.")

# =========================
# 🔀 Sankey Chart: Genre → Language → Media Type
# =========================
st.subheader("Content Flow: Genre → Language → Media Type")
st.markdown("""
### Insight: Content Lifecycle Mapping  
This Sankey diagram reveals how content flows from **Genre** → **Language** → **Media Type**.  
For example, **Drama** content is often localized into **Spanish/Korean** and mostly released as **TV Shows**.  
It helps uncover **content structuring patterns** and regional preferences across formats.  
This flow visualization is powerful for guiding **content acquisition, localization, and production strategy**.
""")
sankey_df = df_filtered.groupby(["genres", "language", "media_type"]).size().reset_index(name="count")

if not sankey_df.empty:
    # Prepare node list and mapping
    all_nodes = pd.Series(
        pd.concat([sankey_df["genres"], sankey_df["language"], sankey_df["media_type"]])
        .unique()
    ).reset_index(drop=True)
    node_map = {k: v for v, k in all_nodes.items()}

    # Genre → Language links
    sankey_links_1 = pd.DataFrame({
        "source": sankey_df["genres"].map(node_map),
        "target": sankey_df["language"].map(node_map),
        "value": sankey_df["count"]
    })

    # Language → Media Type links
    sankey_links_2 = pd.DataFrame({
        "source": sankey_df["language"].map(node_map),
        "target": sankey_df["media_type"].map(node_map),
        "value": sankey_df["count"]
    })

    sankey_links = pd.concat([sankey_links_1, sankey_links_2], ignore_index=True)

    # Create Sankey diagram
    fig_sankey = go.Figure(data=[go.Sankey(
        node=dict(
            label=all_nodes.tolist(),
            pad=15,
            thickness=15
        ),
        link=dict(
            source=sankey_links["source"],
            target=sankey_links["target"],
            value=sankey_links["value"]
        )
    )])

    fig_sankey.update_layout(
        title_text=" Genre → Language → Media Type Flow",
        font_size=10,
        height=600
    )
    st.plotly_chart(fig_sankey, use_container_width=True)
else:
    st.warning("Not enough data to display the Sankey flow diagram.")

# =========================
# 📌 Footer
# =========================
st.markdown("""---""")
st.markdown(
    "<center> Built by Chaitanya Patil |  Powered by Streamlit + Plotly | Last Updated: June 2025</center>",
    unsafe_allow_html=True,
)
