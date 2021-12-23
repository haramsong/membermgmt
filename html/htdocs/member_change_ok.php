<?php
include $_SERVER['DOCUMENT_ROOT']."/db.php";
$bno = $_POST['phone_number'];
$name = $_POST['name'];
$birth_date = $_POST['birth_date'];
$gender = $_POST['gender'];
$email = $_POST['email'].'@'.$_POST['emadress'];
$phone_number = $_POST['phone_number'];
$address = $_POST['address'];

$start_date = $_POST['start_date'];
$start_date = date('Y-m-d', strtotime($start_date));
$due_date = $_POST['due_date'];
$due_date = date('Y-m-d', strtotime($due_date));
$car_number = $_POST['car_number'];
$league_grade = $_POST['league_grade'];
$now = date_default_timezone_get();
$changed_by = 'admin';
$changed_time = date('Y-m-d H:i:s', strtotime($now));

$sql = mq("update member set name='".$name."', birth_date='".$birth_date."', gender='".$gender."', email='".$email."',phone_number='".$phone_number."',
address='".$address."',start_date='".$start_date."',due_date='".$due_date."',car_number='".$car_number."',league_grade='".$league_grade."',changed_by='".$changed_by."',changed_time='".$changed_time."'
where phone_number='".$phone_number."'"); ?>

<script type="text/javascript">alert("수정되었습니다.");window.opener.location.reload();window.close();</script>
<meta http-equiv="refresh" content="0 url=/member_check.php">
