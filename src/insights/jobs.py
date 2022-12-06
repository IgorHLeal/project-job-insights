from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf8") as file:
        reader = csv.DictReader(file, delimiter=',', quotechar='"')
        data_job = list(reader)
        return data_job


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    list_jobs = set()
    for job in jobs:
        list_jobs.add(job["job_type"])
    return list_jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    list_job_type = [job for job in jobs if job["job_type"] == job_type]
    return list_job_type
