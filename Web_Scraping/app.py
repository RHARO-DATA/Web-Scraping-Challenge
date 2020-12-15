

from flask import Flask, render_template
import pymongo
app = Flask(__name__)
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.mars_db


@app.route('/')
def index():



@app.route('/scrape')
def scrape():



if __name__ == "__main__":
	app.run(debug=True)