from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    list_salary = []
    for job in data:
        if job["max_salary"].isdigit():
            list_salary.append(int(job["max_salary"]))
    return max(list_salary)


def get_min_salary(path: str) -> int:
    data = read(path)
    list_salary = []
    for job in data:
        if job["min_salary"].isdigit():
            list_salary.append(int(job["min_salary"]))
    return min(list_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError

    if type(job["min_salary"]) is not int or type(job["max_salary"]) is not int:
        raise ValueError

    if job["min_salary"] > job["max_salary"]:
        raise ValueError

    if type(salary) is not int:
        raise ValueError

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
