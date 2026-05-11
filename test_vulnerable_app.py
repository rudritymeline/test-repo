import unittest
from vulnerable_app import hash_password

class TestApp(unittest.TestCase):
    def test_hash_password(self):
        # Testing the hash function to provide coverage with MD5 32 characters
        result = hash_password("password123")
        self.assertEqual(len(result), 32)  

if __name__ == "__main__":
    unittest.main()