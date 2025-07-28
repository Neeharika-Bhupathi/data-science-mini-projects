# Covid-19 Data Analysis & Tableau Preprocessing
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (sample: covid19_india.csv with Date, State, Confirmed, Recovered, Deaths)
df = pd.read_csv('covid19_india.csv')

# Convert date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Aggregate by date for overall trend
daily = df.groupby('Date')[['Confirmed', 'Recovered', 'Deaths']].sum().reset_index()

# Plot trends
plt.figure(figsize=(10, 5))
plt.plot(daily['Date'], daily['Confirmed'], label='Confirmed', color='blue')
plt.plot(daily['Date'], daily['Recovered'], label='Recovered', color='green')
plt.plot(daily['Date'], daily['Deaths'], label='Deaths', color='red')
plt.title('Covid-19 Trend in India')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.legend()
plt.tight_layout()
plt.show()

# Save cleaned data for Tableau
daily.to_csv('covid_processed.csv', index=False)
print("Processed data saved to covid_processed.csv")
