select left_operand, operator, right_operand,
 case operator
    when '>' then (loperand > roperand)
    when '<' then (loperand < roperand)
    else  (loperand = roperand)
 end as value
from( 
    select e.*, v.value as loperand, v1.value as roperand
     from expressions e
     join variables v
     on v.name = e.left_operand
     join variables v1
     on v1.name = e.right_operand
 ) a


  
