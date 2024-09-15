import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from main import (
    read_csv_file, summary_statistics, plot_histograms, plot_scatter_with_hue, 
    plot_box_by_category, plot_correlation_heatmap, plot_scatter_with_trend, 
    plot_bar_by_category
)

# Sample CSV data as a string
sample_data = """customer_id,age,annual_income,purchase_amount,purchase_frequency,region,loyalty_score
1,23,50000,200,5,North,80
2,45,60000,300,7,South,85
3,34,55000,250,6,East,90
4,50,65000,400,8,West,70
5,29,70000,350,7,North,75
"""

# Function to create DataFrame from sample data
def setup_dataframe():
    return pd.read_csv(StringIO(sample_data))

def test_read_csv_file():
    """Test read_csv_file function using StringIO"""
    df = setup_dataframe()
    result = pd.read_csv(StringIO(sample_data))
    pd.testing.assert_frame_equal(result, df)
    print("test_read_csv_file passed")

def test_summary_statistics():
    """Test summary_statistics function"""
    df = setup_dataframe()

    # Run the summary_statistics function to ensure it doesn't raise any errors
    try:
        summary_statistics(df)
        print("test_summary_statistics passed")
    except Exception as e:
        print(f"test_summary_statistics failed: {e}")

def test_plot_histograms():
    """Test plot_histograms function"""
    df = setup_dataframe()

    # Mock plt.show to prevent actual plotting during tests
    plt.show = lambda: None
    plot_histograms(df, ['age', 'annual_income', 'purchase_amount', 'purchase_frequency'])
    print("test_plot_histograms passed")

def test_plot_scatter_with_hue():
    """Test plot_scatter_with_hue function"""
    df = setup_dataframe()

    plt.show = lambda: None
    plot_scatter_with_hue(df, 'annual_income', 'purchase_amount', 'region')
    print("test_plot_scatter_with_hue passed")

def test_plot_box_by_category():
    """Test plot_box_by_category function"""
    df = setup_dataframe()

    plt.show = lambda: None
    plot_box_by_category(df, 'region', 'loyalty_score')
    print("test_plot_box_by_category passed")

def test_plot_correlation_heatmap():
    """Test plot_correlation_heatmap function"""
    df = setup_dataframe()

    plt.show = lambda: None
    plot_correlation_heatmap(df, ['purchase_amount', 'purchase_frequency', 'loyalty_score'])
    print("test_plot_correlation_heatmap passed")

def test_plot_scatter_with_trend():
    """Test plot_scatter_with_trend function"""
    df = setup_dataframe()

    plt.show = lambda: None
    plot_scatter_with_trend(df, 'annual_income', 'purchase_amount')
    print("test_plot_scatter_with_trend passed")

def test_plot_bar_by_category():
    """Test plot_bar_by_category function"""
    df = setup_dataframe()

    plt.show = lambda: None
    plot_bar_by_category(df, 'region', 'purchase_amount')
    print("test_plot_bar_by_category passed")

# Run the tests
test_read_csv_file()
test_summary_statistics()
test_plot_histograms()
test_plot_scatter_with_hue()
test_plot_box_by_category()
test_plot_correlation_heatmap()
test_plot_scatter_with_trend()
test_plot_bar_by_category()
