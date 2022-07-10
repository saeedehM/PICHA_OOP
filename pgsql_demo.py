import psycopg2
import psycopg2

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = '2871375!!!'
port_id = 5432
conn = psycopg2.connect(host=hostname, dbname=database, user=username, password=pwd, port=port_id)
cur = conn.cursor()
create_script = '''Create table if not exists employee2(
    id  int Primary Key,
    name    varchar(40) Not Null,
    salary  int, 
    dept_id varchar(30)
)
'''
cur.execute(create_script)
# insert_script='Insert into employee (id,name,salary, dept_id) values(%s,%s,%s,%s)'
# insert_value= [ (2,'Julie',13000,'D1'),(3,'Robin',15000,'D1'),(4,'Xavier',12000,'D2')]
# for record in insert_value:
#     cur.execute(insert_script,record)

cur.execute('Select * from employee')
# print(cur.fetchall())
for record in cur.fetchall():
    print(record['name'], record['salary'])
update_script = 'Update employee set salary = salary + (salary*0.5)'
cur.execute('Select * from employee')

cur.execute(update_script)
cur.execute('Select * from employee')

# for record in cur.fetchall():
#     print(record[0], record[1])
conn.commit()

delete_script = 'delete from employee where name = %s'
delete_record = ('James',)
cur.execute(delete_script, delete_record)

cur.close()
conn.close()
