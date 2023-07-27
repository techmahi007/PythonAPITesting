import pytest

# Test case code must be written inside a method
# Method name must start with 'test'

#a = 101
actual = "Testing"

# Decorator
#@pytest.mark.skipif(a>100, reason="Skipped because this functionality is not working...")
def test_Login_Logout_testing():
    print("This is start of testing...")
    print("This is end of testing")
    assert  actual == "Hello", "These two values must be same"

@pytest.mark.TopPriority
def test_Login_Logout_invalid_credentials():
    print("This is 3rd test case")
    print("This is end of testing")

# print statement output display on console :  -s
# Verbose mode - display test cases name with status :  -v
# execute only a specific test case :  -k (nameOfTestcase) (nameOfFolder)
# execute test cases using any tag :  -m