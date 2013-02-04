class FullName:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        return self

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Name:
    def __init__(self, name_string):
        self.name = name_string

    def __str__(self):
        return self.name
