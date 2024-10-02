with customer_orders as (
    select *
    from {{ ref('custom') }}  -- Remplacez 'custom' par le nom de votre modèle de commandes clients
),

customer_loyalty as (
    select
        customer_id,
        case 
            when number_of_orders > 26 then 'Really Loyal'
            when number_of_orders between 20 and 25 then 'Loyal'
            when number_of_orders between 15 and 20 then 'Moderate'
            else 'New'
            
        end as loyalty_status,
    from customer_orders
)

SELECT *
FROM customer_loyalty
