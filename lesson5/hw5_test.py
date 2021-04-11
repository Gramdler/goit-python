import unittest
from hw5 import normalize


class NormalizeTests(unittest.TestCase):

    def test_check_lower_case(self):

        result = normalize("вася пупкин")

        self.assertEqual("vasya_pypkin", result)

    def test_check_upper_case(self):

        result = normalize("ВАСЯ ПУПКИН")

        self.assertEqual("VASYA_PYPKIN", result)

    def test_check_mix_case(self):

        result = normalize("Вася Пупкин")

        self.assertEqual("Vasya_Pypkin", result)

    def test_check_another_symbols(self):

        result = normalize("Вася#$@_Пупкин1998")

        self.assertEqual("Vasya____Pypkin1998", result)


if __name__ == '__main__':
    unittest.main()
