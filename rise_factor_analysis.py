import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------- STEP 1: Load Data --------------------
df = pd.read_csv("top_insta_influencers_data.csv")
print("Initial Data Loaded:")
print(df.head())

# -------------------- STEP 2: Data Cleaning --------------------
replace_dict = {'k': 'e3', 'm': 'e6', 'b': 'e9', '%': ''}

columns_to_clean = [
    'posts', 'followers', 'avg_likes',
    '60_day_eng_rate', 'new_post_avg_like', 'total_likes'
]

# Replace and convert to float
df[columns_to_clean] = df[columns_to_clean].replace(replace_dict, regex=True).astype(float)

# Drop missing values
df.dropna(subset=columns_to_clean + ['influence_score'], inplace=True)

# -------------------- STEP 3: Feature Engineering --------------------
# Compute engagement rate (as %), growth in likes
df['growth_factor'] = df['new_post_avg_like'] / df['avg_likes']
df['like_follower_ratio'] = df['avg_likes'] / df['followers']

# Classification Rules:
# 1. If growth_factor > 1.1 and engagement > 1.5 → Rising
# 2. If growth_factor < 0.9 and engagement < 1.0 → Declining
# 3. Else → Stable

def classify_trend(row):
    if row['growth_factor'] > 1.1 and row['60_day_eng_rate'] > 1.5:
        return 'Rising 📈'
    elif row['growth_factor'] < 0.9 and row['60_day_eng_rate'] < 1.0:
        return 'Declining 📉'
    else:
        return 'Stable 🟰'

df['trend'] = df.apply(classify_trend, axis=1)

# -------------------- STEP 4: Show Summary --------------------
print("\nTrend Classification Summary:")
print(df['trend'].value_counts())

# Top examples from each category
for label in ['Rising 📈', 'Stable 🟰', 'Declining 📉']:
    print(f"\nTop 3 influencers classified as {label}:")
    print(df[df['trend'] == label][['channel_info', 'followers', 'avg_likes', 'new_post_avg_like', '60_day_eng_rate', 'trend']].head(3))

# -------------------- STEP 5: Visualizations --------------------

# Pie chart of distribution
plt.figure(figsize=(6, 6))
df['trend'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FFC107', '#F44336'])
plt.title("Influencer Trend Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# Scatter Plot: Growth vs Engagement
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='growth_factor', y='60_day_eng_rate', hue='trend', palette='Set1')
plt.title("Growth Factor vs 60-Day Engagement Rate")
plt.xlabel("Growth Factor (New Likes / Avg Likes)")
plt.ylabel("60-Day Engagement Rate (%)")
plt.axhline(1.5, linestyle='--', color='gray')
plt.axvline(1.1, linestyle='--', color='gray')
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------- STEP 6: Save Output --------------------
df.to_csv("influencer_trend_classification.csv", index=False)
print("Saved results to influencer_trend_classification.csv ✅")
