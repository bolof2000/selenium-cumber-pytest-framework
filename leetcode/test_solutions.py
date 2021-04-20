import pytest
from solutions import Solutions


# ------------------------------------------------------------------------------------------
# fixture
# ------------------------------------------------------------------------------------------
#@pytest.fixture
#def test_method_access():
    #return Solutions()

# ------------------------------------------------------------------------------------------
# Tests
# -------------------------------------------------------------------------------------------
class test_solutions:

    test_methods= Solutions()
    def test_longestPalindrome(self):
        actual_result = self.test_methods.longestPalindrome("babad")
        assert actual_result== "bab"


