<?php
include  $_SERVER['DOCUMENT_ROOT']."/db.php";
$date_now = date_default_timezone_get();
$date_now = strtotime($date_now);
?>
<!doctype html>
<head>
    <meta charset="UTF-8">
    <title>게시판</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="css/tablestyle.css">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
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
            <a href="/index.php"><span style="margin-left: 20px;background-size: cover;display: inline-block; background-image: url('/image/exit.png'); width: 25px; height:35px;"></span></a>

            <div id="write_btn">
                <div style="display:inline-block; margin-left: 30px; margin-right:30px; margin-top:30px;">
<!-- 상세정보-->
                <button id="button2" onclick="
                if(k == undefined) {
                    alert('회원 선택을 하십시오.');
                    exit();
                }
                 let url_code2 = `/member_change.php?member_id=${k}`;
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
                    if (end_date <= date_now) {
                        alert('양도일수가 부족합니다.');
                        exit();
                    }
                    let url_code3 = `/membership_transfer.php?member_id=${k}`;
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
                    if (end_date <= date_now) {
                        alert('일시정지 대상이 아닙니다.');
                        exit();
                    }
                    let url_code4 = `/membership_pause.php?member_id=${k}`;
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
                <button id="button1" onclick="window.open('signin.php','member', 'width=495, height=850,top=100,left=500,resizable=no');">
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
<!--                <th width="90">생년월일</th>-->
<!--                <th width="50">성별</th>-->
<!--                <th width="200">주소</th>-->
<!--                <th width="100">차량 번호</th>-->
<!--                <th width="200">이메일</th>-->
<!--                <th width="50">등급</th>-->
<!--                <th width="100">최초 등록일</th>-->
            </tr>
            </thead>
            <?php
            if(isset($_GET['page'])){
                $page = $_GET['page'];
            }else{
                $page = 1;
            }
            $getsql = mq("select * from member");
            $row_num = mysqli_num_rows($getsql); //게시판 총 레코드 수
            $list = 30; //한 페이지에 보여줄 개수
            $block_ct = 5; //블록당 보여줄 페이지 개수

            $block_num = ceil($page/$block_ct); // 현재 페이지 블록 구하기
            $block_start = (($block_num - 1) * $block_ct) + 1; // 블록의 시작번호
            $block_end = $block_start + $block_ct - 1; //블록 마지막 번호

            $total_page = ceil($row_num / $list); // 페이징한 페이지 수 구하기
            if($block_end > $total_page) $block_end = $total_page; //만약 블록의 마지박 번호가 페이지수보다 많다면 마지박번호는 페이지 수
            $total_block = ceil($total_page/$block_ct); //블럭 총 개수
            $start_num = ($page-1) * $list; //시작번호 (page-1)에서 $list를 곱한다.

            $sql = mq("select a.member_id, a.name, a.phone_number, b.start_date, b.due_date 
                            from member as a left outer join time_manage as b on a.member_id = b.member_id
                            order by a.member_id, b.start_date desc
                            ");
            $old = '';
            while($board = $sql->fetch_array())
            {
                $new = $board['member_id'];
                if ($new == $old) {
                    continue;
                }
                $start_date = $board['start_date'];
                $start_date = strtotime($start_date);
                $due_date = $board['due_date'];
                $due_date = strtotime($due_date);
                $warning_date = strtotime("-1 months", $due_date);
                if($due_date >= $date_now && $warning_date <= $date_now) {
                    $status = 'status_red';
                } elseif($date_now < $start_date) {
                    $status = 'status_yellow';
                } elseif($date_now < $due_date && $date_now > $start_date) {
                    $status = 'status_green';
                } else {
                    $status = 'status_gray';
                }
                ?>
                <tbody>
                <script>
                    let k;
                    let j;
                </script>
                <tr class="get_id" onclick="
                k = document.getElementById(<?php echo $board['member_id']; ?>).getAttribute('value');
                j = document.getElementById(<?php echo $board['member_id']; ?>).getAttribute('data_date');
                let b = document.getElementsByClassName('get_id');
                let i;
                for (i=0; i < b.length; i++) {
                    b[i].style.backgroundColor = '#FFFFFF';
                    }
                document.getElementById(<?php echo $board['member_id']; ?>).style.backgroundColor = '#C8C8C8';" id="<?php echo $board['member_id']; ?>"
                    value="<?php echo $board['member_id']; ?>" data_date="<?php echo $board['due_date']; ?>">
                    <td width="40"><span class="<?php echo $status; ?>"></span></td>
                    <td width="80"><?php echo $board['member_id']; ?></td>
                    <td width="100"><?php echo $board['name']; ?></td>
                    <td width="110" ><?php echo $board['phone_number']; ?></td>
                    <td width="100"><?php echo $board['start_date']; ?></td>
                    <td width="100"><?php echo $board['due_date']; ?></td>
                </tr>
                </tbody>

            <?php $old = $board['member_id'];
            } ?>
        </table>
    </div>

</div>

</body>
</html>