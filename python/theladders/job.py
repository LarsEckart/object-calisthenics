from theladders.collection import Collection

class Jobs (Collection):
    def by_recruiter(self, recruiter):
        return self.filter(lambda job : job.from_recruiter(recruiter))


class Job:
    def __init__(self, identifier, data):
        self.identifier = identifier
        self.data = data

    def __str__(self):
        return "%s" % self.data

    def from_recruiter(self, recruiter):
        return self.data.is_from_recruiter(recruiter)


class JreqJob (Job):
    def validate_application(self, jobseeker_application):
        if not jobseeker_appliation.has_resume():
            raise MissingResumeError


class AtsJob (Job):
    def validate_application(self, jobseeker_application):
        pass


class Data:
    def __init__(self, recruiter, title):
        self.recruiter = recruiter
        self.title = title

    def __str__(self):
        return "%s" % self.title

    def is_from_recruiter(self, recruiter):
        return self.recruiter.has_identity(recruiter)

class Title:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title


def MissingResumeError ():
    def __init__(self, job, job_application):
        super(MissingResumeException, self)
        self.job = job
        self.job_application = job_application
