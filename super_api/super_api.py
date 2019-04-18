from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
engine = SQLAlchemy.create_engine("sqlite:///memory.db")

@app.route('/', methods=['GET'])
def index():
	all_tables_query = """
	SELECT 
	    name
	FROM 
	    sqlite_master 
	WHERE 
	    type ='table' AND 
	    name NOT LIKE 'sqlite_%';
	"""
	return render_template("index.html", tables=pd.read_sql(engine, all_tables=all_tables_query))

@app.route('/create_table', methods=['POST'])
def create_table():
	return f"CREATE TABLE {request.form['table_name']} ({','.join(request.form['columns'].split())});"

@app.route('read_table/<table>', methods=['GET'])
def read_table(table):
	return pd.read_sql(engine, "SELECT * FROM data;")

## CHECK IF I can just put nothing for ID
## If so, then just delete read_one and just use read_table
@app.route('read_one/table/<id>', methods=['GET'])
def read_one(id):
	return pd.read_sql(engine, f"SELECT * FROM data WHERE did={id}")

@app.route('/insert', methods=['POST'])
def insert_one():
	return f"INSERT INTO data VALUES ({','.join(request.form.values())});"

@app.route('/dump', methods=['POST'])
def insert_one():
	return f"INSERT INTO data VALUES ({','.join(request.form.values())});"

@app.route('/update_table/<id>', methods=['PUT'])
def update_one(id):
	return ""

@app.route('/delete_table/<id>', methods=['POST'])
def delete_table(id):
	return ""


if __name__ == "__main__":
	app.run()