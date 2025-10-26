# Superstore Sales Data Analysis (Python Project)
# Overview

This project performs exploratory data analysis (EDA) on the Sample Superstore dataset using Python.
The goal is to uncover insights related to sales, profit trends, and customer segments through visual analysis.

# Tools & Libraries

Python

Pandas – data cleaning & transformation

NumPy – numerical operations

Matplotlib – visualization

# Dataset

File: Sample - Superstore.csv
The dataset includes information about orders, shipping, products, customers, and regions such as:

Order Date, Ship Date

Category, Sub-Category

Sales, Profit

Customer Segment, Region

# Data Preparation

Loaded the dataset using Pandas

Checked structure & data types (df.info(), df.describe())

Converted date columns to datetime format

Extracted new time-based features:
Order Month
Order Year
Order Day of Week

# Analysis Performed
1. Monthly Sales Trend

Line plot showing how total sales vary by month.

2. Sales by Category

Pie chart visualizing the distribution of sales across product categories.

3. Sales by Sub-Category

Bar chart highlighting which product sub-categories generate the most sales.

4. Monthly Profit Trend

Line plot showing profit fluctuations month by month.

5. Profit by Category

Pie chart comparing total profit across categories.

6. Profit by Sub-Category

Bar chart revealing which sub-categories contribute most to profit.

7. Sales & Profit by Customer Segment

Grouped bar chart comparing sales vs. profit for each customer segment.

8. Sales-to-Profit Ratio

Calculated and displayed ratio of total sales to total profit per segment.

# Visualizations

All visualizations are created using Matplotlib, providing clear and informative insights about:

Seasonal performance

Category-wise contributions

Profitability patterns

Segment-level efficiency

# Key Insights

Certain months show strong sales peaks (likely festive or seasonal).

Technology category often drives higher profit margins.

Some sub-categories have high sales but low profits, indicating cost inefficiencies.

Consumer segment contributes the most to sales volume.

# Conclusion

This project demonstrates how to use Python for data analysis — cleaning, transforming, and visualizing data to generate business insights.
