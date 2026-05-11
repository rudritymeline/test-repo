import unittest
from vulnerable_app import hash_password

class TestApp(unittest.TestCase):
    def test_hash_password(self):
        # Testing the hash function to provide coverage
        result = hash_password("password123")
        self.assertEqual(len(result), 32)  # MD5 is 32 chars

if __name__ == "__main__":
    unittest.main()