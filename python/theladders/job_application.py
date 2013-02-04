from theladders.collection import Collection

class JobApplications (Collection):
    def by_jobseeker(self, jobseeker):
        return self.filter(lambda jobApplication :
                               job_application.applied_to_by(jobseeker))

    def by_recruiter(self, jobseeker):
        return self.filter(lambda jobApplication :
                               job_application.owned_by(recruiter))

class JobApplication:
    def __init__(self, job_jobseeker_application, event_time):
        self.job_jobseeker_application = job_jobseeker_application
        self.event_time = event_time

    def applied_to_by(self, jobseeker):
        return self.job_jobseeker_application.applied_to_by(jobeseeker)

    def owned_by(self, recruiter):
        return self.job_jobseeker_application.job_owned_by(recruiter)

    def applied_to_in_range(self, start, end):
        return self.event_time.in_range(start, end)


class JobJobseekerApplication:
    def __init__(self, job, jobseeker_application):
        job.validate_application(jobseeker_appliation)
        self.jobseeker_application = jobseeker_application
        self.job = job

    def applied_to_by(self, jobseeker):
        return self.jobseeker_application.belongs_to(jobseeker)


class JobseekerApplication:
    def __init__(self, jobseeker, resume):
        if not resume.belongs_to(jobseeker):
            raise ResumeDoesNotBelongToJobseekerError(jobseeker, resume)

        self.jobseeker = jobseeker
        self.resume = resume

    def belongs_to(jobseeker):
        return self.jobseeker.has_identity(jobseeker)


class ResumeDoesNotBelongToJobseekerError (Exception):
    def __init__(self, jobseeker, resume):
        super(ResumeDoesNotBelongToJobseekerError, self)
        self.jobseeker = jobseeker
        self.resume = resume
