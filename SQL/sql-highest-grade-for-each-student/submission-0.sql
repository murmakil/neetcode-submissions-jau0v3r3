with cte as(
    select student_id, max(score) as score
    from exam_results
    group by student_id
)
select student_id, exam_id, score
from(
    select c.student_id, e.exam_id, c.score,
    row_number() over(partition by c.student_id order by exam_id) as rn
    from cte c
    join exam_results e
     on e.student_id = c.student_id
      and e.score = c.score
)
where rn = 1
order by student_id