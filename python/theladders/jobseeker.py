class Jobseeker:
    def __init__(self, identifier, name):
        self.identifier = identifier
        self.name = name

    def has_identity(self, jobseeker):
        return self.identifier == jobseeker.identifier

    def __str__(self):
        return "%s" % self.name
