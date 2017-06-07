# class Parent1:        # define parent class
#    def __init__(self):
#       print ("Calling parent1 constructor")

#    def ethod(self):
#       print ("Calling parent1 method")

# class Parent2:
#    def __init__(self):
#       print ("Calling parent2 constructor")

#    def method(self):
#       print ("Calling parent2 method")

# class Child(Parent1, Parent2): # define child class
#    def __init__(self):
#       super(Child, self).__init__()
#       self.__string = "Sample String"
#       print ("Calling child constructor")

#    def method(self):
#       super(Child, self).method()
#       print ("Calling child method")

# c = Child()          # instance of child
# c.method()
# c.method()
# c.method()

class First():
    def __init__(self):
        print ("first")

    def save(self):
        print ("first save")

class First3rd():
    def __init__(self):
        print ("First3rd")

    def save(self):
        print ("first3rd save")

class Second(First):
    def __init__(self):
        print ("second")
        super(Second, self).__init__()

    def save(self):
        print ("second save")
        super(Second, self).save()

class Third(First3rd):
    def __init__(self):
        print ("third")
        super(Third, self).__init__()

    def save(self):
        print ("Third save")
        super(Third, self).save()

class Fourth(Third, Second):
    def __init__(self):
        # print ("fourth")
        # super(Fourth, self).__init__()
        pass

    def save(self):
        print ("fourth save")
        super (Fourth, self).save()


if __name__ == "__main__":
    obj = Fourth()
    obj.save()