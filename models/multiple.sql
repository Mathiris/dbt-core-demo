
-- Use the `ref` function to select from other models

SELECT *
FROM {{ ref('raw_data') }}
WHERE MOD(numero, 10) = 0