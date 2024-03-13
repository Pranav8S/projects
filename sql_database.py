from sqlalchemy import create_engine,text,MetaData,Table,select,insert,update,delete

from getpass import getpass

password=getpass()

engine = create_engine('postgresql+psycopg2://postgres:{}@localhost:5432/company'.format(password))

with engine.connect() as conn:
    
    try :

        result = conn.execute(text("select * from employee"))

        print('*'*100)
        rows=result.fetchall()
        for row in rows:
            print(row)

        insert = conn.execute(text("insert into employee values(123,'Creed','Braton','1994-12-07','M',350000,102,3)"))

        update = conn.execute(text("update employee set birth_date='2006-11-29' where emp_id=115"))

        delete = conn.execute(text("delete from employee where emp_id=128"))

        conn.commit()

        result = conn.execute(text("select * from employee"))

        print('*'*100)
        rows=result.fetchall()
        for row in rows:
            print(row)

    except Exception as e:

        print(f"{e}")




with engine.connect() as conn:
    
    try:

        metadata = MetaData()

        employee = Table('employee',metadata,autoload_with=engine)

        print('#'*100)
        select_all=conn.execute(select(employee))
        rows=select_all.fetchall()
        for row in rows:
            print(row)
         
        print('#'*100)    
        select_=conn.execute(select(employee.c['first_name','last_name','birth_date','salary']))
        rows=select_.fetchall()
        for row in rows:
            print(row)


        # insert
        print('#'*100)
        insert_stmt = employee.insert().values(emp_id=293,first_name='Kevin',last_name='Malone',super_id=102)
        #print(insert_stmt)
        #compiled=insert_stmt.compile()
        #compiled.params
        conn.execute(insert_stmt)
        conn.commit()

        #update
        print('#'*100)
        update_stmt = employee.update().where(employee.c.birth_date=='1994-12-7').values(salary=100000,sex='F')
        conn.execute(update_stmt)
        conn.commit()


        #delete
        print('#'*100)
        delete_stmt = employee.delete().where(employee.c.salary==69000)
        conn.execute(delete_stmt)
        conn.commit()


    except Exception as e:
        print(f"{e}")
