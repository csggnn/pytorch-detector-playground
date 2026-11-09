import pytest
from dsl import SortingLine
from driver import Sam3Driver

@pytest.fixture(scope="session")
def sorting_line():
    return SortingLine(Sam3Driver())
