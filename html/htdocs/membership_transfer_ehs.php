<?php
include $_SERVER['DOCUMENT_ROOT']."/db.php"; /* db load */
date_default_timezone_set('Asia/Seoul');
$get_id = $_GET['member_id'];
$sql = mq("select a.member_id, a.name, a.phone_number, b.start_date, b.due_date 
             from member as a left outer join time_manage as b 
			   on a.member_id = b.member_id 
			where a.member_id = $get_id 
			      order by a.member_id, b.start_date desc");
$board = $sql -> fetch_array();
$start_date = strtotime($board['start_date']);
$due_date = strtotime($board['due_date']);
$today = date('Y-m-d');                                  // echo $today; -> YYYY-MM-DD(오늘날짜)
$start_date_ymd = date('Y-m-d', $start_date);
$trans_s_days = 0;
if ($start_date_ymd <= $today) {                         // echo $start_date_ymd;  -> YYYY-MM-DD 
   $trans_s_days = 1 ;                      // echo $today; -> YY-MM-DD 형태로 출력
   $start_date_ymd = $today;
}
$trans_start_date = date('Y-m-d', strtotime($start_date_ymd. "+ {$trans_s_days} days"));
$trans_due_date = date('Y-m-d', $due_date);
$days_diff_base = round(($due_date - strtotime($trans_start_date)) / 86400); //초 * 분 * 시간 = 86400
?>

<!doctype html>
<head>
    <meta charset="UTF-8">
    <title>게시판</title>
    <link rel="stylesheet" type="text/css" href="/css/jquery-ui.css" />
    <link rel="stylesheet" 
	      href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
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
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" 
	        integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" 
			crossorigin="anonymous"></script>

    <script type="text/javascript" src="/js/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="/js/jquery-ui.js"></script>
</head>
<body onload="check()">
<div id="sign_container">
    <div class="center-align">
        <div class="login_box">
            <form method="post" action="membership_transfer_ok.php" name="memform">
                <div id="table-container">
                    <div class="margin-control">
                        <div id="title_margin">
                            <h1 style="display: inline-block">회원권 양도</h1>
                            <span onclick="window.close();" style="margin-left: 80px; 
							      position:absolute; display: inline-block; 
							      background-image: url('/image/exit.png'); 
								  background-size: cover; width: 30px; height: 50px;"></span>
                        </div>
                        <table cellspacing="0" height="300">
                            <tr>
                                <td align="left" width="150" ><b>회원 ID</b></td>
                                <td align="left" width="200">
								    <input type="text" style="border:none;" size="6" 
									       value="<?php echo $board['member_id']; ?>" 
									       class="inph" name="member_id" id="member_id" 
										   placeholder="ID" required readonly>
                                    <input type="text" style="border:none;" size="4" 
									       value="<?php echo $board['name']; ?>" 
									       class="inph" name="member_name" id="member_name" 
										   placeholder="ID" readonly>

                                </td>
                            </tr>
                            <tr>
                                <td align="left" width="150"><b>유효기간</b></td>
                                <td align="left" width="250">
                                    <input type="text" size="9" class="inph" style="border: none;" 
									       name="start_date" id="start_date" 
									       value="<?php echo $board['start_date']; ?>" 
										   placeholder="ID" readonly> ~
                                    <input type="text" size="9" class="inph" style="border: none;" 
									       name="due_date" id="due_date" 
									       value="<?php echo $board['due_date']; ?>" 
										   placeholder="ID" readonly>
                                </td>
                            </tr>
                            <tr>
                                <td align="left" width="150" ><b>양도대상 회원 ID</b></td>
                                <td align="left" width="200">
								    <input type="text" size="5" class="inph" name="transfer_id" 
									       id="transfer_id" placeholder="ID" required>
                                    <input type="text" style="border:none;" value="" size="4" 
									       class="inph" id="transfer_name" readonly>
                                    </td>
                            </tr>
                            <tr>
                                <td align="left" width="150"><b>시작일</b></td>
                                <td align="left" width="200">
								    <input type="date" size="35" id="transfer_start_date" 
									       class="inph" name="transfer_start_date" 
								           value="<?php echo $trans_start_date; ?>" required></td>
                            </tr>
                            <tr>
                                <td align="left" width="150"><b>종료일</b></td>
                                <td align="left" width="200">
								    <input type="date" size="35" id="transfer_due_date" 
									       class="inph" name="transfer_due_date"
                                           value="<?php echo $trans_due_date; ?>" 
										   required readonly></td>
                            </tr>
                        </table>
                        <div style="margin-top: 20px; text-align: center;">
                            <button type="submit" id="button_submit" onclick="clicked(event)" 
							        style="background-color: white; 
									       background-image: url('/image/add.png'); 
									       display:inline-block; vertical-align:bottom; 
										   width: 50px; height: 50px; background-size:cover; 
										   font-weight: bold; 
										   font-family: '배달의민족 한나체 Air'; border: none;">
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
    function clicked(e) {
        if (document.getElementById("transfer_name").value == "") {
            e.preventDefault();
            alert('일치하는 회원정보가 없습니다.');
        } else {
			alert(document.getElementById("transfer_name").value);
            if (!confirm('양도하시겠습니까?')) {
                e.preventDefault();
                alert('취소되었습니다.');
                window.close();
            }
        }
    }

    let result = document.querySelector('#result');
    document.body.addEventListener('change', function (e) {
        let target = e.target;
		let trans_id = document.getElementById("transfer_id").value;
		let today = new Date();
        switch (target.id) {
            case 'transfer_id':				
                document.getElementById("transfer_name").value = "";
                if (document.getElementById("member_id").value == trans_id) { 
				    document.getElementById("transfer_id").value = "";
					alert("양도할 회원과 양도받을 회원이 동일할 수 없습니다.");                
					break;
                }
            <?php 
                $turning_count = 0;
			    $sql1 = mq("select * from member");
				$rowcount1 = mysqli_num_rows($sql1);              // $sql1에서 추출된 Record 수 
                while ($board1 = $sql1->fetch_array()) {
				   $turning_count += 1;                           // while문 내부 실행 횟수 
                   $mem_id = $board1['member_id'];
            ?>
                   if (trans_id == <?php echo $board1['member_id'];?>) {
                <?php
					  $sql2 = mq("select * from time_manage  
				                   where member_id = '".$mem_id."' 
								   order by start_date desc limit 1");
				      $rowcount2 = mysqli_num_rows($sql2);        // $sql1에서 추출된 Record 수 
                      while ($board2 = $sql2->fetch_array()) {                      
				  	    $start_date_db = $board2['start_date'];
				 	    $due_date_db = $board2['due_date'];
				     } 
				?>
                      document.getElementById("transfer_name").value 
					     = "<?php echo $board1['name']; ?>";

					  if ("<?php echo $rowcount2; ?>" == 0) {					 
                         document.getElementById("transfer_start_date").value 
							= "<?php echo $today; ?>";
                         document.getElementById("transfer_due_date").value  
						    = "<?php echo  date('Y-m-d', 
						       strtotime($today. " + {$days_diff_base} days"));?>"; }
					  else {
						if ("<?php echo $due_date_db;?>" < "<?php echo $today; ?>"){
							 document.getElementById("transfer_start_date").value 
							= "<?php echo $today; ?>";
                             document.getElementById("transfer_due_date").value  
						    = "<?php echo  date('Y-m-d', 
						       strtotime($today. " + {$days_diff_base} days"));?>"; }
						else {
						  <?php $next_start_date = date('Y-m-d', 
						       strtotime($due_date_db. " + 1 days")); ?>
                          document.getElementById("transfer_start_date").value  
						    = "<?php echo $next_start_date; ?>";
						  document.getElementById("transfer_due_date").value  
						    = "<?php echo  date('Y-m-d', 
						       strtotime($next_start_date. " + {$days_diff_base} days"));?>";
						}
							
					  }
				      break;
                   }
          <?php } ?>
                if ( "<?php echo $rowcount1; ?>" == "<?php echo $turning_count; ?>" 
			        && document.getElementById("transfer_name").value == "") {
					document.getElementById("transfer_id").value = "";
					alert("잘못된 회원번호가 입력되었습니다.");
				} 
				break;
  
			case 'transfer_start_date':
                let trans_sdate = document.getElementById("transfer_start_date").value;
			    if (document.getElementById("transfer_name").value == "" ) {
                    if ("<?php echo $start_date;?>" < "<?php echo $today; ?>"){
                       <?php $next_start_date = date('Y-m-d', 
						   strtotime($today. " + 1 days")); ?>
					   document.getElementById("transfer_start_date").value 
						 = "<?php echo $next_start_date; ?>";
                       document.getElementById("transfer_due_date").value  
						 = "<?php echo date('Y-m-d', 
						     strtotime($next_start_date. " + {$days_diff_base} days"));?>"; }
					else {
                       document.getElementById("transfer_start_date").value  
						 = "<?php echo $start_date; ?>";
					}
					alert("양도대상 회원을 먼저 지정하시오'");
					break;
			    }
                break;
          
            default:
                break;
        }

    });
</script>
</body>
</html>