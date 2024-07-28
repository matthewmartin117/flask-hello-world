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
    
