#CREATING TABLE 
CREATE TABLE Orders (
    OrderID         VARCHAR(20)   PRIMARY KEY,
    OrderDate       DATE,
    CustomerID      VARCHAR(10),
    Product         VARCHAR(50),
    Quantity        INT,
    UnitPrice       DECIMAL(10,2),
    ShippingAddress VARCHAR(100),
    PaymentMethod   VARCHAR(20),
    OrderStatus     VARCHAR(20),
    TrackingNumber  VARCHAR(20),
    ItemsInCart     INT,
    CouponCode      VARCHAR(20),
    ReferralSource  VARCHAR(20),
    TotalPrice      DECIMAL(10,2)
);


# 1ST QUERY view all
SELECT * FROM Orders;


# 2ND QUERY key columns
SELECT OrderID, Product, Quantity, UnitPrice, TotalPrice, OrderStatus, ReferralSource
FROM Orders;


# 3RD where status = delivered
SELECT OrderID, CustomerID, Product, TotalPrice, OrderStatus
FROM Orders
WHERE OrderStatus = 'Delivered'
ORDER BY TotalPrice DESC;


# 4TH orders above 2000
SELECT OrderID, CustomerID, Product, Quantity, TotalPrice
FROM Orders
WHERE TotalPrice > 2000
ORDER BY TotalPrice DESC;


#5TH orders using coupons
SELECT OrderID, Product, CouponCode, TotalPrice, OrderStatus
FROM Orders
WHERE CouponCode IS NOT NULL AND CouponCode != ''
ORDER BY CouponCode;



#6th insta orders paid by credit cards
SELECT OrderID, Product, PaymentMethod, ReferralSource, TotalPrice
FROM Orders
WHERE ReferralSource = 'Instagram'
AND PaymentMethod = 'Credit Card';


#7 counting orders by status
SELECT OrderStatus, COUNT(*) AS TotalOrders
FROM Orders
GROUP BY OrderStatus
ORDER BY TotalOrders DESC;


#8 revenue by product
SELECT Product, COUNT(*) AS TotalOrders, SUM(TotalPrice) AS TotalRevenue, AVG(TotalPrice) AS AvgOrderValue
FROM Orders
GROUP BY Product
ORDER BY TotalRevenue DESC;


#9 count orders by mpayment method
SELECT PaymentMethod, COUNT(*) AS NumberOfOrders, SUM(TotalPrice) AS TotalRevenue
FROM Orders
GROUP BY PaymentMethod
ORDER BY NumberOfOrders DESC;



#10 count revenue by referral
SELECT ReferralSource, COUNT(*) AS TotalOrders, SUM(TotalPrice) AS TotalRevenue, AVG(TotalPrice) AS AvgOrderValue
FROM Orders
GROUP BY ReferralSource
ORDER BY TotalRevenue DESC;



#11 cancelled & returned orders per product
SELECT Product, OrderStatus, COUNT(*) AS OrderCount
FROM Orders
WHERE OrderStatus IN ('Cancelled', 'Returned')
GROUP BY Product, OrderStatus
ORDER BY Product, OrderCount DESC;



#12 5 highest revenue
SELECT OrderID, CustomerID, Product, Quantity, TotalPrice, OrderStatus
FROM Orders
ORDER BY TotalPrice DESC
LIMIT 5;


#13 avg order value by coupon
SELECT 
CASE WHEN CouponCode IS NULL OR CouponCode = '' THEN 'No Coupon'
ELSE CouponCode END AS CouponUsed,
COUNT(*) AS TotalOrders,
AVG(TotalPrice) AS AvgOrderValue,
SUM(TotalPrice) AS TotalRevenue
FROM Orders
GROUP BY CouponUsed
ORDER BY AvgOrderValue DESC;



#14 products w avg revenue above 1000
SELECT Product, COUNT(*) AS TotalOrders, AVG(TotalPrice) AS AvgRevenue
FROM Orders
GROUP BY Product
HAVING AVG(TotalPrice) > 1000
ORDER BY AvgRevenue DESC;


#15 referral sources w morethan 20 orders
SELECT ReferralSource, COUNT(*) AS TotalOrders
FROM Orders
GROUP BY ReferralSource
HAVING COUNT(*) > 20
ORDER BY TotalOrders DESC;



#16 full summary
SELECT
COUNT(*) AS TotalOrders,
COUNT(DISTINCT CustomerID) AS UniqueCustomers,
SUM(TotalPrice) AS GrossRevenue,
AVG(TotalPrice) AS AvgOrderValue,
MAX(TotalPrice) AS LargestOrder,
MIN(TotalPrice) AS SmallestOrder,
SUM(CASE WHEN OrderStatus = 'Delivered' THEN 1 ELSE 0 END) AS DeliveredOrders,
SUM(CASE WHEN OrderStatus = 'Cancelled' THEN 1 ELSE 0 END) AS CancelledOrders,
SUM(CASE WHEN OrderStatus = 'Returned' THEN 1 ELSE 0 END) AS ReturnedOrders
FROM Orders;