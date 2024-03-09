import os
import sys

# Adding the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ..sensitiveInfoDetector.main import detect_secrets


def test_sensitive_info():
    example_string = "String contains Username"
    assert (detect_secrets(example_string) == True)


def test_no_sensitive_info():
    example_string = "String does not contain sensitive data"
    assert detect_secrets(example_string) == False


def test_no_data():
    example_string = " "
    assert detect_secrets(example_string) == False


# Output : Test case passed
