import unittest
from app import app
from faker import Faker

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_sum(self):
        fake = Faker()
        num1 = fake.random_number(digits=3)
        num2 = fake.random_number(digits=3)
        payload = {'num1': num1, 'num2': num2}
        response = self.app.post('/sum', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], num1 + num2)

    def test_negative_sum(self):
        fake = Faker()
        num1 = -5
        num2 = -10
        payload = {'num1': num1, 'num2': num2}
        response = self.app.post('/sum', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], num1 + num2, "The result of -5 + -10 should be -15")

if __name__ == '__main__':
    unittest.main()