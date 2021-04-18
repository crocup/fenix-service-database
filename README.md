<h1 align="center" style="border-bottom: none !important; margin-bottom: 5px !important;"><a href="#">Class Database</a></h1>
<p align="center">Класс для работы с базами данных (пример: Mongo)</p>
<p align="center">
Class for database operation (example: Mongo)
</p>
<p align="center">
  <a href="#">
    <img src="https://img.shields.io/github/license/crocup/Service-Database" />
  </a>
<a href="#">
    <img src="https://img.shields.io/github/last-commit/crocup/Service-Database" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/github/stars/crocup/Service-Database?style=social" />
  </a>
</p>

# About
Пример класса для работы с базами данными.
`Данный класс используется в ПО Fenix Security Scanner`

## Usage
Объявление:
```python
message_mongo = MessageProducer(MongoDriver(host='localhost', port=27017,
                                                 base="base", collection="collection"))
```

## Example
Пример использования: Получение записи из БД Mongo
```python
message_mongo = MessageProducer(MongoDriver(host='localhost', port=27017,
                                                 base="base", collection="collection"))
result = message_mongo.get_message(message={"name": "Ivan"})
```
