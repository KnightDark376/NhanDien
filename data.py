import cv2
import numpy as np
import os
import sqlite3


def insertOrUpdate(id, name):
    conn = sqlite3.connect('\Documents\Python\DATA\data.db')
    query = "SELECT * FROM people WHERE IF=" + str(id)
    cusror = conn.execute(query)

    isRecordExist = 1
    for row in cusror:
        isRecordExist = 1

    if isRecordExist == 0 :
        query = "INSERT INTO people(ID, Name) VALUES(" +str(id) +',' + str(name) + "')"
    else:
        query = "UPDATE people SET Name=" + str(name) + "WHERE ID=" + str(id)
    conn.execute(query)
    conn.commit()
    conn.close()
insertOrUpdate(1, "abc")