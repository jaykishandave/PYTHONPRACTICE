import pytest


@pytest.mark.login
def test_m1():
    name = "selenium"
    assert name == name.upper()


def test_m2():
    assert True


@pytest.mark.login
def test_m3():
    assert False


def test_m4():
    assert 100 == 100


@pytest.mark.login
def test_m5():
    assert "jay" == "jay"


def test_m6():
    print("Hello World")


@pytest.mark.login
def test_login():
    assert "admin" == "admin"
