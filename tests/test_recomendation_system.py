import unittest
from uab.pa.project.common import TipusDades, TipusRecomanador
from uab.pa.project.test_recommendations import funcio_test_recomanadors


class RecommendationSystemTests(unittest.TestCase):

    def test_run_test_movies_simple(self):
        sol = funcio_test_recomanadors(self,
                                       TipusDades.Pelicules,
                                       TipusRecomanador.Simple,
                                       "1")
        print(sol)


if __name__ == '__main__':
    unittest.main()
