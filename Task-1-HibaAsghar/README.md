# Project 1: Data Cleaning

## Overview
This project performs a full Data Cleaning pipeline
on an e-commerce orders dataset provided by DecodeLabs.
The goal is to prepare raw data for analysis by fixing
missing values, standardizing formats, and validating accuracy.

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
- OpenPyXL

## Cleaning Steps Performed

### CR001 — Missing Values Fix
- Issue: 309 missing values in CouponCode column
- Action: Filled with NO_COUPON
- Impact: Preserved all 309 records

### CR002 — Duplicate Check
- Issue: Checked for duplicate rows and OrderIDs
- Action: Verified uniqueness of all OrderIDs
- Impact: Zero duplicates confirmed

### CR003 — Date Format Standardization
- Issue: Dates not in standard format
- Action: Converted all dates to ISO 8601 YYYY-MM-DD
- Impact: All 1,200 dates now uniform

### CR004 — Text Standardization
- Issue: Inconsistent casing and whitespace in text columns
- Action: Applied Proper Case and stripped whitespace
- Columns Fixed: Product, ShippingAddress, PaymentMethod,
  OrderStatus, CouponCode, ReferralSource

### CR005 — Numeric Precision
- Issue: UnitPrice and TotalPrice had inconsistent decimals
- Action: Rounded to 2 decimal places
- Impact: Consistent numeric formatting

### CR006 — Price Validation
- Issue: Needed to verify TotalPrice accuracy
- Action: Validated TotalPrice = Quantity x UnitPrice
- Impact: Zero pricing errors confirmed

## Final Verification Results
- Duplicate OrderIDs : 0
- Bad Date Formats   : 0
- Missing Values     : 0

## Output Files
- Project1_Final_Output.xlsx
  - Sheet 1: Cleaned_Data
  - Sheet 2: Change_Log

## Project Structure
- clean_Data.py — Full data cleaning Python script
- Dataset_for_Data_Analytics.xlsx — Raw dataset
- Project1_Final_Output.xlsx — Cleaned output file
- README.md — Project documentation
