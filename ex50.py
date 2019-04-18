from flask import Flask
from SQLAlchemy import create_engine
import pandas as pd

app = Flask(__name__)
engine = create_engine("sqlite:///memory.db")

@app.route('/', methods=['GET'])
def read():
	return pd.read_sql(engine, "SELECT * FROM data;")

@app.route('/<id>', methods=['GET'])
def read_one(id):
	return pd.read_sql(engine, f"SELECT * FROM data WHERE did={id}")

if __name__ == "__main__":
	app.run()