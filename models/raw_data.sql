
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}

WITH numeros AS (
    SELECT 
        CAST(n AS INT) AS numero
    FROM 
        UNNEST(GENERATE_ARRAY(1, 100)) AS n
)

SELECT *
FROM numeros
/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
