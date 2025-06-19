# 🎬 Netflix Analytics Dashboard

An interactive, data-rich Streamlit dashboard that visualizes Netflix content trends and quarterly revenue insights from 2017 to 2025. This project transforms raw data into actionable intelligence through dynamic visualizations, genre/language exploration, and KPI storytelling — all hosted live and accessible globally.

🔗 **Live Demo**: [netflix-dashboard-analytics.streamlit.app](https://netflix-dashboard-analytics.streamlit.app/)  
📎 **Portfolio**: [chatty21.github.io/Portfolio](https://chatty21.github.io/Portfolio/)

---

## 📊 Features

✅ **Genre & Language Filters**  
Easily explore Netflix’s growth by filtering top 10 genres and languages via sidebar controls.

📈 **Revenue Over Time**  
Visualize Netflix’s quarterly revenue (2017–2025) and correlate it with content volume and success.

📦 **Content & Media Breakdown**  
Animated race charts and bar graphs to explore release trends by media type, region, and language.

💰 **Revenue Efficiency & KPIs**  
- Revenue per Release (RPR)
- Top 3 Blockbuster Quarters
- Blockbuster Efficiency Flags

🔀 **Advanced Visuals**
- Sankey Diagram: Tracks flow from Genre → Language → Media Type
- Tooltip-enabled Scatter Plots
- Animated Genre Race Chart

📰 **Storytelling Mode**  
Each chart is accompanied by clean narrative summaries to help users quickly grasp the insights.

---

## 📁 Datasets Used

1. **`netflix_simplified_with_quarter_expanded.csv`**  
   Includes Netflix content metadata with genre, type, region, and quarter flags.

2. **`netflix_quarterly_revenue_2017_2025_complete.csv`**  
   Netflix's global revenue broken down by quarter and year.

---

## 🧠 Tech Stack

- **Frontend**: Streamlit (interactive UI)
- **Backend/Data**: Pandas, Numpy
- **Visualization**: Plotly (express + graph_objects), Altair, Streamlit’s built-in elements
- **Deployment**: [Streamlit Cloud](https://streamlit.io/cloud)

---

## 🚀 Run Locally

```bash
# Clone the repository
git clone https://github.com/chatty21/netflix-analytics-dashboard.git
cd netflix-analytics-dashboard

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run netflix_streamlit_dashboard.py
