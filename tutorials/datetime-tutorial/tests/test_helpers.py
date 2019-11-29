import unittest
import helpers
import datetime
import calendar

class TestHelpers(unittest.TestCase):

    def setUp(self):
        self.d1 = datetime.date(2011, 1, 31)
        self.d2 = datetime.date(2012, 2, 29)

    def test_add_relative(self):
        self.assertEqual(
            helpers.add_relative(self.d1, years=1, months=1),
            datetime.date(2012, 2, 29))

        self.assertEqual(
            helpers.add_relative(self.d2, years=1, months=0),
            datetime.date(2013, 2, 28))

        self.assertEqual(
            helpers.add_relative(self.d1, years=-3, months=1),
            datetime.date(2008, 2, 29))

    def test_is_leap(self):
        self.assertTrue(helpers.is_leap(2012))
        self.assertFalse(helpers.is_leap(2013))

    def test_is_feb(self):
        self.assertTrue(helpers.is_feb(self.d2))
        self.assertFalse(helpers.is_feb(self.d1))

    def test_last_day_of_month(self):
        for year, month in zip([2012, 2013, 2011], [2, 2, 7]):
            self.assertEqual(helpers.last_day_of_month(year, month),
                             calendar.monthrange(year, month)[1])


    def tearDown(self):
        pass



if __name__ == "__main__":
    unittest.main()