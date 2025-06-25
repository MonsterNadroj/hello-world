class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


jordan = Person("Jordan Monster")
jordan.talk()

bob = Person("Bob Gennerddry")
bob.talk()


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("I am annoying you!")


dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.be_annoying()
