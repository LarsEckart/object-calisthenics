from theladders.collection import Collection

class SavedJobs (Collection):
    def by_jobseeker(self, jobseeker):
        return self.filter(lambda saved_job: saved_job.saved_by(jobseeker)


class SavedJob:
    def __init__(self, jobseeker, job):
        self.jobseeker = jobseeker
        self.job = job

    def saved_by(self, jobseeker):
        return self.jobseeker.has_identity(jobseeker)
