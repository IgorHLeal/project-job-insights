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
    min_salary = job.get("min_salary")
    max_salary = job.get("max_salary")

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("min_salary ou max_salary ausentes no dicionário")

    if type(min_salary) is not int or type(max_salary) is not int:
        raise ValueError("min_salary ou max_salary tem valores não-numéricos")

    if int(min_salary) > int(max_salary):
        raise ValueError("min_salary é maior que o valor de max_salary")

    if not str(salary).lstrip("-").isdigit():
        raise ValueError("salary tem valores não numéricos")

    return int(min_salary) <= int(salary) <= int(max_salary)


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
