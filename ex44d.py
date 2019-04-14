

class Parent:

    def override(self):
        print("PARENT override()")
    def implicit(self):
        print("PARENT implicit()")
    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, before parent altered()")
        super(Child, self).altered()
        print("CHILD, after parent altered()")


dad = Parent()
child = Child()

dad.implicit()
child.implicit()

dad.override()
child.override()

dad.altered()
child.altered()

