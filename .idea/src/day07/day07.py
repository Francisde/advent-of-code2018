class Job:

    def __init__(self, name):
        self.name = name
        self.jobs_after = []
        self.status = "UNKNOWN"
        self.start = 0
        self.done = 0

    def __cmp__(self, other):
        if self.name < other.name:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.name < other.name:
            return True
        else:
            return False

    def add_job_after(self, job):
        self.jobs_after.append(job)
    def begin_job(self, sec, time):
        self.start = sec
        self.done = sec + time

def solve_part_one(job_list):
    result = ""
    done_jobs = []
    doing_jobs = []
    jobs_to_do = job_list.copy()
    sec = 0
    while len(jobs_to_do) > 0:
        ready_jobs = []
        for job1 in jobs_to_do:
            ready = True
            for job2 in jobs_to_do + doing_jobs:
                if job1 != job2:
                    if job1 in job2.jobs_after:
                        ready = False
            if ready:
                job1.staus = "READY"
                ready_jobs.append(job1)
            else:
                job1.staus = "WAITING"
        ready_jobs.sort()
        jobs_to_do.remove(ready_jobs[0])
        ready_jobs[0].status = "DONE"
        result += ready_jobs[0].name
        sec += 1
    return result

def solve_part_two(job_list, worker, ground_time):
    result = ""
    done_jobs = []
    doing_jobs = []
    jobs_to_do = job_list.copy()
    time = 0
    while len(jobs_to_do + doing_jobs) > 0:
        ready_jobs = []
        for job in doing_jobs:
            if job.done <= time:
                print("time: {}, done job: {}".format(time, job.name))
                job.status = "DONE"
                doing_jobs.remove(job)
                done_jobs.append(job)
                worker += 1
                result += job.name
        for job1 in jobs_to_do:
            ready = True
            for job2 in jobs_to_do + doing_jobs:
                if job1 != job2:
                    if job1 in job2.jobs_after:
                        # print("job 1: {}, job2: {}".format(job1.name, job2.name))
                        ready = False
            if ready:
                # print("job {} ready".format(job1.name))
                job1.staus = "READY"
                ready_jobs.append(job1)
            else:
                job1.staus = "WAITING"
        ready_jobs.sort()
        while worker > 0 and len(ready_jobs) > 0:
            print("time: {}, start job: {}".format(time, ready_jobs[0].name))
            jobs_to_do.remove(ready_jobs[0])
            ready_jobs[0].status = "DOING"
            doing_jobs.append(ready_jobs[0])
            ready_jobs[0].begin_job(time, ((ord(ready_jobs[0].name) - 64) + ground_time))
            ready_jobs.remove(ready_jobs[0])
            worker -= 1

        time += 1

    return time



file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

jobs = []
job_dict = dict()

for line in Lines:
    input_line= line.strip()
    split_line = input_line.split(" ")
    job_name = split_line[1]
    job_after_name = split_line[7]
    job = None
    job_after = None
    if job_name in job_dict.keys():
        job = job_dict[job_name]
    else:
        job = Job(job_name)
        jobs.append(job)
        job_dict[job_name] = job
    if job_after_name in job_dict.keys():
        job_after = job_dict[job_after_name]
    else:
        job_after = Job(job_after_name)
        jobs.append(job_after)
        job_dict[job_after_name] = job_after
    job.add_job_after(job_after)
    print("Line {}: {}".format(count, input_line))
    count += 1


print("TASK 1 - sol: {}".format(solve_part_one(jobs)))

print("TASK 2 - sol: {}".format(solve_part_two(jobs, 5 , 60)))

print(ord("A") - 64)
