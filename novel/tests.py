import unittest
import psycopg2
global L
L={1:'wang',2:'an',3:'zhang',5:'tian',8:'shen'}

class TestStringMethods(unittest.TestCase):

    def test_select(self):
        pname = 'tian'
        for i in L.keys():
            if pname==L[i]:
                name=L[i]
                print('select success! the name  ' + pname + '  of id is  ' + str(i))
        self.assertEqual(pname,name)


    def test_insert(self):

        id = 100
        pname = 'hundred'
        L.setdefault(id,pname)
        for i in L.keys():
            if pname==L[i]:
                name=L[i]
                print('insert success')
        self.assertEqual(pname, name)

    def test_delete(self):

        id = 2
        id_1=-1
        for i in L.keys():
            if id==i:
                id_1=i
                print('delete success')
        self.assertEqual(id,id_1)

    def test_updata(self):
        id = 5
        pname = 'qiubi'
        for i in L.keys():
            if i == id:
                L[id] = pname
                print('updata success new name is '+L[id])
        self.assertEqual(pname, L[id])

if __name__ == '__main__':
    unittest.main()