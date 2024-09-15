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

plot_histograms(df, ['age', 'annual_income', 'purchase_amount', 'purchase_frequency'])