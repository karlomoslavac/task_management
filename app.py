from db_connector import add_task, get_tasks, remove_task, edit_task
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PATCH", "DELETE"]}})


@app.route("/tasks", methods=["GET"])
def route_get_tasks():
    try:
        status = request.args.get('status')
        due_date = request.args.get('due_date')

        response = get_tasks(status, due_date)
        return make_response(jsonify(response), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({'response': 'Fail'}), 500)


@app.route("/tasks", methods=["POST"])
def route_add_task():
    try:
        add_task(
            request.json['name'],
            request.json['description'],
            request.json['status'],
            request.json['due_date']
        )
        response = {"response": "Success"}
        return make_response(jsonify(response), 201)

    except Exception as e:
        print(e)
        return make_response(jsonify({'response': 'Fail'}), 500)
    

@app.route("/tasks", methods=["PATCH"])
def route_edit_task():
    try:
        edit_task(
            request.json['task_id'],
            request.json['name'],
            request.json['description'],
            request.json['status'],
            request.json['due_date']
        )
        response = {"response": "Success"}
        return make_response(jsonify(response), 201)

    except Exception as e:
        print(e)
        return make_response(jsonify({'response': 'Fail'}), 500)


@app.route("/tasks", methods=["DELETE"])
def route_remove_task():
    try:
        status = remove_task(request.json['task_id'])
        if status['response'] == "Success":
            return make_response(jsonify({"response": "Success"}), 201)
        return make_response(jsonify({"response": "Fail"}), 401)
 
    except Exception as e:
        print(e)
        return make_response(jsonify({'response': 'Fail'}), 500)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)