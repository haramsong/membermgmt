#!C:\Users\Haram_Song\AppData\Local\Programs\Python\Python38-32\python.exe

import pymysql
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# connection 정보
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='hrsong502',
    db='pythondb',
    charset='utf8'
)
try:
    print("content-type: text/html;charset=utf-8\r\n")
    print(
        "<html>"
        "<head>"
        "\t<title>Python CGI Test</title></head>"
        "<body>"
    )
    curs = conn.cursor()
    sql = "UPDATE pythontb SET row2 = %s WHERE row1 = %s"
    val = (10, 7)
    curs.execute(sql, val)
    data = curs.fetchall()
    conn.commit()



    for i in data:
        print(i)

finally:
    conn.close()
print(
        "</body>"
        "</html>"
    )