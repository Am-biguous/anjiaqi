import unittest
import psycopg2

global database
database = "ddpap3lpi9i19j"
global user
user = "fdfknkjncxjkoc"
global password
password = "28da3e8eba93e294a5edcb487a82d71a9b7b15cc17ad1e0f4000c4d265542b1c"
global host
host = "ec2-174-129-255-57.compute-1.amazonaws.com"
global port
port = "5432"


class TestStringMethods(unittest.TestCase):

    def test_select(self):
        pname = 'an'
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

        print("Opened database successfully")

        cur = conn.cursor()

        cur.execute("SELECT *  from text WHERE name ='" + pname + "'")
        rows = cur.fetchall()
        if len(rows) != 0:
            x = rows[0][0]
        self.assertEqual(2, x)

    def test_insert(self):

        id = '100'
        pname = 'hundred'
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

        cur = conn.cursor()

        cur.execute("INSERT INTO text VALUES (" + id + ",'" + pname + "')")

        conn.commit();

        cur.execute("SELECT *  from text WHERE name ='" + pname + "'")
        rows = cur.fetchall()
        if len(rows) != 0:
            x = rows[0][0]
        self.assertEqual(100, x)

    def test_delete(self):

        id = '6'

        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

        cur = conn.cursor()
        cur.execute("SELECT *  from text WHERE id ='" + id + "'")
        rows = cur.fetchall()
        if len(rows) != 0:
            cur.execute("DELETE FROM text WHERE id = " + id)
            conn.commit();
            x = 1
            self.assertEqual(1, x)
        else:
            x = 0
            self.assertEqual(0, x)

    def test_updata(self):
        id = '8'
        pname = 'niubi'
        conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

        cur = conn.cursor()

        cur.execute("UPDATE text SET name = '" + pname + "' WHERE id = " + id)

        conn.commit();
        self.assertEqual('niubi', pname)

if __name__ == '__main__':
    unittest.main()