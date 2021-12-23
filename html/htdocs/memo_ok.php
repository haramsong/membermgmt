<?php

include $_SERVER['DOCUMENT_ROOT']."/db.php";
$memo = $_POST['memo'];
$bno = $_GET['phone_number'];
$sql = mq("update member set memo='".$memo."' where phone_number='".$bno."'");
?>

    <script type="text/javascript">alert("완료되었습니다."); window.close(); window.opener.location.reload();</script>
<?php
