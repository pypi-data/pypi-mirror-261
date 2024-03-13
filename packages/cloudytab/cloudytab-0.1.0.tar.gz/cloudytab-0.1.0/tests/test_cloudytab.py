import pytest
from cloudytab import hello


def test_always_passes():
    assert True


def test_hello():
    assert hello() == "Hello from cloudytab!"
