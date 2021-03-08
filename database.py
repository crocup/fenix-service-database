from abc import ABC, abstractmethod
from typing import Dict
from pymongo import MongoClient
import logging


class Driver(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def insert(self, message):
        pass

    @abstractmethod
    def delete(self, message):
        pass

    @abstractmethod
    def update(self, message, new_values):
        pass


class MongoDriver(Driver):
    def __init__(self, host, port, base, collection):
        self.client = MongoClient(host, port)
        self.base = self.client[base]
        self.collection = self.base[collection]

    def connect(self):
        self._conect_to_mongo()

    def _conect_to_mongo(self):
        logging.info('Connect to mongo')

    def disconnect(self):
        self._disconnect_from_mongo()

    def _disconnect_from_mongo(self):
        self.client.close()
        logging.info('Disconnect from mongo')

    def insert(self, message):
        self._insert_message(message)

    def _insert_message(self, message):
        self.collection.insert_one(message)
        logging.info(f'Inserted: {message}')

    def delete(self, message):
        self._delete_message(message)

    def _delete_message(self, message):
        self.collection.delete_one(message)
        logging.info(f'Deleted: {message}')

    def update(self, message, new_value):
        self._update_message(message, new_value)

    def _update_message(self, message, new_value):
        self.collection.update_one(message, {'$set': new_value})
        logging.info(f'Updated: {message}')


class Producer(ABC):
    def __init__(self, driver: Driver):
        self.driver = driver

    @abstractmethod
    def insert(self, message: Dict):
        pass

    @abstractmethod
    def delete(self, message: Dict):
        pass

    @abstractmethod
    def update(self, message: Dict, new_value: Dict):
        pass


class MessageProducer(Producer):

    def insert(self, message: Dict):
        self.driver.connect()
        self.driver.insert(message)
        self.driver.disconnect()

    def delete(self, message: Dict):
        self.driver.connect()
        self.driver.delete(message)
        self.driver.disconnect()

    def update(self, message: Dict, new_value: Dict):
        self.driver.connect()
        self.driver.update(message, new_value)
        self.driver.disconnect()
