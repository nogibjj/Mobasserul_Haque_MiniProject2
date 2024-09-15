import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def read_csv_file(file_path):
    return pd.read_csv(file_path)


def summary_statistics(dataframe, output_file):
    """Display summary statistics for numerical columns in the DataFrame."""
    summary = dataframe.describe().transpose()
    summary['median'] = dataframe.median(numeric_only=True)
    summary['range'] = summary['max'] - summary['min']
    summary['variance'] = dataframe.var(numeric_only=True)

    with open(output_file, 'a', encoding='utf-8') as file:
        file.write("### Summary Statistics\n")
        file.write(summary.to_string())
        file.write("\n\n")


def plot_histograms(dataframe, columns, output_file, bins=20):
    """Plot histograms for specified columns in the DataFrame."""
    plt.figure(figsize=(12, 6))
    dataframe[columns].hist(bins=bins, edgecolor='black', figsize=(14, 8))
    plt.suptitle('Distribution of age, annual income, purchase amount, and purchase frequency')
    
    plt.savefig("histograms.png")
    with open(output_file, 'a', encoding='utf-8') as file:
        file.write("![Histograms](histograms.png)\n\n")


def plot_scatter_with_hue(dataframe, x_col, y_col, hue_col, output_file):
    """To visualize the relationship between annual income and purchase amount across different regions."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_col, y=y_col, data=dataframe, hue=hue_col)
    plt.title(f'{x_col} vs. {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    
    plt.savefig("scatter_hue.png")
    with open(output_file, 'a', encoding='utf-8') as file:
        file.write(f"![{x_col} vs {y_col} with Hue](scatter_hue.png)\n\n")


def plot_box_by_category(dataframe, x_col, y_col, output_file):
    """To compare the distribution of loyalty scores across different regions."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=x_col, y=y_col, data=dataframe)
    plt.title(f'{y_col} by {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)

    plt.savefig("box_by_category.png")
    with open(output_file, 'a', encoding='utf-8') as file:
        file.write(f"![{y_col} by {x_col}](box_by_category.png)\n\n")


def plot_correlation_heatmap(dataframe, columns, output_file):
    """To visualize the correlation matrix between purchase amount, purchase frequency, and loyalty score."""
    plt.figure(figsize=(8, 6))
    corr_matrix = dataframe[columns].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')

    plt.savefig("correlation_heatmap.png")
    with open(output_file, 'a', encoding='utf-8') as file:
        file.write("![Correlation Matrix](correlation_heatmap.png)\n\n")


def plot_scatter_with_trend(dataframe, x_col, y_col, output_file):
    """To visualize the relationship between annual income and purchase amount with a trend line."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_col, y=y_col, data=dataframe)
    sns.regplot(x=x_col, y=y_col, data=dataframe, scatter=False, color='red')
    plt.title(f'{x_col} vs. {y_col} with Trend Line')
    plt.xlabel(x_col)
    plt.ylabel(y_col)

    plt.savefig("scatter_with_trend.png")
    with open(output_file, 'a', encoding='utf-8') as file:
        file.write(f"![{x_col} vs {y_col} with Trend](scatter_with_trend.png)\n\n")


def plot_bar_by_category(dataframe, category_col, value_col, output_file):
    """To compare average purchase amounts by region."""
    plt.figure(figsize=(10, 6))
    dataframe.groupby(category_col)[value_col].mean().plot(kind='bar')
    plt.title(f'Average {value_col} by {category_col}')
    plt.xlabel(category_col)
    plt.ylabel(f'Average {value_col}')

    plt.savefig("bar_by_category.png")
    with open(output_file, 'a', encoding='utf-8') as file:
        file.write(f"![Average {value_col} by {category_col}](bar_by_category.png)\n\n")
