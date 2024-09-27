with customers as (

    select
    id as customer_id,
    first_name,
    last_name,
    from `skilled-loader-436608-i6`.dbt-tutorial.custom_shop_customers
),

orders as (
    select
    id as order_id,
    user_id as customer_id,
    order_date,
    status,
    from `skilled-loader-436608-i6`.dbt-tutorial.custom_shop_orders
),


customer_orders as (
    select
    customer_id,
    min(order_date) as first_order_date,
    max(order_date) as most_recent_order_date,
    count(order_id) as number_of_orders,
    from orders
    group by 1
)


SELECT *
FROM customer_orders