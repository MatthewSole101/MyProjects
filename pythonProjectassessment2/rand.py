class Student(object):
    age = ''
    name = ''
    def __int__(self, n, a):
        self.name = n
        self.age = a
    def get_age(self):
        return self.age

inp = input('What is your name?: ')

mystudent = Student(inp, 56)

print(mystudent)



