import unittest
import datetime

class TestStringMethods(unittest.TestCase):
      
    def setUp(self):
        pass

    def test_symbol_check_upper(self):
        self.symbol = 'GME'
        self.assertTrue(self.symbol.isupper(), msg="Symbol should be uppercase")
    def test_symbol_char(self):
        self.symbol = 'abc'
        self.assertTrue(self.symbol.isalpha(), msg="Symbol should be alpha characters")
    def test_chart_type(self):
        self.chart_type = 1
        self.assertIn(self.chart_type,[1,2])
    def test_time_series(self):
        self.time_series = 4
        self.assertIn(self.time_series,[1,2,3,4])
    def test_start_date(self):
        self.date = datetime.date(2022, 7, 22)
        tday = datetime.date.today()
        self.assertEqual(self.date, tday)
    def test_end_date(self):
        self.date = datetime.date(2022, 7, 22)
        tday = datetime.date.today()
        self.assertEqual(self.date, tday)



   
if __name__ == '__main__':
    unittest.main()