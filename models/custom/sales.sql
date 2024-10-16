with product_sales as (
    select
        product_id,
        sum(quantity) as total_sold,
        sum(price * quantity) as total_revenue
    from `skilled-loader-436608-i6`.`dbt_tutorial`.custom_shop_order_items
    group by product_id
)

select
    ps.product_id,
    ps.total_sold,
    ps.total_revenue,
    p.product_name,
    p.price
from product_sales ps
join `skilled-loader-436608-i6`.`dbt_tutorial`.custom_shop_products p 
    on ps.product_id = p.product_id
order by total_sold desc
limit 10
