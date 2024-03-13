CREATE TABLE employee (
	emp_id SERIAL, 
	emp_name VARCHAR (50) NOT NULL, 
	emp_city VARCHAR (10), 
	emp_dob DATE NOT NULL,
	PRIMARY KEY (emp_id)
);



CREATE TABLE example(
	id SERIAL,
	img BYTEA
);

SELECT * FROM example;

INSERT INTO example (img) VALUES ('https://www.youtube.com/watch?v=HXV3zeQKqGY&t=7917s')
INSERT INTO example (img) VALUES ('jfaio f 7o872c078o c 7q83t9ptllh oawifuh o847tyqo o4it hq3p4ot[t9agpwrhro36463ergr6gkh4653rzsgi743yt34q t98 I& ^(#&*)$*(@(*% ))')




SELECT * FROM employee
ORDER BY emp_id;

DROP TABLE employee;

TRUNCATE TABLE employee;

ALTER TABLE employee 
ADD emp_exp DECIMAL(2,1) DEFAULT 0;

ALTER TABLE employee 
ALTER COLUMN emp_exp TYPE DECIMAL(3,1);

ALTER TABLE employee 
ADD CONSTRAINT emp_city UNIQUE (emp_city);


INSERT INTO employee (emp_name, emp_city, emp_dob, emp_exp) VALUES ('Jake', 'Delhi', '1997-09-18', 3.6);
INSERT INTO employee (emp_name, emp_city, emp_dob, emp_exp) VALUES ('Amy', 'Paris', '2000-04-09', 1.9);
INSERT INTO employee (emp_name, emp_city, emp_dob, emp_exp) VALUES ('Pehlaj', 'Mumbai', '1984-09-18', 7.4);
INSERT INTO employee (emp_name, emp_city, emp_dob, emp_exp) VALUES ('Harsh', 'Pune', '1994-09-18', 4.3);
INSERT INTO employee (emp_name, emp_city, emp_dob, emp_exp) VALUES ('Thomas', 'Munich', '1999-09-18', 2.8);

INSERT INTO employee (emp_name, emp_dob) VALUES ('Claire', '2002-12-05');
INSERT INTO employee VALUES (13, 'Aditya', '2002-12-05');

SELECT * FROM employee
ORDER BY emp_id;

DELETE FROM employee WHERE emp_id = 11;

UPDATE employee
SET emp_name = 'Jeet', emp_dob = '1991-11-30', emp_exp = 5.2
WHERE emp_id = 6;

INSERT INTO employee (emp_name, emp_city, emp_dob) VALUES ('Rohit', 'Toronto', '2002-12-05');

DELETE FROM employee WHERE emp_name = 'Ashutosh';

INSERT INTO employee (emp_name, emp_city, emp_dob) VALUES ('Ashutosh', 'Texas', '2002-09-25');

UPDATE employee
SET emp_dob = '2001-04-09'
WHERE emp_name = 'Amy'

SELECT * FROM employee;

DELETE FROM employee 
WHERE emp_dob > '2002-10-01';


SELECT emp_city FROM employee;

SELECT emp_name, emp_dob FROM employee;

SELECT employee.emp_name, employee.emp_dob 
FROM employee
ORDER BY emp_name DESC;

SELECT employee.emp_name, employee.emp_dob
FROM employee
ORDER BY emp_dob, emp_name;

SELECT emp_name FROM employee
LIMIT 2;

SELECT emp_city
FROM employee
ORDER BY emp_city
LIMIT 5;

SELECT emp_name FROM employee
WHERE emp_dob > '1998-01-01';

SELECT emp_id, emp_name, emp_city FROM employee
WHERE emp_city <> 'Paris';

SELECT emp_name FROM employee
WHERE '1950-01-01' < emp_dob < '1998=01-01';


SELECT emp_name FROM employee
WHERE emp_city = 'Pune' OR emp_city ='Mumbai';

SELECT emp_name, emp_exp FROM employee
WHERE emp_exp > 3 AND emp_dob < '1999-01-01'
ORDER BY emp_exp DESC;


SELECT *
FROM employee
WHERE emp_name IN ('Pehlaj', 'Ashutosh', 'Rohit');

SELECT *
FROM employee
WHERE emp_name IN ('Pehlaj', 'Ashutosh', 'Rohit') AND emp_exp < 6;

SELECT emp_name, emp_city, emp_exp, emp_dob 
FROM employee
WHERE emp_city IN ('Paris', 'Texas', 'Delhi') OR (emp_exp > 2 AND emp_dob > '1999-01-01')






CREATE TABLE department (
	dept_id SERIAL,
	dept_name VARCHAR(10)
);


SELECT * FROM department;

ALTER TABLE department DROP emp_id;

INSERT INTO department (dept_name) VALUES ('Sales');
INSERT INTO department (dept_name) VALUES ('Corporate');
INSERT INTO department (dept_name) VALUES ('Analytics');
INSERT INTO department (dept_name) VALUES ('HR');


CREATE TABLE emp_dept (
	emp_id INT,
	dept_id INT,
	PRIMARY KEY (emp_id),
	FOREIGN KEY (dept_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);

SELECT * FROM emp_dept;

INSERT INTO emp_dept VALUES (4,2);
INSERT INTO emp_dept VALUES (3,1);
INSERT INTO emp_dept VALUES (5,3);
INSERT INTO emp_dept VALUES (6,1);
INSERT INTO emp_dept VALUES (1,4);
INSERT INTO emp_dept VALUES (9,4);
INSERT INTO emp_dept VALUES (2,3);
INSERT INTO emp_dept VALUES (10,4);

SELECT * FROM emp_dept;

ALTER TABLE emp_dept
DROP CONSTRAINT emp_id;

ALTER TABLE emp_dept
DROP CONSTRAINT dept_id;

ALTER TABLE emp_dept
ADD CONSTRAINT dept_id FOREIGN KEY(dept_id) REFERENCES department(dept_id)
ON DELETE SET NULL;

ALTER TABLE emp_dept
ADD CONSTRAINT emp_id FOREIGN KEY(emp_id) REFERENCES employee(emp_id)
ON DELETE SET NULL;

ALTER TABLE emp_dept
RENAME COLUMN ddeepptt_id TO dept_id;

SELECT * FROM department;

ALTER TABLE department ADD COLUMN mgr_id INT;

ALTER TABLE department DROP COLUMN mgr_id;


ALTER TABLE department 
ADD FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL;

ALTER TABLE department
ADD CONSTRAINT dept_name UNIQUE (dept_name);

ALTER TABLE department
ALTER COLUMN dept_name SET NOT NULL;

UPDATE department
SET mgr_id = 6 
WHERE dept_id = 1;

UPDATE department
SET mgr_id = 4 
WHERE dept_id = 2;

UPDATE department
SET mgr_id = 2 
WHERE dept_id = 3;

UPDATE department      
SET mgr_id = 9 
WHERE dept_id = 4;

SELECT * FROM department;

DELETE FROM department
WHERE dept_name IS NULL;




ALTER TABLE employee
ADD COLUMN sup_id INT;

ALTER TABLE employee
ADD CONSTRAINT sup_id FOREIGN KEY(sup_id) REFERENCES employee(emp_id) ON DELETE SET NULL;

SELECT * FROM employee;

UPDATE employee
SET sup_id = 1 WHERE emp_id IN (4,9,10);

UPDATE employee
SET sup_id = 5 WHERE emp_id IN (1,2,3);

UPDATE employee
SET sup_id = 1 WHERE emp_id IN (1,4,5,10);

select min(emp_exp) as second_highest_emp_exp 
from employee
where emp_id in(
select emp_id 
from employee
order by emp_exp desc
limit 2);


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';


SELECT * INTO employee_bkp FROM employee;

SELECT * FROM employee_bkp;
