-- ADVANCED
SELECT 
    ROUND(
        SUM(
            IF(order_date = customer_pref_delivery_date,1,0)) * 100.0
                / COUNT(*), 2) AS immediate_percentage
FROM
(SELECT *,
    DENSE_RANK() OVER(
                    PARTITION BY customer_id
                    ORDER BY order_date) AS first_order
FROM Delivery) f
WHERE first_order = 1
;



-------------------------------------------
-- INTERMEDIATE
-- SELECT 
--     ROUND(SUM(
--         IF(order_date = customer_pref_delivery_date, 1, 0)
--     ) * 100.0 / COUNT(*), 2) AS immediate_percentage
-- FROM Delivery
-- WHERE (customer_id, order_date) IN (SELECT 
--     customer_id, 
--     MIN(order_date) AS first_order
-- FROM Delivery 
-- -- WHERE order_date = MIN(order_date)
-- GROUP BY customer_id)
-- ;
-----------------------------------

-- BEGINNER
-- SELECT 
--     ROUND(SUM(
--         CASE
--             WHEN d.order_date = d.customer_pref_delivery_date
--                 THEN 1
--             ELSE 0 
--         END
--     ) * 100.0 / COUNT(*), 2) AS immediate_percentage
-- FROM Delivery d
-- LEFT JOIN (
--     SELECT customer_id, MIN(order_date) AS first_order
--     FROM Delivery
--     GROUP BY customer_id
-- ) f
-- ON d.customer_id = f.customer_id
-- WHERE d.order_date = f.first_order
-- ;


-- Table: Delivery

-- +-----------------------------+---------+
-- | Column Name                 | Type    |
-- +-----------------------------+---------+
-- | delivery_id                 | int     |
-- | customer_id                 | int     |
-- | order_date                  | date    |
-- | customer_pref_delivery_date | date    |
-- +-----------------------------+---------+
-- delivery_id is the column of unique values of this table.
-- The table holds information about food delivery to customers that make orders at some date and specify a preferred delivery date (on the same order date or after it).
 

-- If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.

-- The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.

-- Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Delivery table:
-- +-------------+-------------+------------+-----------------------------+
-- | delivery_id | customer_id | order_date | customer_pref_delivery_date |
-- +-------------+-------------+------------+-----------------------------+
-- | 1           | 1           | 2019-08-01 | 2019-08-02                  |
-- | 2           | 2           | 2019-08-02 | 2019-08-02                  |
-- | 3           | 1           | 2019-08-11 | 2019-08-12                  |
-- | 4           | 3           | 2019-08-24 | 2019-08-24                  |
-- | 5           | 3           | 2019-08-21 | 2019-08-22                  |
-- | 6           | 2           | 2019-08-11 | 2019-08-13                  |
-- | 7           | 4           | 2019-08-09 | 2019-08-09                  |
-- +-------------+-------------+------------+-----------------------------+
-- Output: 
-- +----------------------+
-- | immediate_percentage |
-- +----------------------+
-- | 50.00                |
-- +----------------------+
-- Explanation: 
-- The customer id 1 has a first order with delivery id 1 and it is scheduled.
-- The customer id 2 has a first order with delivery id 2 and it is immediate.
-- The customer id 3 has a first order with delivery id 5 and it is scheduled.
-- The customer id 4 has a first order with delivery id 7 and it is immediate.
-- Hence, half the customers have immediate first orders.