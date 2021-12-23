<?php
include $_SERVER['DOCUMENT_ROOT']."/db.php"; /* db load */
$num = $_GET['member_id'];
$sql = mq("select a.member_id, a.name, a.phone_number, b.start_date, b.due_date 
                            from member as a left outer join time_manage as b on a.member_id = b.member_id where a.member_id = $num order by a.member_id, b.start_date desc");
$board = $sql -> fetch_array();
$start_date = $board['start_date'];
$start_date = strtotime($start_date);
$due_date = $board['due_date'];
$due_date = strtotime($due_date);
date_default_timezone_set('Asia/Seoul');
$today = date_default_timezone_get();
$today = date('Y-m-d',strtotime($today));
$days = round(($due_date - strtotime($today)) / 86400); //초 * 분 * 시간 = 86400
$new_date = date('Y-m-d', strtotime($today. " + {$days} days"));
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
                            <h1 style="display: inline-block">회원권 양도</h1>
                            <span onclick="window.close();" style="margin-left: 80px; position:absolute; display: inline-block;background-image: url('/image/exit.png'); background-size: cover; width: 30px; height: 50px;"></span>
                        </div>
                        <table cellspacing="0" height="300">
                            <tr>
                                <td align="left" width="150" ><b>회원 ID</b></td>
                                <td align="left" width="200"><input type="text" style="border:none;" size="6" value="<?php echo $board['member_id']; ?>" class="inph" name="member_id" id="member_id" placeholder="ID" required readonly>
                                    <input type="text" style="border:none;" size="4" value="<?php echo $board['name']; ?>" class="inph" name="member_name" id="member_name" placeholder="ID" readonly>

                                </td>
                            </tr>
                            <tr>
                                <td align="left" width="150"><b>유효기간</b></td>
                                <td align="left" width="250">
                                    <input type="text" size="9" class="inph" style="border: none;" name="transfer_start_date" id="transfer_start_date" value="<?php echo $board['start_date']; ?>" placeholder="ID" readonly> ~
                                    <input type="text" size="9" class="inph" style="border: none;" name="transfer_due_date" id="transfer_due_date" value="<?php echo $board['due_date']; ?>" placeholder="ID" readonly>
                                </td>
                            </tr>
                            <tr>
                                <td align="left" width="150" ><b>양도대상 회원 ID</b></td>
                                <td align="left" width="200"><input type="text" size="5" class="inph" name="transfer_id" id="transfer_id" placeholder="ID" required>
                                    <input type="text" style="border:none;" value="" size="4" class="inph" id="transfer_name" readonly>
                                    </td>
                            </tr>
                            <tr>
                                <td align="left" width="150"><b>시작일</b></td>
                                <td align="left" width="200"><input type="date" size="35" id="start_date" class="inph" name="start_date" value="<?php echo $today; ?>" required></td>
                            </tr>
                            <tr>
                                <td align="left" width="150"><b>종료일</b></td>
                                <td align="left" width="200"><input type="date" size="35" id="due_date" class="inph" name="due_date" value="<?php echo $new_date; ?>" required readonly></td>
                            </tr>
                        </table>
                        <div style="margin-top: 20px; text-align: center;">
                            <button type="submit" id="button_submit" onclick="clicked(event)" style="background-color: white; background-image: url('/image/add.png'); display:inline-block; vertical-align:bottom; width: 50px; height: 50px; background-size:cover; font-weight: bold; font-family: '배달의민족 한나체 Air'; border: none;">
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
        switch (target.id) {
            case 'transfer_id':
                document.getElementById("transfer_name").value = "";
                <?php
                    $sql = mq("select * from member");

                    while($board = $sql->fetch_array())
                    {
                        $num = $board['member_id'];
                        $sql3 = mq("select * from time_manage where member_id = '".$num."' order by start_date desc limit 1");
                        while($board1 = $sql3 -> fetch_array()) {
                            $due_date_compare = $board1['due_date'];
                            $due_date_compare = strtotime($due_date_compare);
                            $due_date_set = date('Y-m-d', strtotime($board1['due_date'] . ' + 1 day'));
                        }
                    ?>
                    if (document.getElementById("transfer_id").value == <?php echo $board['member_id'];?>) {
                        document.getElementById("transfer_name").value = "<?php echo $board['name'];?>";
                        <?php
                            if( $due_date_compare > strtotime($today)) {
                                $new_add_date = date('Y-m-d', strtotime($due_date_set. " + {$days} days"));
                         ?>
                            //alert("<?php //echo date('Y-m-d', $due_date_compare); ?>//");
                            document.getElementById("start_date").value = "<?php echo date('Y-m-d', strtotime($due_date_set)); ?>";
                            document.getElementById("due_date").value = "<?php echo $new_add_date; ?>";
                        <?php } ?>
                    }
                <?php } ?>
                break;
            case 'start_date':
                let date1 = new Date(document.getElementById("start_date").value);
                date1.setDate(date1.getDate() + <?php echo $days; ?>);
                document.getElementById("due_date").value = formatDateNow(date1);
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
</script>

</body>
</html>