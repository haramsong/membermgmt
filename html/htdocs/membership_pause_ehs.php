<?php
include $_SERVER['DOCUMENT_ROOT']."/db.php"; /* db load */
date_default_timezone_set('Asia/Seoul');
$num = $_GET['member_id'];
$sql = mq("select a.member_id, a.name, a.phone_number, b.start_date, b.due_date 
             from member as a left outer join transaction as b 
			   on a.member_id = b.member_id where a.member_id = $num order by a.member_id, b.start_date desc");
$board = $sql -> fetch_array();
// $start_date = $board['start_date'];
// $start_date = strtotime($start_date);
// $due_date = $board['due_date'];
// $due_date = strtotime($due_date);
// $today = date_default_timezone_get();                 // echo $today; -> Asia/Seoul
// $today = date('Y-m-d',strtotime($today));             // echo $today; -> YYYY-MM-DD(오늘날짜)

$start_date = strtotime($board['start_date']);
$due_date = strtotime($board['due_date']);

$today = date('Y-m-d');                                  // echo $today; -> YYYY-MM-DD(오늘날짜)
if ($start_date < strtotime($today)) {                   // echo $start_date;  -> 1606431600 (2020-11-27의 값), echo strtotime($today); -> 1600354800
   $start_date = strtotime($today);                      // echo $today; -> YY-MM-DD 형태로 출력
}
$days_diff_base = round(($due_date - $start_date) / 86400); //초 * 분 * 시간 = 86400
$start_date = date('Y-m-d',$start_date);
$due_date = date('Y-m-d',$due_date);

$chg_start_date = date('Y-m-d', strtotime($due_date. "+ 1 days"));   // 변경유효기간 시작일,  echo $due_date; -> 10자리 정수형태로 출력
$chg_due_date = date('Y-m-d', strtotime($chg_start_date. "+ {$days_diff_base} days"));      // 변경유효기간 종료일
?>

<!doctype html>
<head>
    <meta charset="UTF-8">
    <title>게시판</title>
    <link rel="stylesheet" type="text/css" href="/css/jquery-ui.css" />
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
	      integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="/css/popup.css">
    <script>
        function resizeWindow(win)    {
            var wid = win.document.body.offsetWidth + 30;
            var hei = win.document.body.offsetHeight + 40;        //30 과 40은 넉넉하게 하려는 임의의 값임

            win.resizeTo(wid,hei);
        }
    </script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" 
	        integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

    <script type="text/javascript" src="/js/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="/js/jquery-ui.js"></script>
</head>
<body onload="check()">
<div id="sign_container">
    <div class="center-align">
        <div class="login_box">
            <form method="post" action="membership_pause_ok.php" name="memform">
                <div id="table-container">
                    <div class="margin-control">
                        <div id="title_margin">
                            <h1 style="display: inline-block">일시정지</h1>
                            <span onclick="window.close();" style="margin-left: 80px; position:absolute; display: inline-block;
							               background-image: url('/image/exit.png'); background-size: cover; width: 30px; height: 50px;"></span>
                        </div>
                        <table cellspacing="0" height="300">
                            <tr>
                                <td align="left" width="150" ><b>회원 ID</b></td>
                                <td align="left" width="200">
								    <input type="text" style="border:none;" size="6" value="<?php echo $board['member_id']; ?>" 
									       class="inph" name="member_id" id="member_id" placeholder="ID" required readonly>
                                    <input type="text" style="border:none;" size="4" value="<?php echo $board['name']; ?>" 
									       class="inph" name="member_name" id="member_name" placeholder="ID" readonly>

                                </td>
                            </tr>
                            <tr>
                                <td align="left" width="150"><b>유효기간</b></td>
                                <td align="left" width="250">
                                    <input type="text" size="9" 
									       class="inph" style="border: none;" name="start_date" id="start_date" 
										   value="<?php echo $board['start_date']; ?>" placeholder="ID" readonly> ~
                                    <input type="text" size="9" 
									       class="inph" style="border: none;" name="due_date" id="due_date" 
										   value="<?php echo $board['due_date']; ?>" placeholder="ID" readonly>
                                </td>
                            </tr>
                            <tr>
                                <td align="left" width="150"><b>일시정지 시작일</b></td>
                                <td align="left" width="200">
								    <input type="date" size="35" id="pause_start_date" 
									       class="inph" name="pause_start_date" value="<?php echo $start_date; ?>" required>
								</td>
                            </tr>
                            <tr>
                                <td align="left" width="150"><b>일시정지 종료일</b></td>
                                <td align="left" width="200">
								    <input type="date" size="35" id="pause_due_date" 
									       class="inph" name="pause_due_date" value="<?php echo $due_date; ?>" required>
								</td>
                            </tr>
							<tr>
                                <td align="left" width="150"><b>변경 유효기간</b></td>
                                <td align="left" width="250">
                                    <input type="text" size="9" 
									       class="inph" style="border: none;" name="chg_start_date" id="chg_start_date" 
										   value="<?php echo $chg_start_date; ?>" placeholder="ID" readonly> ~
                                    <input type="text" size="9" 
									       class="inph" style="border: none;" name="chg_due_date" id="chg_due_date" 
										   value="<?php echo $chg_due_date; ?>" placeholder="ID" readonly>
                                </td>
                            </tr>
                        </table>
                        <div style="margin-top: 20px; text-align: center;">
                            <button type="submit" id="button_submit"  onclick="clicked(event)" 
							        style="background-color: white; background-image: url('/image/add.png'); display:inline-block; 
									       vertical-align:bottom; width: 50px; height: 50px; background-size:cover; 
										   font-weight: bold; font-family: '배달의민족 한나체 Air'; border: none;">
                            <div id="button_submit_text">
                                확 인
                            </div>
                            </button>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>

<script>
    let result = document.querySelector('#result');
    document.body.addEventListener('change', function (e) {
		let today = date_a = new Date();
		let start_date = date_b = new Date(document.getElementById("start_date").value);  // '유효기간 시작일'
		let due_date = date_c = new Date(document.getElementById("due_date").value);      // '유효기간 종료일'
        let date1 = date_d = new Date(document.getElementById("pause_start_date").value); // '일시정지 시작일'
		let date2 = date_e = new Date(document.getElementById("pause_due_date").value);   // '일시정지 종료일'
		let date3 = new Date(document.getElementById("chg_start_date").value);            // '변경 유효기간 시작일'
        let date4 = new Date(document.getElementById("chg_due_date").value);
        let final_date = new Date();
		let days_diff_base = <?php echo $days_diff_base; ?>;                                   // 유효기간 일수 = '유효기간 종료일' - '유효기간 시작일'
        let days_diff;

		date_a = getFormatDate(today);                     
		date_b = getFormatDate(start_date);             // '유효기간 시작일'    YYYYMMDD
		date_c = getFormatDate(due_date);				// '유효기간 종료일'    YYYYMMDD   
		date_d = getFormatDate(date1);					// '일시정지 시작일'    YYYYMMDD    
		date_e = getFormatDate(date2);					// '일시정지 종료일'    YYYYMMDD    
														
        let target = e.target;
        switch (target.id) {
            case 'pause_start_date':    // '변경 유효기간 시작일'                                    
				if (days_diff_base < 8) {
                   document.getElementById("pause_start_date").value = formatDateNow(start_date);
				   alert("유효한 잔여일자가 7일이내이면 일시정지가 불가합니다");
				   break;
				}
                if (date_d < date_b) {                   // '일시정지 시작일' < '유효기간 시작일'
                    date1 = document.getElementById("pause_start_date").value = formatDateNow(start_date);
                    alert("입력된 일자가 유효기간 시작일 보다 빠를 수 없습니다");
                }
                if (date_a < date_b) {                      // '오늘일자' < '유효기간 시작일'
				} else {
					if (date_d < date_a) {                  // 일시정지 시작일' < '오늘일자' 
				      date1 = document.getElementById("pause_start_date").value = formatDateNow(today);
                      alert("입력된 일자가 오늘일자 보다 빠를 수 없습니다");
	                 }
				}
				if (date_d >= date_e) {                     // 일시정지 시작일' >= '일시정지 종료일'
					if (date_d < date_a) {                  // 일시정지 시작일' < '오늘일자' 
						date1 = document.getElementById("pause_start_date").value = formatDateNow(today);       // '오늘일자'
					} else {
                        date1 = document.getElementById("pause_start_date").value = formatDateNow(start_date);  // '유효기간 시작일'
					}
					alert("일시정지 시작일이 종료일보다 같거나 늦을 수 없습니다");					
				}

                date1 = new Date(date1);
			    days_diff = (due_date - date1) / 86400000;                           // '유효기간 종료일' - '일시정지 시작일' / 86400000(하루 초: 24* 60* 60 * 10000)

//                date1.setDate(date1.getDate() + <?php echo $days_diff_base; ?>);        // 앞에서 주석표시를 했음에도 $days가 정의되지 않았다고 오류가 발생함 

				final_date = date3;
				final_date.setDate(final_date.getDate() + days_diff);
                document.getElementById("chg_due_date").value = formatDateNow(final_date);        // '변경 유효기간 종료일'
                break;

            case 'pause_due_date':   // '변경 유효기간 종료일'
                days_diff = (date2 - date1) / 86400000;                              // '일시정지 종료일' - '일시정지 시작일' / 86400000(하루 초: 24* 60* 60 * 10000)
                if (days_diff < 7) { 
				    days_diff = 6;
					alert("입력된 일자가 일시정지 최소 기간인 7일을 넘어야 합니다.");                   
				} 
                final_date = new Date(date1);
				final_date.setDate(final_date.getDate() + days_diff);
                date2 = document.getElementById("pause_due_date").value = formatDateNow(final_date);  // '일시정지 종료일'  

				final_date = new Date(date2);
				days_diff = 1;
				final_date.setDate(final_date.getDate() + days_diff);
                date3 = document.getElementById("chg_start_date").value = formatDateNow(final_date);  // '변경 유효기간 시작일'

				days_diff = (due_date - date1) / 86400000;                            // '유효기간 종료일' - '일시정지 시작일' / 86400000(하루 초: 24* 60* 60 * 10000)
                final_date = new Date(date3);
                final_date.setDate(final_date.getDate() + days_diff);
                document.getElementById("chg_due_date").value = formatDateNow(final_date);        // '변경 유효기간 종료일'
                break;

			default:
                break;
         }

    });
</script>
<script>
    function formatDateNow(date) {
        var d = new Date(date),
            month = '' + (d.getMonth() + 1),
            day = '' + (d.getDate()),
            year = d.getFullYear();

        if (month.length < 2)
            month = '0' + month;
        if (day.length < 2)
            day = '0' + day;

        return [year, month, day].join('-');
    }

/* 날짜 yyyyMMdd format으로 변환  */  
	function getFormatDate(date){
		var year = date.getFullYear();              //yyyy
		var month = (1 + date.getMonth());          //M
		month = month >= 10 ? month : '0' + month;  //month 두자리로 저장
		var day = date.getDate();                   //d
		day = day >= 10 ? day : '0' + day;          //day 두자리로 저장
		return  year + '' + month + '' + day;       //''에 '-' 추가하여 yyyy-mm-dd 형태 생성 가능
	}

</script>

</body>
</html>
