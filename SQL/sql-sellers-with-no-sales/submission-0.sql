select seller_name
from seller 
where seller_id not in (select seller_id
                        from orders
                        where sale_date >= '20200101'
                         and sale_date < '20210101'
                        )
order by seller_name 
