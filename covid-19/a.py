import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
covid_df = pd.read_csv("covid_19_clean_complete.csv")
# Convert Date column to datetime
covid_df["Date"] = pd.to_datetime(covid_df["Date"])
# Check for missing values
print("\nMissing Values in COVID-19 Dataset:")
print(covid_df.isnull().sum())
# Summary statistics
print("\nCOVID-19 Summary Statistics:")
print(covid_df.describe())
# Group by Date to get global trends
covid_trend = covid_df.groupby("Date")[["Confirmed", "Deaths", "Recovered", "Active"]].sum()
# Plot COVID-19 Trends
plt.figure(figsize=(12, 6))
sns.lineplot(data=covid_trend, linewidth=2.0)
plt.title("Global COVID-19 Cases Over Time", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.legend(["Confirmed", "Deaths", "Recovered", "Active"])
plt.xticks(rotation=45)
plt.grid()
plt.show()