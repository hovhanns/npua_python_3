class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count+=1

    def say_hello(self, person):
        print(f"hello {person} my name is {self.name}")

    def __str__(self):
        print("STR called")
        return f"Converted {self.name}"
    def __repr__(self):
        self.__str__()



a = Student("John")
# print(a.name)
# a.say_hello("Hakob")
# print(Student.count)
# print(a.count)
c = str(a)
print(a.__str__())