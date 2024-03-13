create table bookings(
	booking_id int,
	name varchar,
	host_id int,
	host_name varchar,
	neighbourhood_group varchar(50),
	neighbourhood varchar(50),
	latitude decimal(7,5),
	longitude decimal(7,5),
	room_type varchar(50),
	price int,
	minimum_nights int,
	number_of_reviews int,
	last_review	date,
	reviews_per_month decimal(4,2),
	calculated_host_listings_count int,
	availability_365 int,
	primary key(booking_id)	
)

drop table bookings;



-- sql shell command to copy dtaa from csv file
ny_airbnb=# \COPY bookings FROM 'C:\Users\Pranav\OneDrive\Documents\AB_NYC_2019.csv' delimiter ',' CSV HEADER ENCODING 'utf-8'
COPY 48895



select * from bookings

select max(len)
from(
	select length(name) as len
	from bookings
) as subquery;


-- over()


select booking_id, name, host_name, neighbourhood, price, 
avg(price) over(),
min(price) over(),
max(price) over()
from bookings;


select booking_id, name, host_name, neighbourhood, price, 
round(price - avg(price) over()) as diff_from_avg_price,
round(price - max(price) over()) as diff_from_max_price
from bookings;

select max(price) from bookings;

select booking_id, name, host_name, neighbourhood_group, price, round(avg(price) over()) as avg_price,
round(price / avg(price) over() * 100) || '%' as percent_avg_price,
round(ceil(price) / max(price) over() * 100) || '%' as percent_max_price
from bookings;



-- partition by

select booking_id, name, host_name, neighbourhood_group, round(avg(price) over()) as avg_price,
round(avg(price) over(partition by neighbourhood_group)) as avg_price_of_ngh_group
from bookings;

select * from bookings

select booking_id, name, host_name, neighbourhood_group, round(avg(price) over()) as avg_price,
round(avg(price) over(partition by neighbourhood_group)) as avg_price_of_ngh_group,
round(avg(price) over(partition by neighbourhood_group, neighbourhood)) as avg_price_of_ngh
from bookings;

select booking_id, name, neighbourhood_group, neighbourhood, price, round(avg(price) over()) as avg_price,
price - round(avg(price) over(partition by neighbourhood_group)) as delta_price_ngh_group,
price - round(avg(price) over(partition by neighbourhood_group, neighbourhood)) as delta_price_of_ngh
from bookings;



--row_number


select booking_id, name, neighbourhood_group, neighbourhood, price,
row_number() over(order by price desc) as overall_price_rank
from bookings


select booking_id, name, neighbourhood_group, neighbourhood, price,
row_number() over(order by price desc) as overall_price_rank,
row_number() over(partition by neighbourhood_group order by price desc) as ngh_group_price_rank
from bookings


select booking_id, name, neighbourhood_group, neighbourhood, price,
row_number() over(order by price desc),
row_number() over(partition by neighbourhood_group order by price desc) as ngh_group_price_rank,
row_number() over(partition by neighbourhood_group, neighbourhood order by price desc) as ngh_price_rank
from bookings


--top 3

with cte as (
	select booking_id, name, neighbourhood_group, neighbourhood, price,
	row_number() over(partition by neighbourhood_group, neighbourhood order by price desc) as ngh_price_rank
	from bookings
	)
select * from cte where ngh_price_rank <= 3

select booking_id, name, neighbourhood_group, neighbourhood, price,
row_number() over(partition by neighbourhood_group, neighbourhood order by price desc) as ngh_price_rank,
case
	when row_number() over(partition by neighbourhood_group, neighbourhood order by price desc) <=3 then 'yes'
	else 'no'
end as is_top_3
from bookings



-- rank

select booking_id, name, neighbourhood_group, price,
row_number() over(order by price desc) as overall_price_rank,
rank() over(order by price desc) as overall_price_rank_with_rank
from bookings

-- dense rank

select booking_id, name, neighbourhood_group, price,
row_number() over(order by price desc) as overall_price_rank,
rank() over(order by price desc) as overall_price_rank_with_rank,
dense_rank() over(order by price desc) as overall_price_with_dense_rank
from bookings



select distinct(neighbourhood_group), count(1) 
from bookings
group by neighbourhood_group

select neighbourhood_group, max(price)
from bookings
group by neighbourhood_group



with cte as(
	select booking_id, name, neighbourhood_group, price,
	dense_rank() over(partition by neighbourhood_group order by price desc) as price_rank
	from bookings
)
select * from cte
where price_rank <=3


-- lag and lead

select * from bookings

select booking_id, name, neighbourhood_group, price,
lag(price) over(partition by neighbourhood_group order by price desc) as lagging_price,
lead(price) over(partition by neighbourhood_group order by price desc) as leading_price
from bookings


select booking_id, name, neighbourhood_group, price,
lag(last_review,3) over(partition by neighbourhood_group order by price desc) as previous_last_review_date_record,
last_review,
lead(last_review,3) over(partition by neighbourhood_group order by price desc) as next_last_review_date_record
from bookings

with cte as (
	select booking_id, name, neighbourhood_group,
	rank() over(partition by neighbourhood_group order by price desc) as ngh_group_price_rank,
	lag(price) over(partition by neighbourhood_group order by price desc) as lagging_prev_price,
	price,
	lead(price) over(partition by neighbourhood_group order by price desc) as leading_next_price
	from bookings
	)
select * from cte
where ngh_group_price_rank <=5


-- rolling sum

select booking_id, name, neighbourhood_group, price,
sum(price) over(order by last_review range between unbounded preceding and current row) as rolling_sum
from bookings


-- rolling sum over 7 days

select booking_id, name, neighbourhood_group, price, last_review,
sum(price) over(order by last_review range between interval '7 days' preceding and current row) as rolling_sum_7days
from bookings


-- rolling sum over 7 rows

select booking_id, name, neighbourhood_group, price, last_review,
sum(price) over(order by price desc rows between 7 preceding and current row) as rolling_sum_7rows
from bookings


-- moving average 10 rows

select booking_id, name, neighbourhood_group, price, last_review,
round(avg(price) over(order by price desc rows between current row and 9 following)) as moving_avg_10rows
from bookings
