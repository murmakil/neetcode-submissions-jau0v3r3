select name, coalesce(travelled_distance, 0) as travelled_distance
from(
    select u.name, sum(r.distance) as travelled_distance
    from users u
    left join rides r
     on r.user_id = u.id
    group by u.name 
)a
order by travelled_distance desc, name