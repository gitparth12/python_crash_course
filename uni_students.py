class Student:
    def __init__(self, name: str, unikey: str, units: list = None):
        # instance variables
        self.name = name
        self.unikey = unikey
        if units is None:
            self.units = []
        else:
            self.units = units

    def add_unit(self, unit: str):
        self.units.append(unit)


class Uni:
    # class attribute
    location = "Sydney"

    def __init__(self, name: str, all_students: list = None):
        # instance attributes
        self.all_students = [] if all_students is None else all_students
        self.name = name

    def add_student(self, student: Student):
        self.all_students.append(student)

    def print_students(self):
        for student in self.all_students:
            print(
                "{} has {} units and their unikey is {}".format(
                    student.name, len(student.units), student.unikey
                )
            )
    


if __name__ == "__main__":
    usyd = Uni("University of Sydney")
    usyd.add_student(Student("John", "jfni8484"))
    mary = Student("Mary", "mfkd01293", ["info1110", "info1113", "elec1601"])
    usyd.add_student(mary)

    unsw = Uni("University of New South Wales")

    usyd.print_students()
