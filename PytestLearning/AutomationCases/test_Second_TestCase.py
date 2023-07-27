import pytest

# Test case code must be written inside a method
# Method name must start with 'test'

@pytest.fixture(scope="module")
def fixture_testing():
    print("\nThis fixture code will execute before the test case")
    print("-----------------------------------------------------")
    yield
    print("\nThis code will execute after the test case")
    print("-----------------------------------------------------")

def test_Registration_testing(fixture_testing):
    print("This is our 2nd test case code...")
    print("This is end of testing")

def test_Automation_testing(fixture_testing):
    print("This is our 4th test case code")
    print("This is the end of this test case")