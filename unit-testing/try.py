import unittest

class TestStringMethods(unittest.TestCase):
    # Contoh test case  1
    def test_strip(self):
        # menghilangkan beberapa karakter dari string (c . m o w) dan melakukan pengecekan value setelah penghilangan karakter
        self.assertEqual('www.google.com'.strip('c.mow'), 'google')

    # Contoh test case 2
    def test_isalnum(self):
        self.assertTrue('gre3nday')
        self.assertTrue('gr!nd3y')

    # Contoh test case 3
    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)

        # cek s.index gagal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index('decode')

        # test runner
        if __name__ == '__main__':
            unittest.main()
