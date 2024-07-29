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

#This route will insert data into the Basketball table that you've created.
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

#This route will query all of the data from the database, and return the information in a table.
@app.route('/db_select')
def selecting():
    #create a connection  
    conn = psycopg2.connect("postgresql://mattmartin_lab10database_user:u7EzgKpgdZosFadNuNAfnVjIz2USZIPZ@dpg-cqj9ctmehbks73c8agkg-a/mattmartin_lab10database")
    # create a cursor from the connection
    cur = conn.cursor()
    # execute a statement that selects the table
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    # assign the results to a variable 
    records = cur.fetchall()
    # close the connection
    conn.close()
    # create a string to return the response 
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    # return the formatted table
    return response_string

    
    
