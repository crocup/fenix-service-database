from flask import Flask, jsonify, request, abort
import config
from database import MessageProducer, MongoDriver

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)


@app.route('/api/v1/database/get_one', methods=['POST'])
def message_one():
    if not request.json or not 'data':
        abort(400)
    data = request.json
    message_mongo = MessageProducer(MongoDriver(host='localhost', port=27017,
                                                base=data["base"], collection=data["collection"]))
    result = message_mongo.get_message(message=data["data"])
    return jsonify({"result": result})


@app.route('/api/v1/database/get_all', methods=['POST'])
def message_all():
    if not request.json or not 'data':
        abort(400)
    data = request.json
    message_mongo = MessageProducer(MongoDriver(host='localhost', port=27017,
                                                base=data["base"], collection=data["collection"]))
    result = message_mongo.get_all_message()
    return jsonify({"result": result})


@app.route('/api/v1/database/insert', methods=['POST'])
def message_insert():
    if not request.json or not 'data':
        abort(400)
    data = request.json
    message_mongo = MessageProducer(MongoDriver(host='localhost', port=27017,
                                                base=data["base"], collection=data["collection"]))
    message_mongo.insert_message(message=data["data"])
    return jsonify({"result": "OK"})


@app.route('/api/v1/database/upsert', methods=['POST'])
def message_upsert():
    if not request.json or not 'data':
        abort(400)
    data = request.json
    message_mongo = MessageProducer(MongoDriver(host='localhost', port=27017,
                                                base=data["base"], collection=data["collection"]))
    message_mongo.update_message(message=data["data"], new_value=data["set"])
    return jsonify({"result": "OK"})


@app.route('/api/v1/database/delete', methods=['POST'])
def message_delete():
    if not request.json or not 'data':
        abort(400)
    data = request.json
    message_mongo = MessageProducer(MongoDriver(host='localhost', port=27017,
                                                base=data["base"], collection=data["collection"]))
    message_mongo.delete_message(message=data["data"])
    return jsonify({"result": "OK"})


if __name__ == '__main__':
    app.run(port=9002)
