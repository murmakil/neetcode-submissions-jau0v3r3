with cte as(
select customer_id, customer_name, sum(A) as A, sum(B) as B, sum(C) as C
from (
    select c.customer_id, c.customer_name,
    case when product_name = 'A' then 1 else 0 end as A,
    case when product_name = 'B' then 1 else 0 end as B,
    case when product_name = 'C' then 1 else 0 end as C
    from orders o
    join customers c
     on c.customer_id = o.customer_id
)a
group by customer_id, customer_name
)
select customer_id, customer_name
from cte
where A >= 1 and B >= 1 and C = 0
order by customer_name



