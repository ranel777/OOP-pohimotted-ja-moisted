class Course:
    """
    Kursus, kus õpilased saavad hindeid.
    """
    def __init__(self, name: str):
        """
        Konstruktor kursuse loomiseks.
        
        :param name: Kursuse nimi
        """
        self.name = name
        self.grades = []

    def add_student_grade(self, student: 'Student', grade: int):
        """
        Lisab õpilase hinde kursusele.
        
        :param student: Õpilane, kellele hinne lisatakse
        :param grade: Hinne
        """
        self.grades.append((student, grade))

    def get_grades(self) -> list:
        """
        Tagastab kõik kursuse tulemused.
        
        :return: Kursuse tulemused (õpilased, hinded)
        """
        return self.grades

    def get_average_grade(self) -> float:
        """
        Arvutab kursuse keskmise hinde. Kui hinnet pole, tagastatakse -1.
        
        :return: Kursuse keskmine hinne
        """
        if not self.grades:
            return -1
        total = sum(grade for _, grade in self.grades)
        return total / len(self.grades)

    def __repr__(self):
        """
        Tagastab kursuse nime.
        
        :return: Kursuse nimi
        """
        return self.name

class School:
    """
    Kool, mis haldab õpilasi ja kursuseid.
    """
    def __init__(self, name: str):
        """
        Konstruktor, mis loob kooli nime ja alustab õpilaste ning kursuste hoidmisega.
        
        :param name: Koolide nimi
        """
        self.name = name
        self.students = []
        self.courses = []

    def add_course(self, course: 'Course'):
        """
        Lisab kursuse kooli. Kui kursus on juba olemas, siis ei lisata uuesti.
        
        :param course: Kursus, mida kooli lisatakse
        """
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student: 'Student'):
        """
        Lisab õpilase kooli ja määrab talle unikaalse ID, kui õpilast pole veel lisatud.
        
        :param student: Õpilane, keda kooli lisatakse
        """
        if student not in self.students:
            self.students.append(student)
            student.set_id(len(self.students))

    def add_student_grade(self, student: 'Student', course: 'Course', grade: int):
        """
        Lisab õpilasele hinne kursusel. Hinne lisatakse ainult siis, kui õpilane ja kursus on olemas.
        
        :param student: Õpilane, kellele hinnet lisatakse
        :param course: Kursus, millele hinne lisatakse
        :param grade: Hinne, mida õpilane saab kursuse eest
        """
        if student in self.students and course in self.courses:
            student.add_grade(course, grade)
            course.add_student_grade(student, grade)

    def get_students(self) -> list:
        """
        Tagastab järjendi kõigist õpilastest.
        
        :return: Õpilaste nimekiri
        """
        return self.students

    def get_courses(self) -> list:
        """
        Tagastab järjendi kõigist kursustest.
        
        :return: Kursuste nimekiri
        """
        return self.courses

    def get_students_ordered_by_average_grade(self) -> list:
        """
        Tagastab õpilaste järjendi järjestatuna keskmise hinde järgi.
        
        :return: Õpilased järjestatuna keskmise hinde järgi
        """
        return sorted(self.students, key=lambda student: student.get_average_grade(), reverse=True)


class Student:
    """
    Õpilane, kellel on nimi, ID ja hinnete nimekiri.
    """
    def __init__(self, name: str):
        """
        Konstruktor, mis loob õpilase nimega ja määrab alguses ID väärtuseks None.
        
        :param name: Õpilase nimi
        """
        self.name = name
        self.grades = []
        self.student_id = None

    def set_id(self, student_id: int):
        """
        Määrab õpilasele ID ainult siis, kui ID on veel määramata.
        
        :param student_id: Õpilase unikaalne identifikaator
        """
        if self.student_id is None:
            self.student_id = student_id

    def get_id(self) -> int:
        """
        Tagastab õpilase ID.
        
        :return: Õpilase ID või -1, kui ID ei ole määratud
        """
        return self.student_id if self.student_id is not None else -1

    def add_grade(self, course: 'Course', grade: int):
        """
        Lisab õpilasele hinne kursuse kohta.
        
        :param course: Kursus, millele hinne lisatakse
        :param grade: Hinne, mida õpilane saab kursusel
        """
        self.grades.append((course, grade))

    def get_grades(self) -> list:
        """
        Tagastab õpilase tulemused (kursus, hinne).
        
        :return: Õpilase tulemused (kursus, hinne)
        """
        return self.grades

    def get_average_grade(self) -> float:
        """
        Tagastab õpilase keskmise hinde. Kui õpilasel pole hindepunkte, tagastatakse -1.
        
        :return: Õpilase keskmine hinne
        """
        if not self.grades:
            return -1
        total = sum(grade for _, grade in self.grades)
        return total / len(self.grades)

    def __repr__(self) -> str:
        """
        Tagastab õpilase nime.
        
        :return: Õpilase nimi
        """
        return self.name
