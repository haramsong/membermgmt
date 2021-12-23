<?php
include $_SERVER['DOCUMENT_ROOT']."/db.php";

echo
date_default_timezone_set('Asia/Seoul');
$member_id = $_POST['member_id'];
$type = 'D';
$chg_start_date = date('Y-m-d', strtotime($_POST['chg_start_date']));
$chg_due_date = date('Y-m-d', strtotime($_POST['chg_due_date']));
$created_by = 'admin';
$created_time = date('Y-m-d H:i:s');
$changed_by = 'admin';
$changed_time = date('Y-m-d H:i:s');
$sql = mq("select * from transaction where member_id = '".$member_id."' order by start_date desc limit 1");
$board = $sql->fetch_array();
$doc_source = $board['doc_number'];
$sql = mq("insert into transaction (member_id,type,start_date,due_date,doc_source,created_by,created_time,changed_by,changed_time) 
values('".$member_id."','".$type."','".$chg_start_date."','".$chg_due_date."','".$doc_source."','".$created_by."','".$created_time."','".$changed_by."','".$changed_time."');");
?>
<meta charset="utf-8" />
<script type="text/javascript">alert('일시정지가 완료되었습니다.'); window.close(); window.opener.location.reload();</script>