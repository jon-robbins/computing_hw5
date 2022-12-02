import unittest

class TestFunctionsHW5(unittest.TestCase):
    def test_car_at_light_correct(self):
        self.assertEqual(FunctionsHW5.car_at_light("red"), "stop")

    def test_car_at_light_error(self):
        self.assertEqual(FunctionsHW5.car_at_light(123), None)

    def test_safe_subtract_correct(self):
        self.assertEqual(FunctionsHW5.safe_subtract(5, 3), 2)

    def test_safe_subtract_error(self):
        self.assertEqual(FunctionsHW5.safe_subtract("5","3"), None)

    def test_retrieve_age_eafp_correct(self):
        self.assertEqual(FunctionsHW5.retrieve_age_eafp({'name': 'John', 'last_name': 'Doe', 'birth': 1987}), 35)

    def test_retrieve_age_eafp_error(self):
        self.assertEqual(FunctionsHW5.retrieve_age_eafp({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}), None)

    def test_retrieve_age_lbyl_correct(self):
        self.assertEqual(FunctionsHW5.retrieve_age_lbyl({'name': 'John', 'last_name': 'Doe', 'birth': 1987}), 35)

    def test_retrieve_age_lbyl_error(self):
        self.assertEqual(FunctionsHW5.retrieve_age_lbyl({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}), None)

    def test_read_data_correct(self):
        df = pd.DataFrame({"name":"jon", "gender":"M"})
        self.assertEqual(FunctionsHW5.read_data('data.csv'), df)

    def test_read_data_error(self):
        self.assertEqual(FunctionsHW5.read_data('123.csv'), None)

    def test_count_simba_correct(self):
        strArray = ["Simba and Nala are lions.", "I laugh in the face of danger.","Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]
        self.assertEqual(FunctionsHW5.count_simba(strArray), 3)

    def test_count_simba_error(self):
        self.assertEqual(FunctionsHW5.count_simba(['123']), 3)

    def test_get_day_month_year_correct(self):
        dateList = []
        dateList.append(datetime.date.today())
        dateList.append(datetime.date(2019, 4, 13))
        df = pd.DataFrame({"year":2019, "month":4, "day":"13"})
        self.assertEqual(FunctionsHW5.get_day_month_year(dateList), df)

    def test_get_day_month_year_error(self):
        self.assertEqual(FunctionsHW5.get_day_month_year(['123']), None)

    def test_compute_distance_correct(self):
        self.assertEqual(FunctionsHW5.compute_distance([((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]), [31.13186522205169, 157.005827868894])

    def test_compute_distance_error(self):
        self.assertEqual(FunctionsHW5.compute_distance(['123']), None)

    def test_sum_general_int_list_correct(self):
        self.assertEqual(FunctionsHW5.sum_general_int_list([[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]), 48)

    def test_sum_general_int_list_error(self):
        self.assertEqual(FunctionsHW5.sum_general_int_list(['123']), None)
