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
    sql = "select a.*, b.start_date, b.due_date " \
          "from member as a left outer join time_manage as b on a.member_id = b.member_id " \
          "where a.member_id=%s order by b.start_date desc limit 1"
    mem = cgi.FieldStorage()['member_id'].value
    curs.execute(sql, mem)
    data = curs.fetchall()
    emailarr = data[4].split('@')
    print('''
        <!doctype html>
            <head>
                <meta charset="UTF-8">
                <title>게시판</title>
                <link rel="stylesheet" type="text/css" href="/css/jquery-ui.css" />
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                      integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                      crossorigin="anonymous">
                <link rel="stylesheet" href="/css/popup.css">
                <script>
                    function resizeWindow(win)    {
                        var wid = win.document.body.offsetWidth + 30;
                        var hei = win.document.body.offsetHeight + 40;        //30 과 40은 넉넉하게 하려는 임의의 값임
                        win.resizeTo(wid,hei);
                    }
                </script>
                <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
                        integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n"
                        crossorigin="anonymous"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"
                        integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6"
                        crossorigin="anonymous"></script>
                <script type="text/javascript" src="/js/jquery-3.2.1.min.js"></script>
                <script type="text/javascript" src="/js/jquery-ui.js"></script>
                <script type="text/javascript" src="/js/common.js"></script>
            </head>
            <body>
                <script>
                    function delete_member() {
                        if(confirm("정말로 삭제하시겠습니까?"))
                        {
                            location.href="/member_delete.php?phone_number= 
            ''', end='')
    print(data[5], end='')
    print('''
                    "} else {
                        }
                    }
                </script>
                <div id="sign_container">
                    <div class="center-align">
                        <div class="login_box">
                            <form method="post" action="member_change_ok.py" name="memform">
                                <div id="table-container">
                                    <div class="margin-control">
                                        <div id="title_margin">
                                        <h1 style="display: inline-block">회원 정보</h1>
                                            <span onclick="window.close();" style="margin-left: 90px; position:absolute; 
                                            display: inline-block;background-image: url('/image/exit.png'); 
                                            background-size: cover; width: 30px; height: 50px;"></span>
                                        </div>
                                        <table cellspacing="0" height="470">
                                            <tr>
                                                <td align="left" width="250"><b>이름</b></td>
                                                <td align="left" width="200"><input type="text" size="35" class="inph"
                                                 name="name" id="name" value="
                                                 ''', end='')
    print(data[1],end='')
    print('''
                                                 " placeholder="이름" required></td>
                                            </tr>
                                            <tr>
                                                <td align="left" width="250"><b>생년월일</b></td>
                                                <td align="left" width="200"><input type="text" size="35" class="inph"
                                                 name="birth_date" value="
                                                 ''', end='')
    print(data[2])
    print('''
                                                 " id="birth_date" placeholder="생년월일" required></td>
                                            </tr>
                                            <tr>
                                                <td align="left" width="250"><b>성별</b></td>
                                                <td align="left" width="200">
    ''')
    if data[3] == '남':
        print('''
        <input type="radio" id="male" name="gender" class="inph" value="남" style="margin-left:10px" checked>남</input>
        <input type="radio" id="female" name="gender" value="여">여</input>
        ''')
    else:
        print('''
               <input type="radio" id="male" name="gender" class="inph" value="남" style="margin-left:10px">남</input>
               <input type="radio" id="female" name="gender" value="여" checked>여</input>
               ''')
    print('''                                
                                                </td>
                                            </tr>
                                            <tr>
                                                <td align="left" width="250"><b>이메일</b></td>
                                                <td align="left" width="400"><input type="text" class="inph" value="
                                                ''', end='')
    print(emailarr[0], end='')
    print('''
                                                " name="email" style="margin-right: 10px" required>@<select name="emadress"
                                                  class="inph" value="
                                                  ''', end='')
    print(emailarr[1], end='')
    print('''
                                                " style="margin-left: 10px" required>
                                                        <option value="naver.com">naver.com</option>
                                                        <option value="nate.com">nate.com</option>
                                                        <option value="hanmail.com">hanmail.com</option>
                                                    </select></td>
                                            </tr>
                                            <tr>
                                                <td align="left" width="250"><b>전화번호</b></td>
                                                <td align="left" width="200"><input type="text" size="35" class="inph"
                                                name="phone_number" value="
                                                ''', end='')
    print(data[5], end='')
    print('''                                           
                                                " placeholder="전화번호" required></td>
                                            </tr>
                                            <tr>
                                                <td align="left" width="250"><b>주소</b></td>
                                                <td align="left" width="200"><input type="text" size="35" class="inph" 
                                                name="address" value="
                                                ''', end='')
    print(data[6], end='')
    print('''                                           
                                                " placeholder="주소" required></td>
                                            </tr>
                                            <tr>
                                                <td align="left" width="200"><b>차량 번호</b></td>
                                                <td align="left" width="200"><input type="text" size="35" class="inph"
                                                 name="car_number" value="
                                                 ''', end='')
    print(data[7], end='')
    print('''                                             
                                                 " placeholder="차량 번호"></td>
                                            </tr>
                                            <tr>
                                                <td align="left" width="250"><b>유효기간 시작일</b></td>
                                                <td align="left" width="200"><input type="date" size="35" class="inph"
                                                 name="start_date" value="
                                                 ''', end='')
    print(data[8], end='')
    print('''                                             
                                                 " placeholder="시작일" required>
                                                 <span style="background-color: white; margin-left: 30px;" 
                                                 onclick="window.open('/member_time.php?member_id=
                                                 ''', end='')
    print(data[0])
    print('''
                                                 ', 'member', 'width=495,height=900,top=200,left=500,resizable=no');">
                                                 내역 보기</span></td>
                                            </tr>
                                            <tr>
                                                <td align="left" width="250"><b>유효기간 만료일</b></td>
                                                <td align="left" width="200"><input type="date" size="35" class="inph"
                                                 name="due_date" value="
                                                 ''', end='')
    print(data[9], end='')
    print('''                                             
                                                 " placeholder="만료일" required></td>
                                            </tr>
                                            <tr>
                                                <td align="left" width="250"><b>리그 등급</b></td>
                                                <td align="left" width="200"><input type="text" size="35" class="inph" 
                                                name="league_grade" value="
                                                ''', end='')
    print(data[10], end='')
    print('''
                                                " placeholder="리그 등급" required></td>
                                            </tr>
                                        </table>
                                        <button id="button_submit" type="submit" style="background-color:white;
                                                background-size:cover; background-image: url('image/chat.png'); 
                                                display:inline-block; width: 60px; height: 60px; border: none;
                                                margin-top: 20px; position: relative;">
                                            <div id="button_submit_text">변경</div>
                                        </button>
                                        <button id="button_submit" style="display:inline-block; position: absolute; 
                                                vertical-align:center; margin-top: 20px; margin-left: 50px; 
                                                width: 60px; height: 60px;background-size: cover; 
                                                background-image: url('image/delete.png');" onclick="delete_member();">
                                            <div id="button_submit_text">삭제</div>
                                        </button>
                                    </div>
                                </div> 
                            </form>
                        </div>
                    </div>
                </div>
            </body>
        </html>
    ''')
    conn.commit()
finally:
    conn.close()