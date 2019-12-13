from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.core import serializers
import json

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


def main_Index(request):
    return render(request, "main_index.html")

def pageSelect(request):
    return render(request, "select.html")

def pageInsert(request):
    return render(request, "insert.html")

def pageDelete(request):
    return render(request, "delete.html")
def pageUpdate(request):
    return render(request, "update.html")



def select(request):
    print(database,user,password,host,port)
    pname = request.GET.get('pname')
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

    print("Opened database successfully")

    cur = conn.cursor()

    cur.execute("SELECT *  from text WHERE name ='"+pname+"'")
    rows = cur.fetchall()
    if len(rows) != 0:
        print(rows)
        x = rows[0][0]
        return HttpResponse(pname+"所对应的ID为"+str(x))
    else:
        return HttpResponse("NAME NOT FIND,PLEASE BACK TO LAST PAGE")

def insert(request):
    id = request.GET.get('id')
    pname = request.GET.get('pname')
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

    cur = conn.cursor()

    cur.execute("INSERT INTO text VALUES ("+id+",'"+pname+"')")

    conn.commit();
    return HttpResponse("INSERT SUCCESS")
def delete(request):
    id = request.GET.get('id')

    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

    cur = conn.cursor()
    cur.execute("SELECT *  from text WHERE id ='" + id + "'")
    rows = cur.fetchall()
    if len(rows) != 0:
        cur.execute("DELETE FROM text WHERE id = "+id)

        conn.commit();
        return HttpResponse("DELETE SUCCESS")
    else:
        return HttpResponse("Id,which you want to delete not exist, please input id existing in the table")

def update(request):
    id = request.GET.get('id')
    pname = request.GET.get('pname')
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

    cur = conn.cursor()

    cur.execute("UPDATE text SET name = '"+pname+"' WHERE id = "+id)

    conn.commit();
    return HttpResponse("Update SUCCESS")