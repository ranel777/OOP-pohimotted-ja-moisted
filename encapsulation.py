"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name: str, student_id: int):
        self.__name = name
        self.__id = student_id
        self.__status = "Active"
            
    def get_id(self) -> int:
            return self.__id
        
    def set_name(self, name: str):
            self.__name = name
            
    def get_name(self) -> str:
        return self.__name
    
    def get_status(self, status: str):
        valid_statuses = {"Active", "Expelled", "Finished", "Inactive"}
        if status in valid_statuses:
            self.__status = status
    
    def get_status(self) -> str:
        return self.__status
            

