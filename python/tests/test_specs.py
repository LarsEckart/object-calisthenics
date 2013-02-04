from theladders.name import Name, FullName
from theladders.identifier import Identifier
from theladders.job import Jobs, JreqJob, AtsJob, Data, Title
from theladders.recruiter import Recruiter

def test_recruiters_can_post_jobs():
    jobs = Jobs()

    recruiter = create_recruiter_named("Adam", "Recruiter")
    
    job1 = create_job_for_recruiter(JreqJob, recruiter, "job1")
    job2 = create_job_for_recruiter(AtsJob, recruiter, "job2")

    jobs.add([job1, job2])

    display = jobs.display()

    assert(display[0] == "job1" and display[1] == "job2")

def test_recruiters_should_be_able_to_see_a_list_of_jobs_they_have_posted():
    jobs = Jobs()

    recruiter1 = create_recruiter_named("Adam", "Recruiter")
    recruiter2 = create_recruiter_named("Beth", "Wrangler")
    
    job1 = create_job_for_recruiter(JreqJob, recruiter1, "job1")
    job2 = create_job_for_recruiter(AtsJob, recruiter1, "job2")
    job3 = create_job_for_recruiter(AtsJob, recruiter2, "job3")
    job4 = create_job_for_recruiter(AtsJob, recruiter2, "job4")

    jobs.add([job1, job2, job3, job4])

    recruiter1_jobs = jobs.by_recruiter(recruiter1)
    display = recruiter1_jobs.display()

    assert(display[0] == "job1" and display[1] == "job2")

def test_jobseekers_can_save_jobs_onsite_for_later_viewing():
    saved_jobs = SavedJobs()

    recruiter1 = create_recruiter_named("Adam", "Recruiter")
    recruiter2 = create_recruiter_named("Beth", "Wrangler")
    
    job1 = create_job_for_recruiter(JreqJob, recruiter1, "job1")
    job2 = create_job_for_recruiter(AtsJob, recruiter1, "job2")
    job3 = create_job_for_recruiter(AtsJob, recruiter2, "job3")
    job4 = create_job_for_recruiter(AtsJob, recruiter2, "job4")

    jobseeker = create_jobseeker_named(first_name, last_name)

    

def create_recruiter_named(first_name, last_name):
    first_name = Name(first_name)
    last_name = Name(last_name)

    name = FullName(first_name, last_name)
    identifier = Identifier()

    return Recruiter(identifier, name)

def create_job_for_recruiter(job_class, recruiter, title):
    title = Title(title)
    data = Data(recruiter, title)
    identifier = Identifier()
    return job_class(Identifier, data)

def create_jobseeker_named(first_name, last_name):
    first_name = Name(first_name)
    last_name = Name(last_name)

    name = FullName(first_name, last_name)
    identifier = Identifier()

    return Jobseeker(identifier, name)
