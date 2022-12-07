from src.pre_built.counter import count_ocurrences
import pytest


def test_counter():
    assert count_ocurrences("data/jobs.csv", "python") == 1639


with pytest.raises(FileNotFoundError):
    count_ocurrences("data/java.java", "Java")
