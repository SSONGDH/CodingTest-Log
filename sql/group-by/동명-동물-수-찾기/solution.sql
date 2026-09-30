SELECT NAME, count(NAME) as COUNT
from ANIMAL_INS A
group by NAME
having count(NAME)>=2
order by NAME
