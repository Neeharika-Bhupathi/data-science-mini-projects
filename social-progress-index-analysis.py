# Social Progress Index Analysis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset (sample: social_progress_index.csv with Country, Education, Healthcare, Sustainability, SPI_Score)
spi = pd.read_csv('social_progress_index.csv')

# Correlation heatmap
correlation = spi[['Education', 'Healthcare', 'Sustainability', 'SPI_Score']].corr()
plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation between SPI components')
plt.show()

# Top & bottom 10 countries by SPI
top_10 = spi.nlargest(10, 'SPI_Score')
bottom_10 = spi.nsmallest(10, 'SPI_Score')

# Bar chart for top countries
plt.figure(figsize=(8, 5))
sns.barplot(x='SPI_Score', y='Country', data=top_10, palette='viridis')
plt.title('Top 10 Countries by SPI')
plt.tight_layout()
plt.show()
