from models.plant import Plant
from models.employee import Employee


class NoneChoice(Exception):
    pass

class Controller:

    def __init__(self, menu_flag=None):
        self.menu_flag = menu_flag

    def start(self):
        print(
            "Choose a menu item by number: \n" +
              "1. Add new Plant \n" +
              "2. Add new Employee \n" +
              "3. Get plant by id \n" +
              "4. Get employee by id \n " +
              "5. Get id by gmail \n"
              )
        self.menu_flag = int(input("Yoer choose: "))

        try:
            if self.menu_flag == 1:
                self.add_new_plant()
            if self.menu_flag == 2:
                self.add_new_empl()
            if self.menu_flag == 3:
                self.get_plant_id()
            if self.menu_flag == 4:
                self.get_embl_id()
            if self.menu_flag == 5:
                self.get_id_email()
        except NoneChoice:
            print("There is no such choice in the menu!!!")

    def add_new_plant(self):
        id = int(input("ID: "))
        location = input("Location: ")
        name = input("Name: ")
        director_id = int(input("Director ID: "))
        plant = Plant(id, location, name, director_id)
        plant.save()

    def add_new_empl(self):
        id = int(input("ID: "))
        name = input("Name: ")
        email = input("Email: ")
        department_type = input("Department Type: ")
        department_id = int(input("Department id: "))
        employee = Employee(id, name, email, department_type, department_id)
        employee.save()

    def get_plant_id(self):
        id = int(input("ID: "))
        plant = Plant.get_by_id(id)
        print(plant)

    def get_embl_id(self):
        id = int(input("ID: "))
        employee = Employee.get_by_id(id)
        print(employee)

    def get_id_email(self):
        email = (input("Email: "))
        id = Employee.get_id_with_gmail(email)
        print("ID of this user: ", id)


