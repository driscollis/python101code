class Person(object):
    """"""
    
    def __init__(self, first_name, last_name):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        """
        Return the full name
        """
        return "%s %s" % (self.first_name, self.last_name)
    
if __name__ == "__main__":
    person = Person("Mike", "Driscoll")
    print(person.full_name)
    print(person.first_name)
    person.first_name = "Dan"
    print(person.full_name)