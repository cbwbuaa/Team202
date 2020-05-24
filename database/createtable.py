#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sqlite3
import dbmessage

if __name__ == "__main__":
    database_name = dbmessage.SQL_oper.database_name
    db = sqlite3.connect(database=database_name)

    cur = db.cursor()

    # 用户表
    try:
        cur.execute(
            """
            CREATE TABLE USER_TABLE
            (
                USER_ID INT NOT NULL,
                USER_NAME VARCHAR(99) NOT NULL,
                PASSWORD VARCHAR(99) NOT NULL,
                AUTHORITY INT NOT NULL
            )
            """
        )
    except Exception as e:
        print(e)
        db.rollback()

    # 地图位置关系表
    try:
        cur.execute(
            """
            CREATE TABLE MAP_PLACE_TABLE
            (
                ID INT NOT NULL,
                PLACE_NAME VARCHAR(99),
                CREATE_TIME TIMESTAMP,
                POS_X FLOAT(24),
                POS_Y FLOAT(24),
                INFO TEXT
            )
            """
        )
    except Exception as e:
        print(e)
        db.rollback()

    # 抓取物品表
    try:
        cur.execute(
            """
            CREATE TABLE CATCHING_TABLE
            (
                ID INT NOT NULL,
                CREATE_TIME TIMESTAMP,
                POS_X FLOAT,
                POS_Y FLOAT,
                POS_Z FLOAT,
                IMAGE_ROUTE CHAR(99)
            )
            """
        )
    except Exception as e:
        print(e)
        db.rollback()

    # 运行日志表
    try:
        cur.execute(
            """
            Create table LOG_Table
            (
                ID INT NOT NULL,
                CREATE_TIME TIMESTAMP,
                INFO TEXT
            );
            """
        )
    except Exception as e:
        print(e)
        db.rollback()

    db.commit()
    db.close()
    print("success")
