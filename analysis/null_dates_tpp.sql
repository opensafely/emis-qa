select top 50
conceptid,
Description,
100*round(count(*)/100,0) as count

from codedevent_snomed c
left join ctv3dictionary dict on c.conceptid = dict.ctv3code
where year(consultationdate)=1899
group by conceptid, Description
having count(*)>99
order by count(*) desc




