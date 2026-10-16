import unittest
from unittest.mock import patch 
from employeee import Employee

class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass: Initializing test Employee instance')
        cls.emp_1 = Employee('Suryaraj', 'Jadeja', 50000)

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass: Cleaning up test Employee instance')
        del cls.emp_1

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Suryaraj.Jadeja@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Suryaraj Jadeja')

    def test_lastname(self):
        self.assertEqual(self.emp_1.last, 'Jadeja')

    def test_firstname(self):
        self.assertEqual(self.emp_1.first, 'Suryaraj')

    def test_raise(self):
        self.emp_1.apply_raise()
        self.assertEqual(self.emp_1.pay, 52000)

    def test_raise_with_amount(self):
        self.emp_1.apply_raise(1.10)
        self.assertEqual(self.emp_1.pay, 55000)

    def test_monthly_schedule(self):
        with patch('employeee.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.text = 'Business hours'
            schedule = self.emp_1.monthly_schedule('March')
            mock_get.assert_called_with('https://company.com/Office-hoursMarch')
            self.assertEqual(schedule, 'Business hours')

            schedule = self.emp_1.monthly_schedule('May')
            mock_get.assert_called_with('https://company.com/Office-hoursMay')
            self.assertEqual(schedule, 'Business hours')

        with patch('employeee.requests.get') as mock_get:
            mock_get.return_value.status_code = 404
            schedule = self.emp_1.monthly_schedule('March')
            mock_get.assert_called_with('https://company.com/Office-hoursMarch')
            self.assertEqual(schedule, 'Bad Response')

            mock_get.return_value.ok = False

if __name__ == '__main__':
    unittest.main()
