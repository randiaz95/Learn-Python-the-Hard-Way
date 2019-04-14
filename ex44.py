

class Parent:
    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
child = Child()

dad.implicit()
child.implicit()
