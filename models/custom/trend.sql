select
    extract(year from co.order_date) as order_year,
    extract(month from co.order_date) as order_month,
    count(co.order_id) as total_orders,
    sum(so.price * so.quantity) as total_revenue
from `skilled-loader-436608-i6`.`dbt_tutorial`.custom_shop_order_items so
join `skilled-loader-436608-i6`.`dbt_tutorial`.custom_shop_orders co 
    on co.order_id = so.order_id
group by order_year, order_month
order by order_year, order_month
