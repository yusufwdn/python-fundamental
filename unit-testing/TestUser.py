import unittest

def connect_db():
    print("connected...")

def disconnect_db(db):
    print("disconnected from database {}".format(db))

class User:
    username  = ""
    is_active = False

    def __init__(self, db, username):
        self.username = username

    def set_active(self):
        self.is_active = True

class TestUser(unittest.TestCase):
    # method ini dijalankan di awal unittesting
    def setUp(self):
        self.db = connect_db()
        self.albert = User(self.db, "albert")

    # method ini dijalankan di akhir unittesting
    def tearDown(self):
        disconnect_db()

    def test_user_default_not_active(self):
        # cek value apakah atribut is_active bernilai false? jika ya, maka test berhasil.
        self.assertFalse(self.albert.is_active)

    def test_user_is_active(self):
        # menjalankan method set_active() untuk mengubah value dari atribut is_active menjadi True.
        self.albert.set_active()

        # cek value apakah atribut is_active bernilai true? jika ya, maka test berhasil.
        self.assertTrue(self.albert.is_active)

if __name__ == "__main__":
    # test runner
    unittest.main()