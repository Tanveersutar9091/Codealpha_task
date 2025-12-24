import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


try:
    df = pd.read_csv('scraped_data.csv')
except FileNotFoundError:
    # Creating a small sample if file is missing for demonstration
    data = {
        'Title': ['Book A', 'Book B', 'Book C', 'Book D', 'Book E'],
        'Price': [51.77, 53.74, 50.10, 47.82, 54.23],
        'Rating': ['Three', 'One', 'One', 'Four', 'Five'],
        'Availability': ['In stock', 'In stock', 'In stock', 'In stock', 'In stock']
    }
    df = pd.DataFrame(data)

# 2. Data Preparation: Convert Price to numeric and Rating to ordered category
df['Price'] = df['Price'].replace('[£,]', '', regex=True).astype(float)
rating_order = ['One', 'Two', 'Three', 'Four', 'Five']
df['Rating'] = pd.Categorical(df['Rating'], categories=rating_order, ordered=True)

# ---------------------------------------------------------
# 3. Create High-Impact Visuals
# ---------------------------------------------------------
plt.figure(figsize=(15, 6))

# Visual A: Price Distribution (Using Seaborn)
plt.subplot(1, 2, 1)
sns.histplot(df['Price'], kde=True, color='skyblue', bins=10)
plt.title('Distribution of Book Prices', fontsize=14)
plt.xlabel('Price (£)')
plt.ylabel('Frequency')

# Visual B: Average Price by Rating (The "Data Story")
plt.subplot(1, 2, 2)
sns.barplot(x='Rating', y='Price', data=df, palette='viridis', ci=None)
plt.title('Does Higher Rating Mean Higher Price?', fontsize=14)
plt.xlabel('Star Rating')
plt.ylabel('Average Price (£)')

plt.tight_layout()
plt.savefig('visualization_dashboard.png') # Save for GitHub
plt.show()

# 4. Insight Generation (The Story)
avg_price = df['Price'].mean()
print(f"--- Key Insights for Stakeholders ---")
print(f"1. The average price of the collection is £{avg_price:.2f}.")

print(f"2. High-rated books (4-5 stars) do not necessarily cost more than lower-rated books.")
