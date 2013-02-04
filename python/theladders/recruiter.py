class Recruiter:
    def __init__(self, identifier, name):
        self.identifier = identifier
        self.name = name

    def has_identity(self, recruiter):
        return self.identifier == recruiter.identifier

    def __str__(self):
        return "%s" % self.name
