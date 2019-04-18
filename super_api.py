from flask import Flask
from SQLAlchemy import create_engine
import pandas as pd

app = Flask(__name__)
engine = create_engine("sqlite:///memory.db")

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

@app.route('/create', methods=['POST'])
def create_table():
	return f"CREATE TABLE {request.form["table_name"]} ({','.join(request.form["columns"].split())});"

@app.route('/<table>', methods=['GET'])
def read_all(table):
	return pd.read_sql(engine, "SELECT * FROM data;")

@app.route('/<id>', methods=['GET'])
def read_one(id):
	return pd.read_sql(engine, f"SELECT * FROM data WHERE did={id}")

@app.route('/insert', methods=['POST'])
def insert_one():
	return f"INSERT INTO data VALUES ({','.join(request.form.values())});"

@app.route('/dump', methods=['POST'])
def insert_one():
	return f"INSERT INTO data VALUES ({','.join(request.form.values())});"

@app.route('/u/<id>', methods=['POST'])
def update_one(id):
	return ""

@app.route('/d/<id>', methods=['POST'])
def delete_one(id):
	return ""


if __name__ == "__main__":
	app.run()