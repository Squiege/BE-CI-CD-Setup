from flask import Flask, request, jsonify

app = Flask(__name__)

sums_data = [
    {"num1": 5, "num2": 10, "result": 15},
    {"num1": -5, "num2": 15, "result": 10},
    {"num1": 20, "num2": 10, "result": 30}
]

@app.route('/sum', methods=['POST'])
def sum():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    return jsonify({'result': result})

@app.route('/sum/result/<int:filter_value>', methods=['GET'])
def get_sums_by_result(filter_value):
    filtered_sums = [i for i in sums_data if i['result'] == filter_value]
    if not filtered_sums:
        return jsonify({"error": "No sums found for the given filter value"}), 404
    return jsonify(filtered_sums), 200