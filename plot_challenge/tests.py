from datetime import datetime
import unittest
import plot_using_termplot as plot


class MyTestCase(unittest.TestCase):

    def test_get_Data_From_API(self):

        data = plot.getDataFromAPI("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/")
        self.assertEqual(dict, type(data))
        self.assertEqual({  "01-01-2022":300,
                            "02-01-2022":500,
                            "03-01-2022":700,
                            "04-01-2022":1300,
                            "05-01-2022":2000,
                            "06-01-2022":3000,
                            "07-01-2022":3500,
                            "08-01-2022":4000,
                            "09-01-2022":4500,
                            "10-01-2022":5000,
                            "11-01-2022":20000,
                            "12-01-2022":35000,
                            "13-01-2022":46000,
                            "14-01-2022":70000,
                            "15-01-2022":90000
                            },data)

    def test_Convert_Data_Into_Lists(self):

        data = plot.getDataFromAPI("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/")
        x_axis, y_axis = plot.convertDataIntoLists(data)
        self.assertEqual(list, type(x_axis))
        self.assertEqual(list, type(y_axis))
        self.assertEqual(15, len(x_axis))
        self.assertEqual(15, len(y_axis))


    def test_covert_String_Date_Into_Date_Time(self):

        self.assertEqual(datetime.strptime("01-01-2022", '%d-%m-%Y'), plot.covertStringDateIntoDateTime("01-01-2022"))


    def test_check_If_Date_Is_Before_Start_Date(self):

        check_date = plot.isDataDateBeforeStartDate("01-01-2022", "25-12-2021")
        self.assertTrue(check_date)

        check_date = plot.isDataDateBeforeStartDate("01-01-2022", "25-12-2022")
        self.assertFalse(check_date)


if __name__ == "__main__":
    unittest.main()