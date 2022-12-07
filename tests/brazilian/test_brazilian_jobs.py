from src.pre_built.brazilian_jobs import read_brazilian_file

path = "tests/mocks/brazilians_jobs.csv"


def test_brazilian_jobs():
    assert read_brazilian_file(path)[0] == {
        "title": "Maquinista",
        "salary": "2000",
        "type": "trainee",
    }

    assert read_brazilian_file(path)[1] == {
        "title": "Motorista",
        "salary": "3000",
        "type": "full time",
    }

    assert read_brazilian_file(path)[2] == {
        "title": "Analista de Software",
        "salary": "4000",
        "type": "full time",
    }
