# 1
# class Animals:
#
#     def eat(self):
#         print("Have to eat!")
#
#     def sleep(self):
#         print("Have to sleep!")
#
# class Animal1(Animals):
#     def __init__(self, type, age):
#         self.type = type
#         self.age = age
#
#     def __call__(self):
#         return print(f"Animal 1 type: {self.type}. Lives: {self.age} year.")
#
#     def jump(self):
#         print("jump forward ")
#
# class Animal2(Animals):
#     def __init__(self, type, age):
#         self.type = type
#         self.age = age
#
#     def __call__(self):
#         return print(f"Animal 1 type: {self.type}. Lives: {self.age} year.")
#
#     def speed(self):
#         print("accelerated ")
#
# class Animal3(Animals):
#     def __init__(self, type, age):
#         self.type = type
#         self.age = age
#
#     def __call__(self):
#         return print(f"Animal 1 type: {self.type}. Lives: {self.age} year.")
#
#     def crawl(self):
#         print("crawl 10 meters ")
#
# class Animal4(Animals):
#     def __init__(self, type, age):
#         self.type = type
#         self.age = age
#
#     def __call__(self):
#         return print(f"Animal 1 type: {self.type}. Lives: {self.age} year.")
#
#     def swim(self):
#         print("swims breaststroke ")
#
# class Animal5(Animals):
#     def __init__(self, type, age):
#         self.type = type
#         self.age = age
#
#     def __call__(self):
#         return print(f"Animal 1 type: {self.type}. Lives: {self.age} year.")
#
#     def hunting(self):
#         print("search for the victim")
#
# animals = Animals()
# #
# animal1 = Animal1("Rabit", 5)
#
# animal1.eat()
# animal1.sleep()
# animal1.jump()

# print(isinstance(animal1, Animals))

#1.a.
# class Human:
#     def __init__(self, study, work):
#         self.study = study
#         self.work = work
#
#     def physical_characteristics(self, height, weight):
#         self.height = height
#         self.weight = weight
#
# class Centaur(Animal1, Human):
#     def __init__(self, type, age, study, work, height, weight, clas):
#         super.__init__(type, age, study, work, height, weight)
#         self.clas = clas
#
#     def activity (self):
#         print("Protection of the fortress ")


# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
#   a.
#       class Person:
#
#         def __init__(self):
#             arm_L = Arm('This is content for page 1')
#             arm_R = Arm('This is content for page 2')
#             self.pages = [arm_L, arm_R]
#
#       class Arm:
#
#           def __init__(self, position):
#               self.position = position

#   b.
#       class CellPhone:
#             def __init__(self, screen):
#                 self.screen = screen
#
#       class Screen:
#           def __init__(self):
#               pass

# 3.
# class Profile:
#     def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
#         self.name = name
#         self.last_name = last_name
#         self.phone_number = phone_number
#         self.address = address
#         self.email = email
#         self.birthday = birthday
#         self.age = age
#         self.sex = sex
#
#     def __str__(self):
#         return f"Name and last name: {self.name} {self.last_name} \nPhone_number: {self.phone_number} " \
#                f"\nBirthday {self.birthday} \nAge: {self.age} \nSex: {self.sex} \nAddress:{self.address} \n" \
#                f"Email:\t{self.email}"
#
# profile = Profile('Jack', 'Felix', 39231294, "19510, Jamboree Road", 'jf007.gmail.com', "06.19.96", 25, 'man')
# print(profile)
#
# 4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.

# from abc import ABC, abstractmethod
#
# class Laptop(ABC):
#
#     @abstractmethod
#     def screen(self):
#         raise NotImplemented
#
#     @abstractmethod
#     def keyboard(self):
#         raise NotImplemented
#
#     @abstractmethod
#     def touchpad(self):
#         raise NotImplemented
#
#     @abstractmethod
#     def webcam(self):
#         raise NotImplemented
#
#     @abstractmethod
#     def ports(self):
#         raise NotImplemented
#
#     @abstractmethod
#     def dynamics(self):
#         raise NotImplemented
#
# class HPLaptop (Laptop):
#
#     def __init__(self, model: str):
#         self.model = model
#
#     def screen(self):
#         print(f'{self.model} has a ...')
#
#     def keyboard(self):
#         print(f'{self.model} has a ...')
#
#     def touchpad(self):
#         print(f'{self.model} has a ...')
#
#     def webcam(self):
#         print(f'{self.model} has a ...')
#
#     def ports(self):
#         print(f'{self.model} has a ...')
#
#     def dynamics(self):
#         print(f'{self.model} has a ...')
