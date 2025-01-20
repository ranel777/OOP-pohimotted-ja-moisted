"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    


if __name__ == '__main__':
    empty_object = Empty()
    print(empty_object)
    
    p1 = Person()
    p1.firstname = "Ivan"
    p1.lastname = "Kook"
    p1.age = "56"
    
    p2 = Person()
    p2.firstname = "Karl"
    p2.lastname = "Kuur"
    p2.age = "23"
    
    p3 = Person()
    p3.firstname = "Opel"
    p3.lastname = "Astra"
    p3.age = "28"
    
    print(f"{p1.firstname} {p1.lastname}, Age: {p1.age}")
    print(f"{p2.firstname} {p2.lastname}, Age: {p2.age}")
    print(f"{p3.firstname} {p3.lastname}, Age: {p3.age}")

    s1 = Student("Debug", "Metssiga", 32)
    s2 = Student("Test", "Lammas", 22)
    s3 = Student("Test", "Lehm", 21)
    
    print(f"{s1.firstname} {s1.lastname}, Age: {s1.age}")
    print(f"{s2.firstname} {s2.lastname}, Age: {s2.age}")
    print(f"{s3.firstname} {s3.lastname}, Age: {s3.age}")

