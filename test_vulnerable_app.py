import unittest
from vulnerable_app import insecure_crypto

class TestVulnerableApp(unittest.TestCase):
    def test_crypto_exists(self):
        # A simple test to ensure the code runs and the function returns a value
        result = insecure_crypto()
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()