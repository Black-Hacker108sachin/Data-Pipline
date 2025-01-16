import pandas as pd


# Sample data: Create a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [25, "30 ", "22", "27", None],
    "City": ["New York", "San Francisco", "Los Angeles", None, "Miami"],
    "Salary": ["50000", "60000 ", None, "70000", "80000"]
}
df = pd.DataFrame(data)

# Step 1: Clean data
# Strip whitespace from string columns
df['Age'] = df['Age'].astype(str).str.strip()
df['Salary'] = df['Salary'].astype(str).str.strip()

# Convert columns to appropriate data types
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # Convert to numeric, replacing invalid values with NaN
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')  # Convert to numeric, replacing invalid values with NaN

# Fill missing values
df['City'] = df['City'].fillna("Unknown")  # Replace missing city with "Unknown"
df['Age'] = df['Age'].fillna(df['Age'].mean())  # Replace missing age with the average age
df['Salary'] = df['Salary'].fillna(df['Salary'].median())  # Replace missing salary with the median

# Step 2: Transform data
# Add a new column for age groups
df['Age Group'] = pd.cut(df['Age'], bins=[0, 25, 35, 50], labels=['Youth', 'Adult', 'Mid-age'])

# Format salary column to display with a dollar sign
df['Salary'] = df['Salary'].apply(lambda x: f"${x:,.2f}")

# Print the cleaned and transformed DataFrame
print("Cleaned and Transformed Data:")
print(df)
