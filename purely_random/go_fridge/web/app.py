import random
from datetime import datetime

from flask import Flask, render_template, send_from_directory, jsonify
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'fridge'

mongo = PyMongo(app)

def get_start_time():
    start_time = datetime.now()
    if start_time.hour < 8:
        start_time = start_time - timedelta(1)

    return datetime(start_time.year, start_time.month, start_time.day, 8)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/items')
def get_items():
    print get_start_time()
    item_runs = mongo.db.posts.find({"timestamp": {"$gt": get_start_time()}}).sort("timestamp")

    all_items = []
    for item in item_runs:
        for run in item['items'].keys():
            all_items.append(run)

    items = list(set(all_items))

    return jsonify(items=items)

@app.route('/item/<item>')
def get_item(item):
    item_runs = mongo.db.posts.find({"timestamp": {"$gt": get_start_time()}},
            {'timestamp': 1, 'items.' + item: 1}).sort("timestamp")

    values = [[run['timestamp'], run['items'][item]] for run in item_runs]

    max_val = max(map(lambda x: x[1], values))
    # If the max is 0, we might as well divide by 1 since the result is the same
    # and to avoid divide by zero errors
    if max_val == 0:
        max_val = 1

    # Make relative values based on the baseline
    values = [[value[0], value[1] / max_val] for value in values]

    return jsonify(values=values)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
