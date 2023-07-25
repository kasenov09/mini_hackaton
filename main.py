import json
from datab.json import *

class Database:
    def __init__(self, filename):
        # self.filename = filename
        self.data = self._load_data()

    def _load_data(self):
        # try:
            with open(datab.json, 'r') as file:
                return json.load(file)
        # except FileNotFoundError:
        #     return []

    def _save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=2)
            
    def create(self, record):
        self.data.append(record)
        self._save_data()

    def read(self, record_id=None):
        if record_id is None:
            return self.data
        for record in self.data:
            if record['id'] == record_id:
                return record
        return None

    def update(self, record_id, new_data):
        for record in self.data:
            if record['id'] == record_id:
                record.update(new_data)
                self._save_data()
                return True
        return False

    def delete(self, record_id):
        for index, record in enumerate(self.data):
            if record['id'] == record_id:
                del self.data[index]
                self._save_data()
                return True
        return False
    # def create():
    #     pass
    
    # def  read():
    #     pass
    
    def update():
        pass
    
    def delete(): 
        pass
    
    def close():
        pass
    
class Model(Database):
    super().__init__()
    pass

class View(Database):
    pass

class Controller(Database):
    pass



# class Model:
#     def __init__(self, data):
#         self.data = data

#     def validate(self):
#         # Здесь можно реализовать логику валидации данных перед добавлением в базу
#         return True

# class View:
#     @staticmethod
#     def print_records(records):
#         for record in records:
#             print(record)

#     @staticmethod
#     def print_message(message):
#         print(message)

# class Controller:
#     def __init__(self, db):
#         self.db = db

#     def create_record(self, data):
#         model = Model(data)
#         if model.validate():
#             self.db.create(data)
#             View.print_message("Запись успешно создана.")
#         else:
#             View.print_message("Ошибка валидации данных. Запись не создана.")

#     def read_records(self, record_id=None):
#         if record_id is not None:
#             record = self.db.read(record_id)
#             if record:
#                 View.print_records([record])
#             else:
#                 View.print_message("Запись не найдена.")
#         else:
#             records = self.db.read()
#             View.print_records(records)

#     def update_record(self, record_id, new_data):
#         if self.db.update(record_id, new_data):
#             View.print_message("Запись успешно обновлена.")
#         else:
#             View.print_message("Запись не найдена. Обновление не выполнено.")

#     def delete_record(self, record_id):
#         if self.db.delete(record_id):
#             View.print_message("Запись успешно удалена.")
#         else:
#             View.print_message("Запись не найдена. Удаление не выполнено.")

# # Пример использования
# if __name__ == "__main__":
#     db = Database("data.json")
#     controller = Controller(db)

#     # Создание записи
#     data1 = {"id": 1, "name": "John", "age": 30}
#     controller.create_record(data1)

#     # Просмотр всех записей
#     controller.read_records()

#     # Обновление записи
#     new_data = {"name": "John Doe", "age": 31}
#     controller.update_record(1, new_data)

#     # Просмотр одной записи по идентификатору
#     controller.read_records(1)

#     # Удаление записи
#     controller.delete_record(1)

#     # Проверка, что запись удалена
#     controller.read_records(1)
