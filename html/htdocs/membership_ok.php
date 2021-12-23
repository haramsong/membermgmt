<?php
include $_SERVER['DOCUMENT_ROOT']."/db.php";

echo
date_default_timezone_set('Asia/Seoul');
$member_id = $_POST['member_id'];
$start_date = $_POST['start_date'];
$start_date = date('Y-m-d', strtotime($start_date));
$type = 'A';
$due_date = $_POST['due_date'];
$due_date = date('Y-m-d', strtotime($due_date));
$created_by = 'admin';
$now = date_default_timezone_get();
$created_time = date('Y-m-d H:i:s', strtotime($now));
$changed_by = 'admin';
$changed_time = date('Y-m-d H:i:s', strtotime($now));

$sql = mq("insert into transaction (member_id,type,start_date,due_date,created_by,created_time,changed_by,changed_time) 
values('".$member_id."','".$type."','".$start_date."','".$due_date."','".$created_by."','".$created_time."','".$changed_by."','".$changed_time."');");
?>
<meta charset="utf-8" />
<script type="text/javascript">alert('회원권 등록이 완료되었습니다.'); window.close(); window.opener.location.reload();</script>