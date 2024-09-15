import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_csv_file(file_path):
    return pd.read_csv(file_path)

def summary_statistics(dataframe):
    """Display summary statistics for numerical columns in the DataFrame."""
    summary = dataframe.describe().transpose()
    summary['median'] = dataframe.median(numeric_only=True)
    summary['range'] = summary['max'] - summary['min']
    summary['variance'] = dataframe.var(numeric_only=True)
    print("Summary Statistics:")
    print(summary)
    

def plot_histograms(dataframe, columns, bins=20):
    """Plot histograms for specified columns in the DataFrame."""
    plt.figure(figsize=(12, 6))
    dataframe[columns].hist(bins=bins, edgecolor='black', figsize=(14, 8))
    plt.suptitle('distribution of age, annual income, purchase amount, and purchase frequency')
    plt.show()

def plot_scatter_with_hue(dataframe, x_col, y_col, hue_col):
    """To visualize the relationship between annual income and purchase amount across different regions."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_col, y=y_col, data=dataframe, hue=hue_col)
    plt.title(f'{x_col} vs. {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

def plot_box_by_category(dataframe, x_col, y_col):
    """To compare the distribution of loyalty scores across different regions."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=x_col, y=y_col, data=dataframe)
    plt.title(f'{y_col} by {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()
    
def plot_correlation_heatmap(dataframe, columns):
    """To visualize the correlation matrix between purchase amount, purchase frequency, and loyalty score."""
    plt.figure(figsize=(8, 6))
    corr_matrix = dataframe[columns].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

def plot_scatter_with_trend(dataframe, x_col, y_col):
    """To visualize the relationship between annual income and purchase amount with a trend line."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_col, y=y_col, data=dataframe)
    sns.regplot(x=x_col, y=y_col, data=dataframe, scatter=False, color='red')
    plt.title(f'{x_col} vs. {y_col} with Trend Line')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

def plot_bar_by_category(dataframe, category_col, value_col):
    """To compare average purchase amounts by region."""
    plt.figure(figsize=(10, 6))
    dataframe.groupby(category_col)[value_col].mean().plot(kind='bar')
    plt.title(f'Average {value_col} by {category_col}')
    plt.xlabel(category_col)
    plt.ylabel(f'Average {value_col}')
    plt.show()


df = read_csv_file('Customer Purchasing Behaviors.csv')
summary_statistics(df)

plot_histograms(df, ['age', 'annual_income', 'purchase_amount', 'purchase_frequency'])
plot_scatter_with_hue(df, 'annual_income', 'purchase_amount', 'region')
plot_box_by_category(df, 'region', 'loyalty_score')
plot_correlation_heatmap(df, ['purchase_amount', 'purchase_frequency', 'loyalty_score'])
plot_scatter_with_trend(df, 'annual_income', 'purchase_amount')
plot_bar_by_category(df, 'region', 'purchase_amount')