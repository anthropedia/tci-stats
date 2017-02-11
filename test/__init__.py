from unittest import TestCase

from tcistats import cronbach_alpha


class StatsTest(TestCase):
    def test_cronbach_alphas(self):
        data = [[1, 2, 3], [1, 2, 3]]
        self.assertEqual(cronbach_alpha(data), 1)
        data = [[1, 1, 1], [1, 2, 3]]
        self.assertEqual(cronbach_alpha(data), 0)
        data = [[3, 4, 5], [3, 4, 6]]
        self.assertEqual(cronbach_alpha(data), .9473684211)
        data = [[1, 1, 1], [1, 2, 3], [1, 3, 5]]
        self.assertEqual(cronbach_alpha(data), .6666666667)