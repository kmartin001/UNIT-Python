import unittest
from main import ElegNagyTerulet

class Testing(unittest.TestCase):

    def setUp(self):
        print("setting up")
        self.tester = ElegNagyTerulet()

    def test_kisTelek(self):
        print("Teszt 1: kis telek")
        self.assertEqual(self.tester.szabalyos_kerulete(1, 2, 3), (6), "Kis teleknek kell lennie!")

    def test_nagyTelek(self):
        print("Teszt 2: nagy telek")
        self.assertEqual(self.tester.szabalyos_kerulete(20, 20, 25), (65), "Nagy teleknek kell lennie!")

    def test_joTelek(self):
        print("Teszt 3: pont jó telek")
        self.assertEqual(self.tester.szabalyos_kerulete(10, 10, 12), (32), "Jó teleknek kell lennie!")

    def test_ValueError(self):
        print("Teszt 4: nem lehet háromszög")
        with self.assertRaises(ValueError):
            result = self.tester.szabalyos_kerulete(1,1,8)
    
    def test_ValueError_negativ(self):
        print("Teszt 5: nem lehet negatív oldala")
        with self.assertRaises(ValueError):
            result = self.tester.szabalyos_kerulete(-10,1,8)

    def tearDown(self):
        print("tearing down")

if __name__ == '__main__':
    unittest.main()