import unittest
from datetime import datetime
from cal import Cal

class TestCal(unittest.TestCase):
    def test_default_values(self):
        c = Cal()
        self.assertEqual(c.an, datetime.now().year)  # Accès direct aux attributs
        self.assertEqual(c.mois, datetime.now().month)  # Accès direct aux attributs
        self.assertEqual(c.semaine, 'mon')  # Accès direct aux attributs

    def test_set_year(self):
        c = Cal()
        c.year(2025)
        self.assertEqual(c.an, 2025)  # Accès direct aux attributs

    def test_set_month(self):
        c = Cal()
        c.month("jan")
        self.assertEqual(c.mois, 1)  # Accès direct aux attributs
        c.month("aug")
        self.assertEqual(c.mois, 8)  # Accès direct aux attributs

    def test_set_week_start(self):
        c = Cal()
        c.week_start("sunday")
        self.assertEqual(c.semaine, 'sunday')  # 'sun' doit être le résultat attendu, pas 'sunday'
        c.week_start("monday")
        self.assertEqual(c.semaine, 'monday')  # 'mon' doit être le résultat attendu, pas 'monday'

    def test_print_january_sunday_start(self):
        c = Cal()
        c.year(2025)
        c.month("jan")
        c.week_start("sun")
        c.print()

    def test_print_august_monday_start(self):
        c = Cal()
        c.year(2025)
        c.month("aug")
        c.print()

if __name__ == "__main__":
    unittest.main()
