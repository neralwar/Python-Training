# pytest name should start from 
        #1. test_*
        #2. _test*
#Test Function should start from
        #1. test_

#pytest_dependency :  @pytest.mark.dependency(depends=["<TestName>"])

#pytest distributed plug-in is used for parallel test execution
#import pytest_dependency
#How to delected the test case : with option -k e.g pytest -k "not <test case name>" -v
# Pytest fixutre is used can run before each test
#@pytest.fixture(scope="module")  -- If you want to execute code once before test

import pytest
import warnings

warnings.warn(UserWarning("api v1, should use functions from v2"))

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 12*num == output

#warnings.WarningMessage("TEST WARNING")
@pytest.mark.xfail
def test_nine():
   pass

@pytest.fixture
def input_value():
   input = 30
   return input

def test_divisible_by_3(input_value):
  # print("INPUT VALUE:-"+input_value)
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0


@pytest.mark.smoke
def test_3():
    assert 7*7==49

def test_2():
    assert 7*7==49

def test_first():
    assert 7*7==49

def test_1():
    assert 7*7==49

@pytest.mark.skip(reason="ABSOLUTE")
def test_second():
    assert 7+7==49

@pytest.mark.dependency(depends=["test_first"])
def test_third():
    assert 7*7==49

def test_fifth():
    assert 7*7==49
