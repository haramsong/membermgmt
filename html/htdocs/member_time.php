<?php
include $_SERVER['DOCUMENT_ROOT']."/db.php"; /* db load */

date_default_timezone_set('Asia/Seoul');
$num = $_GET['member_id'];
$sql = mq("select a.member_id, a.name, a.phone_number, b.type, b.start_date, b.due_date
                            from member as a left outer join transaction as b on a.member_id = b.member_id where a.member_id = $num order by a.member_id, b.start_date desc");
$board = $sql -> fetch_array();
$start_date = strtotime($board['start_date']);
$due_date = strtotime($board['due_date']);
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
<body onload="check()">
<div id="sign_container">
    <div class="center-align">
        <div class="login_box">
            <form method="post" action="membership_transfer_ok.php" name="memform">
                <div id="table-container">
                    <div class="margin-control">
                        <div id="title_margin">
                            <h1 style="display: inline-block">상세 내역</h1>
                            <span onclick="window.close();" style="margin-left: 80px; position:absolute; display: inline-block;background-image: url('/image/exit.png'); background-size: cover; width: 30px; height: 50px;"></span>
                        </div>
                        <table cellspacing="0" height="100">
                            <tr>
                                <td align="left" width="150" ><b>이름</b></td>
                                <td align="left" width="200"><input type="text" style="border:none;" size="4" value="<?php echo $board['name']; ?>" class="inph" name="member_name" id="member_name" placeholder="ID" readonly></td>
                            </tr>
                            <tr>
                                <td align="left" width="150" ><b>전화번호</b></td>
                                <td align="left" width="200"><input type="text" style="border:none;" size="10" value="<?php echo $board['phone_number']; ?>" class="inph" name="phone_number" id="phone_number" readonly>
                                </td>
                            </tr>
                            <tr>
                                <table cellspacing="0" style="border: 1px solid black;">
                                    <tr style="border: 1px solid black;">
                                        <td style="padding: 0; font-weight: bold; border: 1px solid black; background-color: #ffe8a1;" align="center" width="130">시작일</td>
                                        <td style="padding: 0; font-weight: bold; border: 1px solid black; background-color: #ffe8a1;" align="center" width="130">종료일</td>
                                        <td style="padding: 0; font-weight: bold; border: 1px solid black; background-color: #ffe8a1;" align="center" width="80">유형</td>
                                    </tr>
                                    <?php
                                        $sql2 = mq('select * from transaction where member_id = "'.$num.'" order by start_date desc');
                                        while($board2 = $sql2 -> fetch_array()) {
                                    ?>
                                        <tr>
                                            <td style="border: 1px solid black;" align="left" width="130"><?php echo $board2['start_date']; ?></td>
                                            <td style="border: 1px solid black;" align="left" width="130"><?php echo $board2['due_date']; ?></td>
                                            <td style="border: 1px solid black;" align="left" width="80">
                                                <?php
                                                    if ($board2['type'] == 'A') {
                                                        echo "등 록";
                                                    } elseif ($board2['type'] == 'B') {
                                                        echo "양 도";
                                                    } elseif ($board2['type'] == 'C') {
                                                        echo "변 경";
                                                    } else {
                                                        echo "일시정지";
                                                    }
                                                ?>
                                            </td>
                                        </tr>
                                    <?php } ?>
                                </table>
                            </tr>
                        </table>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>

</body>
</html>