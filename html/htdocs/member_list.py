#!C:\Users\Haram_Song\AppData\Local\Programs\Python\Python38-32\python.exe

import pymysql
import sys
import codecs
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
    print('''
    <!doctype html>
    <head>
    <meta charset="UTF-8">
    <title>게시판</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="css/tablestyle.css">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" 
            integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" 
            integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <script src="/js/bootstrap.js"></script>
    <script type="text/javascript">
        function changeTrColor(trObj, oldColor, newColor) {
            trObj.style.backgroundColor = newColor;
            trObj.onmouseout = function(){
                trObj.style.backgroundColor = oldColor;
            }
        }

        function clickTrEvent(trObj) {
            alert(trObj.id);
        }

    </script>
</head>
<body>
<div id="container">
    <div id="board_area">
        <div id="title_margin">
           <h1 style="display: inline-block;">회원 리스트</h1>
              <a href="/index.php"><span style="margin-left: 20px;background-size: cover;display: inline-block;
                 background-image: url('/image/exit.png'); width: 25px; height:35px;"></span></a>

            <div id="write_btn">
                <div style="display:inline-block; margin-left: 30px; margin-right:30px; margin-top:30px;">
<!-- 상세정보-->
                <button id="button2" onclick="
                if(k == undefined) {
                    alert('회원 선택을 하십시오.');
                    exit();
                }
                 let url_code2 = `/member_change.py?member_id=${k}`;
                 window.open(url_code2, 'member', 'width=495, height=550,top=100,left=500,resizable=no');
">
                    <div id="button_text2">
                        상세정보
                    </div>
                </button>
<!-- 회원권 등록-->
                <button id="button3" onclick="
                    if(k == undefined) {
                        alert('회원 선택을 하십시오.');
                        exit();
                    }
                    let url_code = `/membership.php?member_id=${k}`;
                    window.open(url_code, 'member', 'width=495, height=550,top=100,left=500,resizable=no');">
                    <div id="button_text3">
                        회원권 등록
                    </div>
                </button>
<!-- 회원권양도-->
                <button id="button4" onclick="
                    if(k == undefined) {
                      alert('회원 선택을 하십시오.');
                      exit();
                     }
                    let end_date = new Date(j);
                    let date_now = new Date();
                    if (end_date == 'Invalid Date') {
                        alert('양도처리 가능한 대상이 아닙니다.');
                        exit();
					}
                    let days_diff = (end_date - date_now) / 86400000;
                    if (days_diff < 8) {
                        alert('잔여일이 7일 이내면 양도가능 대상이 아닙니다.');
                        exit();
                    } 
                    let url_code3 = `/membership_transfer_ehs.php?member_id=${k}`;
                    window.open(url_code3, 'member', 'width=495, height=550,top=100,left=500,resizable=no');">
                    <div id="button_text4">
                        회원권 양도
                    </div>
                 </button>
<!-- 회원 일시정지-->
                    <button id="button6" onclick="
                    if(k == undefined) {
                        alert('회원 선택을 하십시오.');
                        exit();
                     }
                    let end_date = new Date(j);
                    let date_now = new Date();
					if (end_date == 'Invalid Date') {
                        alert('일시정지처리 가능한 대상이 아닙니다.');
                        exit();
                    }
					let days_diff = (end_date - date_now) / 86400000;
                    if (days_diff < 8) {
                        alert('잔여일이 7일 이내면 일시정지 대상이 아닙니다.');
                        exit();
                    }                    
                    let url_code4 = `/membership_pause_ehs.php?member_id=${k}`;
                    window.open(url_code4, 'member', 'width=495, height=550,top=100,left=500,resizable=no');">
                        <div id="button_text6">
                            일시정지
                        </div>
                    </button>
<!-- 메모-->
                  <button id="button5" onclick="
                      if(k == undefined) {
                            alert('회원 선택을 하십시오.');
                            exit();
                      }
                      let url_code1 = `/member_memo.php?member_id=${k}`;
                      window.open(url_code1,'member', 'width=400, height=500,top=100,left=500,resizable=no');">
                      <div id="button_text5">
                          메모
                      </div>
                  </button>

                </div>
                <div style="display:inline-block;">
                <button id="button1" onclick="window.open('signin.html','member', 'width=495, height=850,top=100,left=500,resizable=no');">
                    <div id="button_text1">
                        회원 등록
                    </div>
                </button>
                </div>
            </div>
        </div>
    </div>
        <table class="list-table">
            <thead>
            <tr>
                <th width="40">상태</th>
                <th width="80">회원번호</th>
                <th width="50">이름</th>
                <th width="100">전화번호</th>
                <th width="80">시작일</th>
                <th width="80">종료일</th>
            </tr>
            </thead>
    ''')

    sql = "select a.member_id, a.name, a.phone_number, b.type, b.start_date, b.due_date, b.doc_source, b.type_source " \
          "from member as a left outer join transaction as b on a.member_id = b.member_id " \
          "order by a.member_id, b.start_date desc"
    curs.execute(sql)
    data = curs.fetchall()
    old = ''
    for x in data:
        if x[0] == 'None':  # x[0] : member_id, x[1] : name, x[2] : phone_number, x[3] : start_date, x[4] : due_date
            continue
        date_now = date.today()
        start_date = x[4]
        due_date = x[5]
        if old == x[0]:
            continue
        if start_date is None or due_date is None:
            status = 'status_gray'
            start_date = ''
            due_date = ''
        else:
            warning = due_date - timedelta(days=31)
            warning1 = datetime.strftime(warning, "%Y-%m-%d")
            warning2 = datetime.strptime(warning1, '%Y-%m-%d')
            warning_date = warning2.date()
            if due_date >= date_now >= warning_date:
                status = 'status_red'
            elif date_now < start_date:
                status = 'status_yellow'
            elif due_date > date_now > start_date:
                status = 'status_green'
            else:
                status = 'status_gray'
        print(
            "<tbody>"
            '<script>let k;let j;</script>'
            '<tr class ="get_id" onclick="'
            'k = document.getElementById(', end='')
        print(x[0], end='')
        print(
            ").getAttribute('value');"
            'j = document.getElementById(', end='')
        print(x[0], end='')
        print(
            " ).getAttribute('data_date');"
            "let b = document.getElementsByClassName('get_id');"
            "let i;"
            'for (i=0; i < b.length; i++) {'
            "b[i].style.backgroundColor = '#FFFFFF';}"
            'document.getElementById(', end='')
        print(x[0], end='')
        print(
            ").style.backgroundColor = '#C8C8C8';"
            '" id="', end='')
        print(x[0], end='')
        print('" value ="', end='')
        print(x[0], end='')
        print('" data_date = "', end='')
        print(start_date, end='')
        print(
            '">'
            '<td width = "40"><span class ="', end='')
        print(status, end='')
        print(
            '"></span></td>'
            '<td width = "80" > ', end='')
        print(x[0], end='')
        print('</td><td width = "100" >', end='')
        print(x[1], end='')
        print('</td><td width = "110" >', end='')
        print(x[2], end='')
        print('</td><td width = "100" >', end='')
        print(start_date, end='')
        print('</td><td width = "100" >', end='')
        print(due_date, end='')
        print('</td></tr></tbody>')

        old = x[0]
    print('</table></div></div>')
    print(
        "</body>"
        "</html>")
    conn.commit()
finally:
    conn.close()
