import unittest
import numpy as np
from src.ima_es import es_historique, es_stresse

class TestES(unittest.TestCase):
    def test_es_historique(self):
        rend = np.array([-0.1, -0.05, 0, 0.02, 0.03])
        es = es_historique(rend, 0.95)
        self.assertAlmostEqual(es, -0.1)

    def test_es_stresse(self):
        rend = np.random.randn(1000) * 0.02
        es = es_stresse(rend, fenetre=100, n_top=10)
        self.assertTrue(np.isfinite(es))

if __name__ == '__main__':
    unittest.main()
