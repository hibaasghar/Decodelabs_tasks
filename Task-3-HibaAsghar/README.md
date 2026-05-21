# Project 3: SQL Data Analysis

## Overview
This project uses SQL queries to extract business insights
from an e-commerce orders dataset provided by DecodeLabs.
The goal is to filter, group, and aggregate raw data into
actionable business intelligence.

## Dataset
- File: Dataset_for_Data_Analytics.xlsx
- Rows: 1,200 orders
- Columns: OrderID, Date, CustomerID, Product, Quantity,
  UnitPrice, PaymentMethod, OrderStatus, ReferralSource,
  CouponCode, TotalPrice

## Tools Used
- MySQL Workbench
- MySQL 8.0

## Queries Covered
1. View all data
2. Select specific columns
3. Filter delivered orders
4. Filter high value orders above 2000
5. Orders that used a coupon
6. Instagram orders paid by Credit Card
7. Count orders by status
8. Revenue by product
9. Orders by payment method
10. Revenue by referral source
11. Cancelled and returned orders per product
12. Top 5 highest revenue orders
13. Average order value by coupon code
14. Products with average revenue above 1000
15. Referral sources with more than 20 orders
16. Full summary dashboard

## Key Insights
- Laptops and Tablets generated the highest total revenue
- Instagram was the top referral source for orders
- Credit Card was the most used payment method
- Delivered orders had the highest average order value

## SQL Concepts Used
- SELECT statements
- WHERE clause for filtering
- GROUP BY for grouping
- ORDER BY for sorting
- COUNT, SUM, AVG aggregations
- HAVING clause for group filtering

## Project Structure
- project3_sql_analysis.sql — All 16 SQL queries
- Dataset_for_Data_Analytics.xlsx — Raw dataset
- README.md — Project documentation
