class Animal(object):
    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound
    def speak(self,):
            print(f"{self.name} makes a   { self.sound} sound")
   def __str__(self):
    return f"{self.name}, {self.type} { self.sound}"
# creating animal objects
# Animal1=Animal("Animal", "cat", "woman")
# print(Animal1)
# Animal2=Animal("Animal", "dog", "dog")
# print(Animal2)
# Animal3=Animal("Animal", "cow", "cow")
# print(Animal3)
    def speak(self):
        return f" A {self.name} barks!"
class Dog(Animal):
    def __init__(self, name, type, sound, breed):
        super().__init__(name, type, sound)
dog1=Dog("Dog", "Domestic", "Woof!","German Shepherd")
print(dog1)
print(dog1)
print (dog1.speak())