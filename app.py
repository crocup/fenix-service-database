from bson import ObjectId
from flask import Flask
import config
from database import MessageProducer, MongoDriver

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)


@app.route('/', methods=['GET'])
def hello_world():
    message_mongo = MessageProducer(MongoDriver(host='localhost', port=27017, base="test", collection="test"))
    message_mongo.insert({'name': 'test5'})
    message_mongo.update({'_id': ObjectId('603e1e87e665a10ae2a87b3e')}, {'name': 'test543785683476'})
    message_mongo.delete({'_id': ObjectId('603e1e87e665a10ae2a87b3e')})
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=9002)
