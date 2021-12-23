<?php
include $_SERVER['DOCUMENT_ROOT']."/db.php";

echo
date_default_timezone_set('Asia/Seoul');
$member_id = $_POST['member_id'];
$transfer_id = $_POST['transfer_id'];
$start_date = $_POST['start_date'];
$due_date = $_POST['due_date'];
$start_date1 = date('Y-m-d', strtotime($start_date));
$due_date1 = date('Y-m-d', strtotime($due_date));
$transfer_start_date = $_POST['transfer_start_date'];
$transfer_start_date1 = date('Y-m-d', strtotime($transfer_start_date));
$transfer_due_date = $_POST['transfer_due_date'];
$transfer_due_date1 = date('Y-m-d', strtotime($transfer_due_date));
$now = date_default_timezone_get();
$now1 = date('Y-m-d', strtotime($now));

$created_by = 'admin';
$created_date = date('Y-m-d H:i:s', strtotime($now));
$changed_by = 'admin';
$changed_date = date('Y-m-d H:i:s', strtotime($now));
if (strtotime($transfer_start_date) <= strtotime($now) & strtotime($now) < strtotime($transfer_due_date)) {
    $sql = mq("update time_manage set due_date = '".$now1."', changed_by = '".$changed_by."', changed_time = '".$changed_date."'
                    where member_id='".$member_id."' and due_date='".$transfer_due_date1."'");
    $sql = mq("select * from time_manage where member_id = '".$member_id."'");
    while($board = $sql ->fetch_array()){
                    echo $board['member_id'];
                    echo $board['start_date'];
                    echo $board['due_date'];
                }
    } else {
    $sql = mq("delete from time_manage where member_id = '" . $member_id . "' and due_date = '" . $transfer_due_date1 . "'");
}
$sql = mq("update time_manage set due_date = '".$due_date1."', changed_by = '".$changed_by."', changed_time = '".$changed_date."' where member_id='".$transfer_id."'");
//$sql1 = mq("insert into time_manage(member_id, start_date,due_date,created_by,created_time,changed_by,changed_time)
//        values('".$transfer_id."','".$start_date1."','".$due_date1."','".$created_by."','".$created_date."','".$changed_by."','".$changed_date."',);");
$sql = mq("select * from time_manage where member_id = '".$transfer_id."'");
while($board = $sql ->fetch_array()){
    echo $board['member_id'];
    echo $board['start_date'];
    echo $board['due_date'];
}
?>
<meta charset="utf-8" />
<!--<script type="text/javascript">alert('등록이 완료되었습니다.'); window.close(); window.opener.location.reload();</script>-->
<!--<meta http-equiv="refresh" content="0 url=/">-->
