class Person:
    def __init__(self, first_name: str, last_name: str, hobbies: list):
        self.first_name = first_name
        self.last_name = last_name
        self.hobbies = hobbies

    @property
    def full_name(self):
        return f"{self.first_name}{self.last_name}"  # Eemaldame tühiku

    def __repr__(self):
        return self.full_name

def filter_by_hobby(people_list: list, hobby: str) -> list:
    return [person for person in people_list if hobby in person.hobbies]

def sort_by_most_hobbies(people_list: list) -> list:
    return sorted(people_list, key=lambda person: (-len(person.hobbies), person.full_name))

def sort_by_least_hobbies(people_list: list) -> list:
    return sorted(people_list, key=lambda person: (len(person.hobbies), person.full_name))

def sort_people_and_hobbies(people_list: list) -> list:
    people_list_sorted = sorted(people_list, key=lambda person: person.full_name)
    
    for person in people_list_sorted:
        person.hobbies = sorted(person.hobbies)

    return people_list_sorted
