# Pandas Descriptive Script Mini Project
[![CI](https://github.com/nogibjj/Mobasserul_Haque_MiniProject2/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Mobasserul_Haque_MiniProject2/actions/workflows/cicd.yml)

This project performs exploratory data analysis (EDA) on a dataset containing customer purchasing behavior, providing insights into various patterns and relationships using pandas, Matplotlib, and Seaborn.

## Table of Contents
- [Overview](#overview)
- [Source](#source)
- [About Dataset](#about-dataset)
  - [Dataset Columns](#dataset-columns)
- [Features](#features)
- [Data Visualization](#data-visualization)
- [Setup](#setup)
  - [Development Environment (Dev Container)](#development-environment-dev-container)
  - [Makefile](#makefile)
  - [GitHub Actions](#github-actions)
- [Usage](#usage)
  - [Summary Statistics](#summary-statistics)
  - [Histograms](#histograms)
  - [Scatter Plot with Hue](#scatter-plot-with-hue)
  - [Box Plot by Category](#box-plot-by-category)
  - [Correlation Heatmap](#correlation-heatmap)
  - [Scatter Plot with Trend Line](#scatter-plot-with-trend-line)
  - [Bar Plot by Category](#bar-plot-by-category)
- [Running Tests](#running-tests)
- [Dependencies](#dependencies)
- [License](#license)

## Overview
This project focuses on analyzing customer purchasing behavior using a dataset in CSV format. It generates various statistical summaries and visualizations to help understand trends, relationships, and distributions in the data.

## Source
The dataset used in this project is **Customer Purchasing Behaviors**, which can be found on Kaggle:  
[Customer Purchasing Behaviors Dataset](https://www.kaggle.com/datasets/hanaksoy/customer-purchasing-behaviors)

## About Dataset

### Dataset Columns
- **customer_id**: Unique ID of the customer.
- **age**: The age of the customer.
- **annual_income**: The customer's annual income (in USD).
- **purchase_amount**: The total amount of purchases made by the customer (in USD).
- **purchase_frequency**: Frequency of customer purchases (number of times per year).
- **region**: The region where the customer lives (North, South, East, West).
- **loyalty_score**: Customer's loyalty score (a value between 0-100).

This dataset includes information on customer profiles and their purchasing behaviors. The data features columns for user ID, age, annual income, purchase amount, loyalty score, region, and purchase frequency. It is intended for analyzing customer segmentation and loyalty trends, and can be used for various machine learning and data analysis tasks related to customer behavior and market research.

## Features
- Display summary statistics, including median, range, and variance.
- Visualize data distributions with histograms.
- Plot scatter plots with categories (hue).
- Compare distributions across categories using box plots.
- Analyze correlations between numerical variables with a heatmap.
- Create scatter plots with trend lines for relationship analysis.
- Generate bar plots comparing categorical data.

## Data Visualization

Below are sample visualizations produced by the project:

- **Distribution of Columns:**
  ![Visualization](Histogram_column_distributions.png)

- **Loyalty Score by Region:**
  ![Visualization](Loyalty_score_by_region_boxplot.png)

- **Scatter Plot with Hue (Region):**
  ![Visualization](scatter_plot_hue_by_region.png)

- **Scatter Plot with Trend Line:**
  ![Visualization](scatter_plot_trend_line.png)

- **Correlation Matrix:**
  ![Visualization](Correlation_matrix_columns.png)

- **Bar Plot of Average Purchase Amount by Region:**
  ![Visualization](bar_plot_average_purchase_amt_by_regions.png)

## Setup

### Development Environment (Dev Container)
This project includes a development container setup, enabling you to develop in a fully configured environment. The container is based on the official Python image and installs all necessary dependencies.

To use the development container, ensure you have Docker installed and a supported code editor like VSCode. The editor will prompt you to "Reopen in Container" when the project is loaded.

### Makefile
The repository includes a `Makefile` to simplify the setup and execution of key commands.

- Install dependencies:
    ```bash
    make install
    ```

- Run linting checks using `pylint`:
    ```bash
    make lint
    ```

- Run tests:
    ```bash
    make test
    ```

- Clean up the environment:
    ```bash
    make clean
    ```

### GitHub Actions
This repository is equipped with GitHub Actions for continuous integration (CI). The workflow runs linting and testing automatically upon each push or pull request.

To view the status of the CI pipeline, navigate to the **Actions** tab of your repository on GitHub.

## Usage

### Summary Statistics
The `summary_statistics` function displays key metrics like the median, range, and variance for each numerical column.

```python
summary_statistics(df)
