class Student:

    def __init__(self, name, rollno, grade):
        self.name = name
        self.rollno = rollno
        self.grade = grade

    def isPassed(self):
        if(self.grade <= 3.5):
            return False
        else:
            return True