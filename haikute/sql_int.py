#!/usr/bin/env python

import sqlite3 as lite
from collections import deque


def db_write(haistorageadd):
    conn = lite.connect('haiku.db')

    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTs Haitable(Id INTEGER PRIMARY KEY, Haiku TEXT);')
        for entry in haistorageadd:
            cur.execute('INSERT INTO Haiku VALUES (NULL, ?);', [entry])

    return


def db_read():
    conn = lite.connect('haiku.db')
    haiqueue = deque()

    with conn:
        cur = conn.cursor()
        cur.execute('SELECT Haiku FROM Haitable ORDER BY Id DESC LIMIT 5;')
        entries = cur.fetchall()

        for entry in entries:
            haiqueue.append(entry[0])
    return haiqueue
