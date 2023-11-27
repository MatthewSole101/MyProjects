class Person:
    def speak(self):
        print('I can speak')
class Man(Person):
    def wear(self):
        print('I wear a shirt')
class Woman(Person):
    def wear(self):
        print('I wear a skirt')




man = Man()

man.wear()
man.speak()