select * from branch;
select * from employee;
select * from client;
select * from works_with;
select * from branch_supplier;

--All_TABLES
SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';

-- TABLE CONSTAINTS
SELECT
    constraint_name,
    constraint_type
FROM
    information_schema.table_constraints
WHERE
    table_name = 'employee';

select * from employee
order by salary desc;

select * from employee 
order by sex, first_name, last_name;

select * from employee
limit 5;

select first_name as Forename, last_name as Surname from employee;

select distinct sex from employee;

select avg(salary) from employee
where sex = 'F';

select count(*) from employee;

select max(salary) from employee;

select count(emp_id)
from employee
where sex = 'M' and birth_date > '1970-01-01';

SELECT SUM (salary) from employee;

select count(1), sex from employee
group by sex;

select length(first_name), length(last_name)
from employee;

select min(salary) from employee;

select sum(total_sales), emp_id
from works_with
group by emp_id
order by sum desc;

select sum(total_sales), client_id
from works_with
group by client_id
order by sum;

select first_name from employee
where first_name LIKE 'J%';

select first_name from employee
where first_name LIKE '%y';

select client_name from client
where client_name LIKE '%LLC';

select supplier_name from branch_supplier
where supplier_name LIKE '%Label%';

select branch_name from branch
where branch_name LIKE 'Sc______';

select first_name, last_name from employee
where extract (month from birth_date) = 10;

select * from employee
where first_name LIKE '%a%';

select * from employee
where last_name LIKE '%a__';

select * from client
where client_name LIKE '%school%';

select * from employee
where super_id is NULL;

select * from employee
where last_name LIKE '[A-Z]%';

select * from employee
where last_name LIKE 'B%';

select * from employee
where salary between 100000 and 300000;

select * from employee
where salary not between 100000 and 300000;

select * from client
where client_name not LIKE 'F%';

select * from client
where lower(client_name) LIKE 't%';




select first_name as all_names
from employee
union
select client_name
from client
union
select branch_name
from branch;


select salary as total_revenue from employee
union
select total_sales from works_with;

select * from branch
insert into branch values (4,'Buffalo',NULL,NULL)



select employee.emp_id, employee.first_name, employee.last_name, branch.branch_name
from employee
join branch
on
employee.emp_id = branch.mgr_id


select employee.emp_id, employee.first_name, employee.last_name, branch.branch_name
from employee
left join branch
on
employee.emp_id = branch.mgr_id


select employee.emp_id, employee.first_name, employee.last_name, branch.branch_name
from employee
right join branch
on
employee.emp_id = branch.mgr_id


select employee.emp_id, employee.first_name, employee.last_name, branch.branch_name
from employee
full outer join branch
on
employee.emp_id = branch.mgr_id


select branch.branch_name, client.client_name
from branch
join client
on branch.branch_id = client.branch_id
order by branch_name


select employee.first_name, employee.last_name, client.client_name
from employee
join works_with ON employee.emp_id = works_with.emp_id
join client on works_with.client_id = client.client_id


select employee.first_name, employee.last_name, employee.salary, branch.branch_name, works_with.total_sales
from employee
join works_with on employee.emp_id = works_with.emp_id
join branch on employee.branch_id = branch.branch_id
order by branch.branch_name


select branch.branch_name, sum(works_with.total_sales) as total_sales
from employee
join works_with on employee.emp_id = works_with.emp_id
join branch on employee.branch_id = branch.branch_id
group by branch.branch_name



select branch.branch_name, sum(employee.salary) as total_salary, sum(works_with.total_sales) as total_sales
from employee
full outer join works_with on employee.emp_id = works_with.emp_id
full outer join branch on employee.branch_id = branch.branch_id
group by branch.branch_name



select * from branch;
select * from employee;
select * from client;
select * from works_with;
select * from branch_supplier;


select first_name, last_name
from employee
where emp_id in(
	select emp_id 
	from works_with
	where total_sales > 30000)
	
select client_name
from client
where branch_id in(
	select branch_id 
	from branch
	where mgr_id in(
		select emp_id
		from employee
		where first_name='Michael' and last_name='Scott'))
		
select sex, round(avg(salary),2) from employee
group by sex
having avg(salary) > 50000

select emp_id, first_name, last_name, salary 
from employee
where exists(select emp_id from employee where salary > 50000)


-- trigger table

create table trigger_test( message varchar(100));

alter table trigger_test add date_time timestamp; 

select * from trigger_test;

INSERT INTO trigger_test VALUES ('example', CURRENT_TIMESTAMP)





-- Insert Trigger Function
CREATE OR REPLACE FUNCTION my_trigger_insert()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO trigger_test VALUES('EMPLOYEE RECORD' || ' ' || NEW.emp_id || ',' || NEW.first_name || ' ' || NEW.last_name || ' ' ||'INSERTED' || ' ' || 'BY' || ' ' || current_user, CURRENT_TIMESTAMP);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Associate Trigger with the Function
CREATE OR REPLACE TRIGGER my_trigger_insert
BEFORE INSERT ON employee
FOR EACH ROW
EXECUTE FUNCTION my_trigger_insert();



DROP TRIGGER IF EXISTS my_trigger ON employee;

DROP FUNCTION IF EXISTS my_trigger_function();



-- Delete Trigger Function
CREATE OR REPLACE FUNCTION my_trigger_delete()
RETURNS TRIGGER AS $$
BEGIN
	INSERT INTO trigger_test VALUES('EMPLOYEE RECORD' || ' ' ||OLD.emp_id || ',' || OLD.first_name || ' ' || OLD.last_name || ' ' || 'DELETED' || ' ' || 'BY' || ' ' || current_user, CURRENT_TIMESTAMP);
	RETURN OLD;
END;
$$ LANGUAGE plpgsql;

-- Associate Trigger with the Function
CREATE OR REPLACE TRIGGER  my_trigger_delete
BEFORE DELETE ON employee
FOR EACH ROW
EXECUTE FUNCTION my_trigger_delete();



-- Update Trigger Function
CREATE OR REPLACE FUNCTION my_trigger_update()
RETURNS TRIGGER AS $$
BEGIN
	INSERT INTO trigger_test VALUES('EMPLOYEE RECORD' || ' ' || NEW.emp_id || ',' || NEW.first_name || ' ' || NEW.last_name || ' '|| 'UPDATED' || ' ' || 'BY' || ' ' || current_user,CURRENT_TIMESTAMP);
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Associate Trigger with the Function
CREATE OR REPLACE TRIGGER my_trigger_update
BEFORE UPDATE ON employee
FOR EACH ROW
EXECUTE FUNCTION my_trigger_update();


ALTER TABLE trigger_log
RENAME TO trigger_test;

truncate table trigger_test;

select * from trigger_test;


select message from trigger_test where date_time between now() - interval '24 hours' and now()

select message from trigger_test where date_time between '2023-11-23 00:00:00' and now()

select * from employee;

INSERT INTO employee VALUES(112, 'Dwight', 'Schrute', '1965-11-29', 'M', 80000, 102, 2)

UPDATE employee
SET birth_date='1964-01-13'
WHERE emp_id=111

delete from employee where emp_id=112 returning *;

SELECT * FROM information_schema.triggers WHERE event_object_table = 'employee';

SELECT trigger_name, event_object_table, action_statement
FROM information_schema.triggers
WHERE event_object_table = 'employee';



select * from employee
where emp_id=105

insert into employee values(118, 'Jan', 'Levinson',	'1961-05-11', 'F', 110000,100,1)
insert into employee values(119, 'Stanley', 'Hudson', '1958-02-19', 'M', 69000, 102, 2)
insert into employee values(149,'Andy','Bernard','1973-07-22','M',65000,106,3)



-- query to list duplicate entries

select a.* 
from employee a
join (select first_name, last_name, birth_date, count(1)
	  from employee
	  group by first_name, last_name, birth_date
	  having count(1) > 1) b
on a.birth_date=b.birth_date
order by first_name, last_name


-- delete duplicates

delete a
from employee a, employee b
where a.emp_id = b.emp_id
and a.emp_id > b.emp_id


-- backup of employee

CREATE TABLE employee_bkp
AS 
SELECT *
FROM employee

select * from employee_bkp



-- indexing
create index idx_emp_id
on employee_bkp(emp_id)

create index idx_name
on employee_bkp(first_name)

drop index idx_name

select * from employee_bkp
where first_name='Stanley' and last_name ='Hudson'

explain analyze select * from employee_bkp
where first_name='Stanley' 

explain analyze select * from employee
where first_name='Stanley' 



explain analyze
select * from employee
limit 5 offset 2



-- common table expressions

with cte as
	(select a.* 
	 from employee a
	 join (select first_name, last_name, birth_date, count(1)
		 from employee
		 group by first_name, last_name, birth_date
	 	 having count(1) > 1) b
	 on a.birth_date=b.birth_date
	 order by first_name, last_name)	 
select * from cte


describe employee_bkp 


-- view

create or replace view duplicates
as 
	select a.* 
	 from employee a
	 join (select first_name, last_name, birth_date, count(1)
		 from employee
		 group by first_name, last_name, birth_date
	 	 having count(1) > 1) b
	 on a.birth_date=b.birth_date
	 order by first_name, last_name


select * from duplicates




-- misc

select 1 + '1'

select 1 + 'abc'

select 1 + Null

select 1/0

select True and '0'

select False or '1'

select Null or False




-- functions

select now()

select current_date

select current_time

select extract(hour from timestamp '2001-02-16 20:38:40') 

select extract(day from timestamp '2001-02-16 20:38:40')

select extract(month from timestamp '2001-02-16 20:38:40')

select '2015-08-11'::date + interval '10 days'

select '2015-08-11'::date - interval '10 days'

select to_char(birth_date::date, 'Day') as day_of_birth from employee

select to_char(birth_date::date, 'Month') as month_of_birth from employee

select extract(quarter from timestamp '2001-02-16 20:38:40')

select extract(week from timestamp '2001-02-16 20:38:40')

select current_timestamp

-- select weekday('2017-06-20 09:34:00')

-- select date(now()-interval '24 hours')

-- select datepart(day,'2021-07-14T13:30:15')

-- select datediff('2017-02-18', interval '10 days')



select session_user

select current_user

select system_user

select user

select version()

select concat(first_name,'::',last_name) from employee

select first_name || '<>' ||last_name from employee

select upper('ghghg')
select lower('UEFIBEF')

select position('uhh' in 'faiue fu asf sfu uuhjj uhh jauf UUH')

select left(first_name,3) from employee
select right(last_name,7) from employee

select (length(first_name) + length(last_name)) as name_length from employee

select trim('   	bsky  			')
select ltrim('    lsod')
select rtrim('didn   ')

select repeat('djdb',6)

select replace('sql tutorial','sql','html')

select upper(replace(lower('XYZ FGH XYZ'), 'x', 'm'));

select reverse(first_name), reverse(last_name) from employee

select reverse(birth_date) from employee

select concat(first_name, repeat('<>',50), last_name) from employee

select first_name=last_name from employee

select substring(first_name,2,length(first_name)) from employee
select substring(last_name,-3,2) from employee
select substring(last_name,length(last_name)-2,2) from employee

select split_part('888-444-7333','-',2)
select split_part(birth_date,'-',2) from employee

select cast('2020-04-13' as date)

select cast('2020-04-13' as timestamp)

select cast('2021-12-27' as varchar)

select cast('2000-02-29' as bytea)

select cast(Null as varchar)

select cast(False as int)

select cast(567766 as decimal(10,2))

select cast(True as int)



select * from employee

select 
	case 
		when first_name ~ '^[M-Z].+' then 'exhbit_a'
		when last_name ~ '^[A-L].+' then 'exhibit b'
		else 'exhibit null'
	end as exhibit_name
from employee

create or replace view test_demo as
select replace(first_name, 'Andy', 'Ryan') as modified_name from employee

select * from test_demo

select substring(last_name,2,7) from employee

select substring(salary::varchar from 1 for 3) from employee




-- STORED PROCEDURE

CREATE OR REPLACE PROCEDURE test_procedure()
AS $$
BEGIN
	PERFORM * FROM employee;
END
$$ LANGUAGE plpgsql;

CALL test_procedure()


CREATE OR REPLACE PROCEDURE insert_data(fname varchar(50), lname varchar(50), bdate date, salary int)
AS $$
DECLARE 
	f_name varchar(50);
	l_name varchar(50);
	b_date date;
	salary int;
BEGIN
	f_name :=fname;
	l_name :=lname;
	b_date :=bdate;
	salary :=salary;
	INSERT INTO employee VALUES (199,f_name,l_name,b_date,salary);
	COMMIT;
END
$$ LANGUAGE plpgsql;

CALL insert_data('Daryl','Sanders','1985-09-17',73000)

select * from employee

