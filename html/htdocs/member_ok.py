#!C:\Users\Haram_Song\AppData\Local\Programs\Python\Python38-32\python.exe

import pymysql
import sys
import codecs
import cgi, cgitb
from datetime import date, timedelta, datetime
from bs4 import BeautifulSoup

# dateutil import시 서버 에러

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# connection 정보
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='hrsong502',
    db='club_member_mgmt',
    charset='utf8'
)
try:
    curs = conn.cursor()

    print("content-type: text/html;charset=utf-8\r\n")
    form = cgi.FieldStorage();
    name = form.getvalue('name');
    birth_date = form.getvalue('birth_date');
    gender = form.getvalue('gender');
    email = form.getvalue('email') + '@' + form.getvalue('emadress');
    phone_number = form.getvalue('phone_number');
    address = form.getvalue('address');
    car_number = form.getvalue('car_number');
    locker_num = form.getvalue('locker_num');
    locker_pw = form.getvalue('locker_pw');
    league_grade = form.getvalue('league_grade');
    created_by = 'admin';
    created_time = datetime.today();
    changed_by = 'admin';
    changed_time = datetime.today();
    sql = "INSERT INTO member (name,birth_date,gender,email,phone_number,address,car_number,locker_num,locker_pw,league_grade,created_by,created_time,changed_by,changed_time) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
    mem = (name,birth_date,gender,email,phone_number,address,car_number,locker_num,locker_pw,league_grade,created_by,created_time,changed_by,changed_time)
    curs.execute(sql,mem)
    print('''
        <meta charset="utf-8" />
        <script type="text/javascript">alert('등록이 완료되었습니다.'); window.close(); window.opener.location.reload();</script>
    ''')
    conn.commit()
finally:
    conn.close()