<?php
include $_SERVER['DOCUMENT_ROOT']."/db.php"; /* db load */
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

    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

    <script type="text/javascript" src="/js/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="/js/jquery-ui.js"></script>
    <script type="text/javascript" src="/js/common.js"></script>
</head>
<body>
<?php
$bno = $_GET['member_id'];
$sql2 = mq("select a.*, b.start_date, b.due_date 
                from member as a left outer join time_manage as b on a.member_id = b.member_id  
                where a.member_id='".$bno."' order by b.start_date desc limit 1");
$board = $sql2->fetch_array();
$emailarr = explode('@', $board['email']);
$emailhead = $emailarr[0];
$emailadd = $emailarr[1];
$radio_value = $board['gender'];
?>
<script>
    function delete_member() {
        if(confirm("정말로 삭제하시겠습니까?"))
        {
            location.href="/member_delete.php?phone_number=<?php echo $board['phone_number']; ?>"
        }
        else {
        }
    }
    //function gender_check() {
    //    if(<?php //echo $board['gender']; ?>// == '남')
    //    {
    //        alert(document.getElementById("male").checked);
    //    }
    //    else if(<?php //echo $board['gender']; ?>// == '여')
    //    {
    //        alert(document.getElementById("female").checked);
    //    }
    //}
</script>
<div id="sign_container">
    <div class="center-align">
        <div class="login_box">
            <form method="post" action="member_change_ok.php" name="memform">
                <div id="table-container">
                    <div class="margin-control">
                        <div id="title_margin">
                        <h1 style="display: inline-block">회원 정보</h1>
                            <span onclick="window.close();" style="margin-left: 90px; position:absolute; display: inline-block;background-image: url('/image/exit.png'); background-size: cover; width: 30px; height: 50px;"></span>
                        </div>
                        <table cellspacing="0" height="470">
                            <tr>
                                <td align="left" width="250" ><b>이름</b></td>
                                <td align="left" width="200"><input type="text" size="35" class="inph" name="name" id="name" value="<?php echo $board['name']; ?>" placeholder="이름" required></td>
                            </tr>
                            <tr>
                                <td align="left" width="250"><b>생년월일</b></td>
                                <td align="left" width="200"><input type="text" size="35" class="inph" name="birth_date" value="<?php echo $board['birth_date']; ?>" id="birth_date" placeholder="생년월일" required></td>
                            </tr>
                            <tr>
                                <td align="left" width="250"><b>성별</b></td>
                                <td align="left" width="200">
<!--                                    남자 radio button-->
                                    <?php
                                    if ($radio_value == '남') {
                                        echo "<input type=\"radio\" id=\"male\" name=\"gender\" class=\"inph\" value=\"남\" style=\"margin-left:10px\" checked>";
                                    } else {
                                        echo "<input type=\"radio\" id=\"male\" name=\"gender\" class=\"inph\" value=\"남\" style=\"margin-left:10px\">";
                                    }
                                ?>
                                    남</input>
<!--                                    여자 radio button-->
                                <?php
                                if ($radio_value == '남') {
                                    echo "<input type=\"radio\" id=\"female\" name=\"gender\" value=\"여\">";
                                } else {
                                    echo "<input type=\"radio\" id=\"female\" name=\"gender\" value=\"여\" checked>";
                                }
                                ?>
                                    여</input>
                                </td>
                            </tr>
                            <tr>
                                <td align="left" width="250"><b>이메일</b></td>
                                <td align="left" width="400"><input type="text" class="inph" value="<?php echo $emailhead; ?>" name="email" style="margin-right: 10px" required>@<select name="emadress" class="inph" value="<?php echo $emailadd; ?>" style="margin-left: 10px" required>
                                        <option value="naver.com">naver.com</option>
                                        <option value="nate.com">nate.com</option>
                                        <option value="hanmail.com">hanmail.com</option>
                                    </select></td>
                            </tr>
                            <tr>
                                <td align="left" width="250"><b>전화번호</b></td>
                                <td align="left" width="200"><input type="text" size="35" class="inph" name="phone_number" value="<?php echo $board['phone_number']; ?>" placeholder="전화번호" required></td>
                            </tr>
                            <tr>
                                <td align="left" width="250"><b>주소</b></td>
                                <td align="left" width="200"><input type="text" size="35" class="inph" name="address" value="<?php echo $board['address']; ?>" placeholder="주소" required></td>
                            </tr>
                            <tr>
                                <td align="left" width="200"><b>차량 번호</b></td>
                                <td align="left" width="200"><input type="text" size="35" class="inph" name="car_number" value="<?php echo $board['car_number']; ?>" placeholder="차량 번호"></td>
                            </tr>
                            <tr>
                                <td align="left" width="250"><b>유효기간 시작일</b></td>
                                <td align="left" width="200"><input type="date" size="35" class="inph" name="start_date" value="<?php echo $board['start_date']; ?>" placeholder="시작일" required>
                                <button style="background-color: white; margin-left: 30px;" onclick="">내역 보기</button></td>
                            </tr>
                            <tr>
                                <td align="left" width="250"><b>유효기간 만료일</b></td>
                                <td align="left" width="200"><input type="date" size="35" class="inph" name="due_date" value="<?php echo $board['due_date']; ?>" placeholder="만료일" required></td>
                            </tr>
                            <tr>
                                <td align="left" width="250"><b>리그 등급</b></td>
                                <td align="left" width="200"><input type="text" size="35" class="inph" name="league_grade" value="<?php echo $board['league_grade']; ?>" placeholder="리그 등급" required></td>
                            </tr>
                        </table>
                            <button id="button_submit" type="submit" style="background-color:white; background-size:cover; background-image: url('image/chat.png'); display:inline-block; width: 60px; height: 60px; border: none; margin-top: 20px; position: relative;">
                            <div id="button_submit_text">
                                변경
                            </div>
                            </button>
                        <button id="button_submit" style="display:inline-block; position: absolute; vertical-align:center; margin-top: 20px; margin-left: 50px;  width: 60px; height: 60px;background-size: cover; background-image: url('image/delete.png');" onclick="delete_member();">
                            <div id="button_submit_text">
                                삭제
                            </div>
                        </button>
                        </div>
                    </div>
            </form>
        </div>
    </div>
</div>
</body>
</html>
