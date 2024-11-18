# ## access modifiers

# class Person:
#     def __init__(self, name, age, ssn):
#         self.name = name          # Public attribute
#         self._age = age           # Protected attribute
#         self.__ssn = ssn          # Private attribute

#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self._age}, SSN: {self.__ssn}")

#     def get_ssn(self):
#         return self.__ssn
    
# class Employee(Person):
#     def display_protected_attribute(self):
#         print(self._age)


# # Create an instance of Person
# # person = Person("John Doe", 30, "123-45-6789")

# emp = Employee("John Doe", 30, "123-45-6789")
# emp.display_protected_attribute()
# print(emp._age, emp._Person__ssn)
# # print(person._Person__ssn)  # Output: 123-45-6789

# # print(person.name)  # Output: John Doe
# # print(person._age)  # Output: 30
# # # print(person.__ssn)  # Uncommenting this line will raise an AttributeError
# # print(person.get_ssn())  # Output: 123-45-6789
# # # Accessing private attribute using name mangling
# # print(person._Person__ssn)  # Output: 123-45-6789




## oop intruduction
## class and object

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def walk(self):
#         print(f"{self.name} is walking")
    
#     def talk(self):
#         print(f"{self.name} is talking")

# # inheritence example
# class Dog(Animal):
#     def __init__(self, name, weight):
#         super().__init__(name)
#         # Animal.__init__(self, name)
#         self.weight = weight

#     def talk(self):
#         print(f"{self.name} is talking, and weight is {self.weight} kg")

#     def __str__(self):
#         return f"Name: {self.name}, Weight: {self.weight}"

# d  = Dog("Tommy", 15)
# d.walk()
# print(str(d))
# # d.talk()
# # print(d)

# # # print mro
# print(Dog.mro())


## multiple inheritence

class A(object):
    def __init__(self,a):
        self.a=a

class B(A):
    def __init__(self,b,**kw):
        self.b=b
        super(B,self).__init__(**kw)

class C(A):
    def __init__(self,c,**kw):
        self.c=c
        super(C,self).__init__(**kw)

class D(B,C):
    def __init__(self,a,b,c,d):
        super(D,self).__init__(a=a,b=b,c=c)
        self.d=d

#print(D.mro())

d = D(1,2,3,4)

print(d.a, d.b, d.c, d.d)
