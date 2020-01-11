import unittest
import random
import app


class TestApp(unittest.TestCase):
    def test_first(self):
        self.assertTrue(True)

    def test_f1_returns_0(self):
        w = app.f1(0)
        self.assertEqual(w, 0)

    def test_f1_returns_1(self):
        w = app.f1(1)
        self.assertEqual(w, 1)

    def test_f1_returns_4(self):
        w = app.f1(2)
        self.assertEqual(w, 4)

    def test_f1_returns_5(self):
        w = app.f1(2, 1)
        self.assertEqual(w, 5)

    def test_f1_returns_7(self):
        w = app.f1(2, 3)
        self.assertEqual(w, 7)

    def test_f2_returns_a(self):
        w = app.f2("ala")
        self.assertEqual(w, "a")

    def test_f2_returns_1(self):
        w = app.f2([1, 2, 3])
        self.assertEqual(w, 1)

    def test_f2_empty_list(self):
        w = app.f2([])
        self.assertEqual(w, "BUUUUM")

    def test_f3_first(self):
        w = app.f3(1)
        self.assertEqual(w, "jeden")

    def test_f3_second(self):
        w = app.f3(2)
        self.assertEqual(w, "dwa")

    def test_f3_thrid(self):
        w = app.f3(3)
        self.assertEqual(w, "trzy")

    def test_f3_fourth(self):
        w = app.f3(random.choice(range(4, 1000)))
        self.assertEqual(w, "other")

    def test_f4_first(self):
        w = app.f4("ala")
        self.assertEqual(w, "ala ma kota")

    def test_f4_second(self):
        w = app.f4("kot")
        self.assertEqual(w, "kot ma kota")

    def test_f4_third(self):
        w = app.f4("kot", "psa")
        self.assertEqual(w, "kot ma kota i psa")

    def test_f4_fourth(self):
        w = app.f4("kot", "mysz")
        self.assertEqual(w, "kot ma kota i mysz")

    def test_f5_first(self):
        w = app.f5(0)
        self.assertEqual(w, [])

    def test_f5_second(self):
        w = app.f5(1)
        self.assertEqual(w, [0])

    def test_f5_third(self):
        w = app.f5(2)
        self.assertEqual(w, [0, 1])

    def test_f5_fourth(self):
        w = app.f5(7)
        self.assertEqual(w, [0, 1, 2, 3, 4, 5, 6])

    def test_f5_fifth(self):
        w = app.f5(7, 2)
        self.assertEqual(w, [0, 2, 4, 6])

    def test_f5_sixth(self):
        w = app.f5(17, 2)
        self.assertEqual(w, [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_f5_seventh(self):
        w = app.f5(17, 5)
        self.assertEqual(w, [0, 5, 10, 15])

    def test_f6_first(self):
        w = app.f6(1, "*")
        self.assertEqual(w, "*")

    def test_f6_second(self):
        w = app.f6(7, "*")
        self.assertEqual(w, "*******")

    def test_f7_returns_word(self):
        w = app.f7("ala")
        self.assertEqual(w, "slowo")

    def test_f7_returns_digit(self):
        w = app.f7(1)
        self.assertEqual(w, "cyfra")

    def test_f7_returns_number(self):
        w = app.f7(111111)
        self.assertEqual(w, "liczba")

    def test_f7_returns_signed_number(self):
        w = app.f7(-11111)
        self.assertEqual(w, "liczba_ze_znakiem")

    def test_f7_returns_sentence(self):
        w = app.f7("Ala ma kota.")
        self.assertEqual(w, "zdanie")

    def test_f7_returns_begin_tag(self):
        w = app.f7("<taag>")
        self.assertEqual(w, "tag poczatkowy")

    def test_f7_end_tag(self):
        w = app.f7("</taag>")
        self.assertEqual(w, "tag koncowy")


if __name__ == '__main__':
    unittest.main()
