# import the module that allows us to interact w/ postgreSQL 
import psycopg2
# connect to our postgreSQL database
conn = psycopg2.connect("postgresql://mattmartin_lab10database_user:u7EzgKpgdZosFadNuNAfnVjIz2USZIPZ@dpg-cqj9ctmehbks73c8agkg-a/mattmartin_lab10database")

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Matthew in 3308'

# db test route 
@app.route('/db_test')
def test():
    # connect to our postgreSQL database
    conn = psycopg2.connect("postgresql://mattmartin_lab10database_user:u7EzgKpgdZosFadNuNAfnVjIz2USZIPZ@dpg-cqj9ctmehbks73c8agkg-a/mattmartin_lab10database")
    conn.close()
    return "Database Connection Sucessful"

# db create route 
@app.route('/db_create')
def create():
    # connect to postgreSQL db 
    conn = psycopg2.connect("postgresql://mattmartin_lab10database_user:u7EzgKpgdZosFadNuNAfnVjIz2USZIPZ@dpg-cqj9ctmehbks73c8agkg-a/mattmartin_lab10database")
    # create a basketball table 
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Sucessfully Created"


@app.route('/db_insert')
def inserting():
    # connect to database
    conn =  psycopg2.connect("postgresql://mattmartin_lab10database_user:u7EzgKpgdZosFadNuNAfnVjIz2USZIPZ@dpg-cqj9ctmehbks73c8agkg-a/mattmartin_lab10database")
    # create a cursor for the connection
    cur = conn.cursor()
    # execute a statement to insert basketball players into the created table
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    #save and commit the changes
    conn.commit()
    #close the connection
    conn.close()
    # return a confirmation string
    return "Basketball Table Succesfully Populated"



    
    
