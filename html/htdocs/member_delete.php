<?php
include $_SERVER['DOCUMENT_ROOT']."/db.php";
    $bno = $_GET['phone_number'];
    $sql4 = mq("select * from member where phone_number='".$bno."'");
    $created = 'admin';
    $searchid = $sql4->fetch_array();
    if($searchid['created_by'] == $created) {
        $sql = mq("delete from member where phone_number='".$bno."'");
        echo '<script type="text/javascript">alert("삭제되었습니다.");window.opener.location.reload();window.close();</script>';
    }
    else {
        echo '<script type="text/javascript">alert("삭제할 권한이 없습니다.");</script>';
    }
?>