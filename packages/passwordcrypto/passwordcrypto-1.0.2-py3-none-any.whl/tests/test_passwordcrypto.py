import unittest

import importlib.util
import sys
spec = importlib.util.spec_from_file_location("passwordcrypto", "passwordcrypto/passwordcrypto.py")
passwordcrypto = importlib.util.module_from_spec(spec)
sys.modules["passwordcrypto"] = passwordcrypto
spec.loader.exec_module(passwordcrypto)

class TestPasswd(unittest.TestCase):
    def setUp(self):
        # Set up any necessary objects or data before each test case
        self.test_pass_file = "testPasswords.txt"
        self.test_key = b"12345"
        self.testPasswd = passwordcrypto.Passwd(self.test_pass_file, self.test_key)

    def test_read(self):
        # Ensure that the read method returns the expected result
        expected_result = [['testApp', 'testEmail', 'testPassword']]
        actual_result = self.testPasswd.read()
        self.assertEqual(actual_result, expected_result)
