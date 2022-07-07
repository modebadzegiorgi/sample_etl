from sample_etl import __version__
from sample_etl.main import addition


def test_version():
    assert __version__ == "0.1.0"


def test_addition():
    assert addition(2, 2) == 4
