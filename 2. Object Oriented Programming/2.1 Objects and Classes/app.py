class Animal:
    name = "Dog"

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def test(self):
        print("Iam working fine")



obj = Animal(5, "Vera")
obj.test()
