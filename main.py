import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_csv_file(file_path):
    return pd.read_csv(file_path)

def summary_statistics(dataframe, report_file):
    """Display summary statistics for numerical columns in the DataFrame and save to markdown."""
    summary = dataframe.describe().transpose()
    summary['median'] = dataframe.median(numeric_only=True)
    summary['range'] = summary['max'] - summary['min']
    summary['variance'] = dataframe.var(numeric_only=True)
    
    # Write the summary statistics to the report file
    with open(report_file, 'a') as f:
        f.write("# Summary Statistics\n")
        f.write(summary.to_markdown())
        f.write("\n\n")
    return summary

def save_plot(fig, filename, report_file, title):
    """Save the plot and add it to the report file."""
    fig.savefig(filename)
    with open(report_file, 'a') as f:
        f.write(f"## {title}\n")
        f.write(f"![{title}]({filename})\n\n")

def plot_histograms(dataframe, columns, bins=20, report_file="summary_report.md"):
    """Plot histograms for specified columns in the DataFrame and save to markdown."""
    fig = plt.figure(figsize=(12, 6))
    dataframe[columns].hist(bins=bins, edgecolor='black', figsize=(14, 8))
    plt.suptitle('Distribution of age, annual income, purchase amount, and purchase frequency')
    save_plot(fig, "Histogram_column_distributions.png", report_file, "Histograms")

def plot_scatter_with_hue(dataframe, x_col, y_col, hue_col, report_file="summary_report.md"):
    """To visualize the relationship between annual income and purchase amount across different regions."""
    fig = plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_col, y=y_col, data=dataframe, hue=hue_col)
    plt.title(f'{x_col} vs. {y_col}')
    save_plot(fig, "scatter_plot_hue_by_region.png", report_file, f"{x_col} vs {y_col} by {hue_col}")

def plot_box_by_category(dataframe, x_col, y_col, report_file="summary_report.md"):
    """To compare the distribution of loyalty scores across different regions."""
    fig = plt.figure(figsize=(10, 6))
    sns.boxplot(x=x_col, y=y_col, data=dataframe)
    plt.title(f'{y_col} by {x_col}')
    save_plot(fig, "Loyalty_score_by_region_boxplot.png", report_file, f"{y_col} by {x_col}")

def plot_correlation_heatmap(dataframe, columns, report_file="summary_report.md"):
    """To visualize the correlation matrix between purchase amount, purchase frequency, and loyalty score."""
    fig = plt.figure(figsize=(8, 6))
    corr_matrix = dataframe[columns].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    save_plot(fig, "Correlation_matrix_columns.png", report_file, "Correlation Heatmap")

def plot_scatter_with_trend(dataframe, x_col, y_col, report_file="summary_report.md"):
    """To visualize the relationship between annual income and purchase amount with a trend line."""
    fig = plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_col, y=y_col, data=dataframe)
    sns.regplot(x=x_col, y=y_col, data=dataframe, scatter=False, color='red')
    plt.title(f'{x_col} vs. {y_col} with Trend Line')
    save_plot(fig, "scatter_plot_trend_line.png", report_file, f"{x_col} vs {y_col} with Trend Line")

def plot_bar_by_category(dataframe, category_col, value_col, report_file="summary_report.md"):
    """To compare average purchase amounts by region."""
    fig = plt.figure(figsize=(10, 6))
    dataframe.groupby(category_col)[value_col].mean().plot(kind='bar')
    plt.title(f'Average {value_col} by {category_col}')
    save_plot(fig, "bar_plot_average_purchase_amt_by_regions.png", report_file, f"Average {value_col} by {category_col}")


# Define the report file path
report_file = 'summary_report.md'

# Clear the existing report file content
with open(report_file, 'w') as f:
    f.write("# Summary Report\n\n")

# Reading the CSV file
df = read_csv_file('Customer Purchasing Behaviors.csv')

# Writing summary statistics to the report file
summary_statistics(df, report_file)

# Generating plots and saving them in the report file
plot_histograms(df, ['age', 'annual_income', 'purchase_amount', 'purchase_frequency'], report_file=report_file)
plot_scatter_with_hue(df, 'annual_income', 'purchase_amount', 'region', report_file=report_file)
plot_box_by_category(df, 'region', 'loyalty_score', report_file=report_file)
plot_correlation_heatmap(df, ['purchase_amount', 'purchase_frequency', 'loyalty_score'], report_file=report_file)
plot_scatter_with_trend(df, 'annual_income', 'purchase_amount', report_file=report_file)
plot_bar_by_category(df, 'region', 'purchase_amount', report_file=report_file)
