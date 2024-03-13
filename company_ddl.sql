CREATE TABLE employee (
	emp_id INT,
	first_name VARCHAR (50),
	last_name VARCHAR (50),
	birth_date DATE,
	sex VARCHAR(1),
	salary INT,
	PRIMARY KEY (emp_id)
);

SELECT * from employee;

ALTER TABLE employee
ADD COLUMN super_id INT REFERENCES employee(emp_id) ON DELETE SET NULL;

ALTER TABLE employee
ADD COLUMN branch_id INT REFERENCES branch(branch_id) ON DELETE SET NULL;

ALTER TABLE employee
ADD CHECK (sex='M' or sex ='F');

CREATE TABLE branch(
	branch_id INT,
	branch_name VARCHAR(50),
	mgr_id INT,
	mgr_start_date DATE,
	PRIMARY KEY (branch_id),
	FOREIGN KEY (mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);

SELECT * FROM branch;



CREATE TABLE client(
	client_id INT,
	client_name VARCHAR (50),
	branch_id INT,
	PRIMARY KEY (client_id),
	FOREIGN KEY (branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL
);

SELECT * FROM client;




CREATE TABLE works_with(
	emp_id 	INT,
	client_id INT,
	total_sales INT
);

SELECT * FROM works_with;

ALTER TABLE works_with
ADD CONSTRAINT ck_empid_clientid PRIMARY KEY(emp_id, client_id);

ALTER TABLE works_with
ADD CONSTRAINT emp_id FOREIGN KEY (emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE;

ALTER TABLE works_with
ADD CONSTRAINT client_id FOREIGN KEY (client_id) REFERENCES client(client_id) ON DELETE CASCADE;






CREATE TABLE branch_supplier(
	branch_id INT,
	supplier_name VARCHAR(50),
	supply_type VARCHAR(50)
);

SELECT * FROM branch_supplier;

ALTER TABLE branch_supplier
ADD CONSTRAINT ck_branchid_suppliername PRIMARY KEY(branch_id, supplier_name);

ALTER TABLE branch_supplier
ADD CONSTRAINT branch_id FOREIGN KEY (branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE;





DROP TABLE 'table_name' CASCADE

SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';




-- Corporate
INSERT INTO employee VALUES(100, 'David', 'Wallace', '1967-11-17', 'M', 250000, NULL, NULL);

INSERT INTO branch VALUES(1, 'Corporate', 100, '2006-02-09');

UPDATE employee
SET branch_id = 1
WHERE emp_id = 100;

INSERT INTO employee VALUES(101, 'Jan', 'Levinson', '1961-05-11', 'F', 110000, 100, 1);


-- Scranton
INSERT INTO employee VALUES(102, 'Michael', 'Scott', '1964-03-15', 'M', 75000, 100, NULL);

INSERT INTO branch VALUES(2, 'Scranton', 102, '1992-04-06');

UPDATE employee
SET branch_id = 2
WHERE emp_id = 102;

INSERT INTO employee VALUES(103, 'Angela', 'Martin', '1971-06-25', 'F', 63000, 102, 2);
INSERT INTO employee VALUES(104, 'Kelly', 'Kapoor', '1980-02-05', 'F', 55000, 102, 2);
INSERT INTO employee VALUES(105, 'Stanley', 'Hudson', '1958-02-19', 'M', 69000, 102, 2);

-- Stamford
INSERT INTO employee VALUES(106, 'Josh', 'Porter', '1969-09-05', 'M', 78000, 100, NULL);

INSERT INTO branch VALUES(3, 'Stamford', 106, '1998-02-13');

UPDATE employee
SET branch_id = 3
WHERE emp_id = 106;

INSERT INTO employee VALUES(107, 'Andy', 'Bernard', '1973-07-22', 'M', 65000, 106, 3);
INSERT INTO employee VALUES(108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, 106, 3);


-- BRANCH SUPPLIER
INSERT INTO branch_supplier VALUES(2, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Patriot Paper', 'Paper');
INSERT INTO branch_supplier VALUES(2, 'J.T. Forms & Labels', 'Custom Forms');
INSERT INTO branch_supplier VALUES(3, 'Uni-ball', 'Writing Utensils');
INSERT INTO branch_supplier VALUES(3, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES(3, 'Stamford Lables', 'Custom Forms');

-- CLIENT
INSERT INTO client VALUES(400, 'Dunmore Highschool', 2);
INSERT INTO client VALUES(401, 'Lackawana Country', 2);
INSERT INTO client VALUES(402, 'FedEx', 3);
INSERT INTO client VALUES(403, 'John Daly Law, LLC', 3);
INSERT INTO client VALUES(404, 'Scranton Whitepages', 2);
INSERT INTO client VALUES(405, 'Times Newspaper', 3);
INSERT INTO client VALUES(406, 'FedEx', 2);

-- WORKS_WITH
INSERT INTO works_with VALUES(105, 400, 55000);
INSERT INTO works_with VALUES(102, 401, 267000);
INSERT INTO works_with VALUES(108, 402, 22500);
INSERT INTO works_with VALUES(107, 403, 5000);
INSERT INTO works_with VALUES(108, 403, 12000);
INSERT INTO works_with VALUES(105, 404, 33000);
INSERT INTO works_with VALUES(107, 405, 26000);
INSERT INTO works_with VALUES(102, 406, 15000);
INSERT INTO works_with VALUES(105, 406, 130000);





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


-- index creation

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


-- export sql_shell

\copy employee_bkp to 'C:\Users\Pranav\OneDrive\Documents\company_ddl.csv' csv header