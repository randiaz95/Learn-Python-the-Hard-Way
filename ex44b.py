

class Parent:
    def override(self):
        print("PARENT Override()")

class Child(Parent):
    def override(self):
        print("CHILD Override()")

dad = Parent()
child = Child()

dad.override()
child.override()
