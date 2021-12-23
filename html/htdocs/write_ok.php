<?php
include $_SERVER['DOCUMENT_ROOT'] . "/db.php";

date_default_timezone_set('Asia/Seoul');
$id = $_SESSION['id'];
$date = date("Y-m-d");
$sql = mq("insert into notice(title,content,created_by,created_time) values('".$_POST['title']."','".$_POST['content']."','".$id."','".$date."')");
?>

<script type="text/javascript">alert("글쓰기 완료되었습니다.");window.close(); window.opener.location.reload();</script>
<meta http-equiv="refresh" content="0 url=../mrk.php"/>
