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
    curs = conn.cursor()
    sql = "SELECT * FROM pythontb;"
    curs.execute(sql)
    data = curs.fetchall()

    print("content-type: text/html;charset=utf-8\r\n")
    print('''
        <html>
            <head>
            <title>Python CGI Test</title></head>
                    <body>
    ''')
    for i in range(len(data)):
        print(i+1, end='')
        print("번째 값은, ", end='')
        print(data[i], end='')
        print("입니다.")
        print("<br>")

finally:
    conn.close()
print(
        "</body>"
        "</html>"
    )