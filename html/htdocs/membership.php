<?php
include $_SERVER['DOCUMENT_ROOT']."/db.php"; /* db load */

$num = $_GET['member_id'];
$now = date_default_timezone_get();
$created_time = date('Y-m-d', strtotime($now));
$sql = mq("select * from member where member_id = $num");
$board = $sql -> fetch_array();
?>
<!doctype html>
<head>
    <meta charset="UTF-8">
    <title>게시판</title>
    <link rel="stylesheet" type="text/css" href="/css/jquery-ui.css" />
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="/css/popup.css">
    <script>
        function resizeWindow(win)    {

            var wid = win.document.body.offsetWidth + 30;

            var hei = win.document.body.offsetHeight + 40;        //30 과 40은 넉넉하게 하려는 임의의 값임

            win.resizeTo(wid,hei);

        }
    </script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

    <script type="text/javascript" src="/js/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="/js/jquery-ui.js"></script>
</head>
<body>
<div id="sign_container">
    <div class="center-align">
        <div class="login_box">
            <form method="post" action="membership_ok.php" name="memform">
                <div id="table-container">
                    <div class="margin-control">
                        <div id="title_margin">
                            <h1 style="display: inline-block">회원권 등록</h1>
                            <span onclick="window.close();" style="margin-left: 80px; position:absolute; display: inline-block;background-image: url('/image/exit.png'); background-size: cover; width: 30px; height: 50px;"></span>
                        </div>
                        <table cellspacing="0" height="300">
                            <tr>
                                <td align="left" width="250" ><b>회원 ID</b></td>
                                <td align="left" width="200"><input type="text" style="border:none;" size="6" value="<?php echo $board['member_id']; ?>" class="inph" name="member_id" id="member_id" placeholder="ID" required readonly>
                                <input type="text" style="border:none;" size="4" value="<?php echo $board['name']; ?>" class="inph" id="member_id" placeholder="ID" readonly></td>
                            </tr>
                            <tr>
                                <td align="left" width="250"><b>기간</b></td>
                                <td align="left" width="400">
                                    <select name="emadress" id="date" name="date" class="date" style="margin-left: 10px" required>
                                        <option id="date_a" value="70000">1개월</option>
                                        <option value="180000">3개월</option>
                                    </select>
                                    <div id="result1" class="result" style="margin-left:50px; display:inline-block;" name="name">70000</div></td>
                            </tr>
                            <tr>
                                <td align="left" width="250"><b>결제 방법</b></td>
                                <td align="left" width="200">카드 <input type="radio" id="credit" class="radiotype" name="pay_type" value="0" checked>
                                    현금<input type="radio" id="cash" class="radiotype" name="pay_type" value="5000" style="margin-left:10px">
                                    <div id="result" style="margin-left: 50px; display:inline-block;" name="name"></div></td>
                            </tr>
                            <tr>
                                <td align="left" width="250" ><b>최종 금액</b></td>
                                <td align="left" width="200">
                                    <div id="total_result" style="display:inline-block" name="name">70000</div></td>
                            </tr>
                            <tr>
                                <td align="left" width="250"><b>시작일</b></td>
                                <td align="left" width="200"><input type="date" size="35" id="start_date" class="inph" name="start_date" value="<?php echo $board['start_date']; ?>" placeholder="시작일" required></td>
                            </tr>
                            <tr>
                                <td align="left" width="250"><b>종료일</b></td>
                                <td align="left" width="200"><input type="date" size="35" id="due_date" class="inph" name="due_date" value="<?php echo $board['due_date']; ?>" placeholder="만료일" required></td>
                            </tr>
                        </table>
                            <div style="margin-top: 20px; text-align: center;">
                            <button id="button_submit" type="submit" onclick="clicked(event)" style="background-color: white; background-image: url('/image/add.png'); display:inline-block; vertical-align:bottom; width: 50px; height: 50px; background-size:cover; font-weight: bold; font-family: '배달의민족 한나체 Air'; border: none;" >
                                <div id="button_submit_text">
                                    등 록
                                </div>
                            </button>
                            </div>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>
<script>

    function clicked(e) {
        if(!confirm('등록하시겠습니까?')){
            e.preventDefault();
            alert('취소되었습니다.');
            window.close();
        }
    }
    // 윤달 체크 function
    function isLeapYear(year){
        if(year % 4 == 0 && year % 100 != 0 || year % 400 == 0){
            return true;
        } else{
            return false;
        }
    }
    function formatDate(date) {
        let month_no = 1;
        if (document.getElementById("date").value != '70000') {
            month_no = month_no + 2;
        }

        var d = new Date(date),
            month = '' + (d.getMonth() + month_no + 1), // getMonth() + 1 -> 당월
            day = '' + (d.getDate() - 1),
            year = d.getFullYear();

        if (day == '0') {
            month = month - 1;
        }

        if (parseInt(month) > 12) {
            year = year + 1;
            month = month - 12;
            month = '' + month.toString();
            if (month == '2') {
                if (parseInt(day) > 28) {
                    day ='' + '28';
                    if (isLeapYear(year) == true) {
                        day = '' + parseInt(day) + 1;
                    }
                }
            }
        }
        if (day == '0') {   // 앞에서 하루를 뺌
            var a  = new Date(year, parseInt(month) , 0),
                month = '' + (a.getMonth() + 1),
                day = '' + (a.getDate()),
                year = a.getFullYear();
        }

        if (month.length < 2){
            month = '0' + month;
        }
        if (day.length < 2){
            day = '0' + day;
        }
        return [year, month, day].join('-');
    }

</script>

<script>
    let result = document.querySelector('#result');
    document.body.addEventListener('change', function (e) {
        let target = e.target;
        switch (target.id) {
            case 'cash':
                result.textContent = `할인액 : ${e.target.value}`;
                if(document.getElementById("date").value == '70000'){
                    result.textContent =  `할인액 : ${e.target.value}`;
                    document.querySelector('#total_result').textContent = `${document.getElementById("date").value - e.target.value}`
                } else {
                    result.textContent = `할인액 : ${3 * document.getElementById("cash").value}`;
                    document.querySelector('#total_result').textContent = `${180000 - 3 * document.getElementById("cash").value}`
                }
                break;
            case 'credit':
                result.textContent = '';
                document.querySelector('#total_result').textContent = `${document.getElementById("date").value}`
                break;
            case 'date':
                let buttons = document.getElementsByName('pay_type');
                for (let i=0;i<buttons.length;i++) {
                    let button = buttons[i];

                    if (button.checked) {
                        if(button.value == '0') {
                            result.textContent = "";
                            document.querySelector('#total_result').textContent = `${document.getElementById("date").value}`
                        } else {
                            if(document.getElementById("date").value == '70000') {
                                result.textContent =  `할인액 : ${document.getElementById("cash").value}`;
                                document.querySelector('#total_result').textContent = `${70000 - document.getElementById("cash").value}`
                            } else {
                                result.textContent = `할인액 : ${3 * document.getElementById("cash").value}`;
                                document.querySelector('#total_result').textContent = `${180000 - 3 * document.getElementById("cash").value}`
                            }
                        }
                    }
                }
                document.querySelector('.result').textContent = parseInt(`${e.target.value}`);
                if(document.getElementById("start_date") != null) {
                    document.getElementById("due_date").value = formatDate(document.getElementById("start_date").value);
                }
                break;
            case 'start_date':
                document.getElementById("due_date").value = formatDate(e.target.value);
                break;

        }


    });
</script>

</body>
</html>