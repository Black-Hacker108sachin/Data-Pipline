import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    "Name": ["Sachin", "Pratik", "Chirag", "Vikas", "Shubham"],
    "Age": [25, 30, 35, 40, 28],
    "Salary": [50000, 60000, 70000, 80000, 55000]
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Line plot for Age vs Salary
def line_plot():
    plt.figure(figsize=(8, 5))
    plt.plot(df["Name"], df["Salary"], marker='o', color="blue", label="Salary")
    plt.title("Salary by Name", fontsize=14)
    plt.xlabel("Name", fontsize=12)
    plt.ylabel("Salary", fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

# Bar plot for Age vs Salary
def bar_plot():
    plt.figure(figsize=(8, 5))
    sns.barplot(x="Name", y="Salary", data=df, palette="viridis")
    plt.title("Salary Distribution by Name", fontsize=14)
    plt.xlabel("Name", fontsize=12)
    plt.ylabel("Salary", fontsize=12)
    plt.show()

# Scatter plot for Age vs Salary
def scatter_plot():
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x="Age", y="Salary", data=df, hue="Name", palette="deep", s=100)
    plt.title("Age vs Salary", fontsize=14)
    plt.xlabel("Age", fontsize=12)
    plt.ylabel("Salary", fontsize=12)
    plt.grid(True)
    plt.show()

# Execute visualizations
if __name__ == "__main__":
    print("Line Plot:")
    line_plot()

    print("Bar Plot:")
    bar_plot()

    print("Scatter Plot:")
    scatter_plot()
