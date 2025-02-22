from abc import ABC, abstractmethod
import json


class Model(ABC):
    file = 'default.json'

    def save(self):
        info_in_dict_format = self._generate_dict()
        info = self.get_file_data(self.file)
        info.append(info_in_dict_format)
        self.save_to_file(info)

    def _generate_dict(self):
        return self.__dict__
#   return{self_vales: getattr(self, select_values) for select_values in self.__dict__}

    @classmethod
    def get_by_id(cls, id):
        data = cls.get_file_data(cls.file)
        for el in data:
            if el['id'] == id:
                return el

        raise Exception("Not found")

    @classmethod
    def get_id_with_gmail(cls, email):
        data = cls.get_file_data(cls.file)
        for el in data:
            if el["email"] == email:
                return el["id"]

    @classmethod
    def get_all(cls):
        data = cls.get_file_data(cls.file)
        return data

    @staticmethod
    def get_file_data(file_name):
        file = open("database/" + file_name, 'r')
        data = json.loads(file.read())
        file.close()
        return data

    def save_to_file(self, data):
        data = json.dumps(data)
        file = open('database/' + self.file, "w")
        file.write(data)
        file.close()
