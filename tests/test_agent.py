import pytest
from agent.run import target_path


def test_project_file_allowed():
    assert target_path("projects/example.py").name == "example.py"


@pytest.mark.parametrize("name", ["../x.py", "agent/run.py", "projects/../../x.py", "projects/script.sh"])
def test_bad_paths_rejected(name):
    with pytest.raises(ValueError):
        target_path(name)
