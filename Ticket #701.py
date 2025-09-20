class Student:
    def __init__(self, name,studant_id, grades):
        self.name = name
        self.studant_id = studant_id
        self.grades = grades
    def gpa(self,scale=4.0):
        raw=sum(self.grades)/len(self.grades)
        return round((raw/100)*scale,2)
    