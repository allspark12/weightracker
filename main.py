from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

# Load existing data from the file, if any
try:
    with open('data.txt', 'r') as file:
        weight_data = json.load(file)
except FileNotFoundError:
    # If the file is not found, initialize with an empty dataset
    weight_data = {
        'time': [],
        'weight': []
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/update_graph", methods=['POST'])
def update_graph():
    weight = float(request.form.get('weight'))

    if not weight:
        return jsonify({'success': False, 'message': 'Invalid weight value'})

    # Update the data
    weight_data['time'].append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    weight_data['weight'].append(weight)

    # Save the updated data to the file
    with open('data.txt', 'w') as file:
        json.dump(weight_data, file)

    return jsonify({'success': True, 'message': 'Weight added successfully'})

@app.route("/get_graph_data")
def get_graph_data():
    return jsonify(weight_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
