import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("weather_data.csv")

# Print city count to check if multiple cities are present
print(df["City"].value_counts())  # ADD THIS LINE HERE

# Remove duplicate city names
df = df.drop_duplicates(subset=["City"])

# Print the data to check if it's loaded correctly
print(df)

# Plot the temperature vs. city bar chart
plt.figure(figsize=(8, 5))
sns.barplot(x="City", y="Temperature (°C)", data=df, hue="City", palette="coolwarm", alpha=1)


# Customize the plot
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.title("Temperature in Different Cities")
plt.xticks(rotation=45)
plt.show()

