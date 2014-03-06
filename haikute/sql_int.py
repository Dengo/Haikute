#!/usr/bin/env python

import sqlite3 as lite
from collections import deque


def db_write(haistorageadd):
    conn = lite.connect('haiku.db')

    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS Haitable(Id INTEGER PRIMARY KEY, Haiku TEXT);')
        while not haistorageadd.empty():
            entry = haistorageadd.get()
            cur.execute('INSERT INTO Haitable VALUES (NULL, ?);', [entry])
        conn.commit()

    return


def db_read():
    # import pdb; pdb.set_trace()
    conn = lite.connect('haiku.db')
    haiqueue = deque()

    with conn:
        cur = conn.cursor()
        cur.execute('SELECT Haiku FROM Haitable ORDER BY Id DESC LIMIT 5;')
        entries = cur.fetchall()

        # import pdb; pdb.set_trace()
        for entry in entries:
            entry = entry[0].encode('UTF-8')
            haiqueue.append(entry)
    return haiqueue
