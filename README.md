# 📈 The Rise Factor: Discovering Emerging & Declining Instagram Influencers

> A data analytics project that classifies top Instagram influencers into **Rising**, **Stable**, or **Declining** categories based on recent post performance and engagement trends.

---

## 🔍 Overview

This project analyzes a cleaned dataset of the top 100 Instagram influencers to detect their **current performance trend** using Python and visualizes key insights with Tableau.

We answer:  
- Who are the fastest-rising influencers today?  
- Which influencers are stable, and which are in decline?  
- How do growth and engagement metrics interact?

---

## 📂 Dataset

**Source**: Provided pre-cleaned dataset  
**File**: `top_insta_influencers_data.csv`  
Contains influencer handles, follower counts, average likes, engagement rate, and country.

---

## ⚙️ Technologies Used

- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **Tableau** (for interactive dashboard)
- **VS Code / .py script**

---

## 📊 Key Metrics & Features

| Feature              | Description                                         |
|----------------------|-----------------------------------------------------|
| `growth_factor`      | Ratio of recent post likes to overall avg likes     |
| `like_follower_ratio`| Average likes divided by followers                  |
| `60_day_eng_rate`    | Engagement rate over the past 60 days (%)           |
| `trend`              | Final classification: 📈 Rising, 🟰 Stable, 📉 Declining |

---

## 🧠 Trend Classification Logic

```python
if growth_factor > 1.1 and engagement > 1.5:
    trend = 'Rising 📈'
elif growth_factor < 0.9 and engagement < 1.0:
    trend = 'Declining 📉'
else:
    trend = 'Stable 🟰'
```
## 📈 Visualizations (in Tableau)

Bar Chart: Top 10 influencers by follower count (per trend)

Scatter Plot: Growth factor vs Engagement Rate

Data Table: Filterable view by trend, country, and followers

Map View: Influencer spread by country

## 💡 Key Insights
- Influencers with low follower counts but high engagement often outperform mega-celebrities in ROI potential.

- A high growth factor signals emerging content trends and rising star potential.

- Tableau dashboards allow dynamic filtering and easy insight discovery for brands or marketers.

---

## Acknowledgements
- Dataset inspired by influencer marketing trend analysis

- Built with love using Python & Tableau 

- Created by Pratyaksha Joshi
