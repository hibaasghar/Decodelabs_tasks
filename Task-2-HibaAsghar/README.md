# Project 2: Exploratory Data Analysis (EDA)

## Overview
This project performs a full Exploratory Data Analysis
on an e-commerce orders dataset provided by DecodeLabs.
The goal is to uncover patterns, trends, and business
insights using Python.

## Dataset
- File: Dataset_for_Data_Analytics.xlsx
- Rows: 1,200 orders
- Columns: OrderID, Date, CustomerID, Product, Quantity,
  UnitPrice, PaymentMethod, OrderStatus, ReferralSource,
  CouponCode, TotalPrice

## Tools Used
- Python 3
- Pandas
- NumPy

## Steps Covered
1. Data Loading and Inspection
2. Missing Values Analysis
3. Descriptive Statistics
4. Outlier Detection IQR Method
5. Product Performance Analysis
6. Order Status Distribution
7. Payment Method Analysis
8. Referral Source Analysis
9. Coupon Code Analysis
10. Monthly Revenue Trend
11. Correlation Analysis
12. Executive Summary

## Key Insights
- Total Revenue: $735,000+
- Instagram is the #1 revenue channel ($275K+)
- Only 29% of orders are successfully Delivered
- 41.4% of orders are Cancelled or Returned
- Chair and Printer lead in total revenue ($195,000+)
- Unit Price is the strongest predictor of order value (r=0.72)
- 8 high-value outlier orders detected ($3,334 to $3,456)

## Recommendations
- Investigate root cause of 41.4% Cancelled/Returned orders
- Launch referral incentive program (lowest revenue channel)
- Promote high-price products to boost avg order value
- Replicate peak-month Jun 2024 marketing conditions year-round

## Project Structure
- eda_project2.py — Full EDA Python script
- Dataset_for_Data_Analytics.xlsx — Raw dataset
- README.md — Project documentation
