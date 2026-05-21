
#  DecodeLabs – Project 2: Exploratory Data Analysis (EDA)

import pandas as pd
import numpy as np

# STEP 1 – LOAD & INSPECT THE DATA

df = pd.read_excel(r"C:\Users\Lenovo\Downloads\Dataset for Data Analytics.xlsx")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")
df["Year"]  = df["Date"].dt.year


print("STEP 1 – DATASET OVERVIEW")

print(f"Shape          : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Date range     : {df['Date'].min().date()} → {df['Date'].max().date()}")
print(f"\nColumn names   : {list(df.columns)}")
print("\nData types:")
print(df.dtypes.to_string())

# STEP 2 

print("STEP 2 – MISSING VALUES")

missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_df = pd.DataFrame({"Missing Count": missing, "Missing %": missing_pct})
missing_df = missing_df[missing_df["Missing Count"] > 0]
print(missing_df.to_string())
print("\n→ Only 'CouponCode' has 309 missing values (25.75%).")
print("  These are valid: customers who used no coupon.")
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# STEP 3 

print("STEP 3 – DESCRIPTIVE STATISTICS (Numeric Columns)")

num_cols = ["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]
stats = df[num_cols].agg(["count", "mean", "median", "std", "min", "max"]).round(2)
print(stats.to_string())

print("\nKey Observations:")
print(f"  • Avg order value  : ${df['TotalPrice'].mean():.2f}")
print(f"  • Median order value: ${df['TotalPrice'].median():.2f}")
print(f"  • Mean > Median → TotalPrice is right-skewed (a few large orders pull the mean up)")
print(f"  • Avg unit price   : ${df['UnitPrice'].mean():.2f}")
print(f"  • Avg quantity/order: {df['Quantity'].mean():.2f} items")
print(f"  • Avg items in cart : {df['ItemsInCart'].mean():.2f}")

# STEP 4  (IQR Method)

print("STEP 4 – OUTLIER DETECTION (IQR Method on TotalPrice)")

Q1  = df["TotalPrice"].quantile(0.25)
Q3  = df["TotalPrice"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["TotalPrice"] < lower_bound) | (df["TotalPrice"] > upper_bound)]
print(f"  Q1 = ${Q1:.2f}  |  Q3 = ${Q3:.2f}  |  IQR = ${IQR:.2f}")
print(f"  Lower fence: ${lower_bound:.2f}  |  Upper fence: ${upper_bound:.2f}")
print(f"\n  Outliers detected: {len(outliers)} records")
print(f"  Outlier TotalPrice range: ${outliers['TotalPrice'].min():.2f} – ${outliers['TotalPrice'].max():.2f}")
print("\n  → These are SIGNAL (very large orders), not data errors. Investigate further.")
print(outliers[["OrderID", "Product", "Quantity", "UnitPrice", "TotalPrice"]].to_string(index=False))

# STEP 5 

print("STEP 5 – PRODUCT PERFORMANCE")

product_stats = df.groupby("Product").agg(
    Orders       = ("OrderID",    "count"),
    AvgUnitPrice = ("UnitPrice",  "mean"),
    AvgQty       = ("Quantity",   "mean"),
    TotalRevenue = ("TotalPrice", "sum")
).round(2).sort_values("TotalRevenue", ascending=False)
print(product_stats.to_string())
top_product = product_stats["TotalRevenue"].idxmax()
print(f"\n  → Top revenue product: {top_product} (${product_stats.loc[top_product,'TotalRevenue']:,.2f})")
print(f"  → Printers have the most orders ({product_stats['Orders'].max()})")

# STEP 6 

print("STEP 6 – ORDER STATUS DISTRIBUTION")

status_counts = df["OrderStatus"].value_counts()
status_pct    = (status_counts / len(df) * 100).round(2)
status_df = pd.DataFrame({"Count": status_counts, "Percentage %": status_pct})
print(status_df.to_string())
cancelled_returned = status_counts["Cancelled"] + status_counts["Returned"]
print(f"\n  → {cancelled_returned} orders ({cancelled_returned/len(df)*100:.1f}%) are Cancelled or Returned.")
print("  → This is a high churn signal worth investigating by product and payment method.")

# STEP 7 

print("STEP 7 – PAYMENT METHOD ANALYSIS")

payment_revenue = df.groupby("PaymentMethod")["TotalPrice"].agg(["count","sum","mean"]).round(2)
payment_revenue.columns = ["Orders","TotalRevenue","AvgOrderValue"]
payment_revenue = payment_revenue.sort_values("TotalRevenue", ascending=False)
print(payment_revenue.to_string())
print(f"\n  → Online payments lead with the most orders ({payment_revenue['Orders'].max()}).")

# STEP 8 

print("STEP 8 – REFERRAL SOURCE ANALYSIS")

referral = df.groupby("ReferralSource").agg(
    Orders  = ("OrderID",    "count"),
    Revenue = ("TotalPrice", "sum")
).round(2).sort_values("Revenue", ascending=False)
print(referral.to_string())
print(f"\n  → Instagram drives the highest revenue (${referral['Revenue'].max():,.2f}).")
print("  → Referral (word-of-mouth) drives the least revenue – a growth opportunity.")

# STEP 9 

print("STEP 9 – COUPON CODE ANALYSIS")

coupon = df.groupby("CouponCode").agg(
    Orders  = ("OrderID",    "count"),
    Revenue = ("TotalPrice", "sum"),
    AvgOrder= ("TotalPrice", "mean")
).round(2).sort_values("Revenue", ascending=False)
print(coupon.to_string())

# STEP 10 

print("STEP 10 – MONTHLY REVENUE TREND")

monthly = df.groupby("Month")["TotalPrice"].sum().reset_index()
monthly["Month"] = monthly["Month"].astype(str)
monthly["Revenue"] = monthly["TotalPrice"].round(2)
print(monthly[["Month","Revenue"]].to_string(index=False))
top_month = monthly.loc[monthly["Revenue"].idxmax()]
low_month  = monthly.loc[monthly["Revenue"].idxmin()]
print(f"\n  → Best month  : {top_month['Month']} (${top_month['Revenue']:,.2f})")
print(f"  → Lowest month: {low_month['Month']} (${low_month['Revenue']:,.2f})")

# STEP 11 

print("STEP 11 – CORRELATION ANALYSIS (Pearson r)")

corr = df[num_cols].corr().round(3)
print(corr.to_string())
print("""
  Interpretation:
  • UnitPrice ↔ TotalPrice  : r = 0.717 → Strong positive correlation
    (Higher priced items naturally produce higher order totals)
  • Quantity  ↔ TotalPrice  : r = 0.615 → Moderate-strong positive
    (More items ordered = higher bill, as expected)
  • Quantity  ↔ ItemsInCart : r = 0.650 → Moderate-strong positive
    (Customers browsing more items tend to buy more)
  • UnitPrice ↔ Quantity    : r = 0.015 → No correlation
    (Price does NOT predict how many units are ordered)

  ⚠ Reminder: Correlation ≠ Causation
""")

# STEP 12 

total_revenue = df["TotalPrice"].sum()
delivered_pct = (df["OrderStatus"] == "Delivered").mean() * 100
cancelled_pct = (df["OrderStatus"] == "Cancelled").mean() * 100
returned_pct  = (df["OrderStatus"] == "Returned").mean() * 100


print("STEP 12 – EXECUTIVE SUMMARY")

print(f"""
Dataset      : 1,200 orders | 14 variables | Jan 2023 – Jun 2025
Total Revenue: ${total_revenue:,.2f}
Avg Order Val: ${df['TotalPrice'].mean():.2f}

KEY FINDINGS:
  1. Revenue is right-skewed. Mean (${df['TotalPrice'].mean():.2f}) > Median
     (${df['TotalPrice'].median():.2f}). Use median for typical customer benchmarks.

  2. High cancellation/return rate. Only {delivered_pct:.1f}% of orders are
     Delivered; {cancelled_pct:.1f}% Cancelled + {returned_pct:.1f}% Returned = critical
     loss to investigate by product/payment method.

  3. Chair and Printer lead in total revenue. Both crossed
     $195,000 in total sales across the period.

  4. Instagram is the #1 revenue-driving channel ($275K+).
     Referral channel is underperforming and should be incentivised.

  5. 8 outlier orders ($3,334–$3,456) detected via IQR.
     These are high-value VIP orders — investigate for upsell strategy.

  6. Unit price is the strongest predictor of order value (r=0.72).
     Focus premium product promotion to drive revenue.

RECOMMENDATIONS:
  → Investigate root cause of 41.4% Cancelled/Returned orders.
  → Launch referral incentive program (lowest revenue channel).
  → Promote high-price products (Laptop, Phone) to boost avg order value.
  → Replicate peak-month (Jun 2024) marketing conditions year-round.
""")
