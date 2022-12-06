from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    industries = set()
    for industry in data:
        if industry["industry"] != "":
            industries.add(industry["industry"])
    list_industries = list(industries)
    return list_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    list_industry = [job for job in jobs if job["industry"] == industry]
    return list_industry
