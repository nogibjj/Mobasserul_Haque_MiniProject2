import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Customer Purchasing Behaviors.csv')

def plot_histograms(dataframe, columns, bins=20):
    """Plot histograms for specified columns in the DataFrame."""
    plt.figure(figsize=(12, 6))
    dataframe[columns].hist(bins=bins, edgecolor='black', figsize=(14, 8))
    plt.suptitle('distribution of age, annual income, purchase amount, and purchase frequency')
    plt.show()

def plot_scatter_with_hue(dataframe, x_col, y_col, hue_col):
    """Plot a scatter plot with color hue for different categories."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_col, y=y_col, data=dataframe, hue=hue_col)
    plt.title(f'{x_col} vs. {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

plot_histograms(df, ['age', 'annual_income', 'purchase_amount', 'purchase_frequency'])
plot_scatter_with_hue(df, 'annual_income', 'purchase_amount', 'region')