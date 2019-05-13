class Bericht:
    def __init__(self, username, age):
        self.username = username
        self.age = age
        print('(Your User Name Is: {})'.format(self.username))

    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.username, self.age), end=" ")


class Teacher(Bericht):
    def __init__(self, username, age, salary): 
        Bericht.__init__(self, username, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.username))

    def tell(self):
        Bericht.tell(self)
        print('Salary: "{:d}"'.format(self.salary))


class Student(Bericht):
    def __init__(self, username, age, marks):
        Bericht.__init__(self, username, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.username))

    def tell(self):
        Bericht.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mr. Hans', 32, 60000)
s = Student('Nick Zegels', 17, 100)

print()

members = [t, s]
for member in members:
    member.tell()