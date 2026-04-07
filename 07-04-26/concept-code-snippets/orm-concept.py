# simple class representing a table (conceptual ORM)
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

u = User("Pooja", 22)
print(u.name)