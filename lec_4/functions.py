def say_hello(name, age=0):
    s = f"Hello, {name}"
    next_age = age + 20
    surname = "Doe"
    return s, next_age, surname

s, age = say_hello("John", 30)
print(s)
print(age)

