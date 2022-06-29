import pytest


def test_m1():
    name = "selenium"
    assert name == name.upper()


def test_m2():
    assert True


def test_m3():
    assert False

def test_login():
    assert "admin"=="admin"