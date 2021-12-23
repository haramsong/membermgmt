<?php
include  $_SERVER['DOCUMENT_ROOT']."/db.php";

if (isset($_SESSION['id'])) {
    echo "<script>window.open('/write.php', 'member', 'width=400, height=600,top=200,left=500,resizable=no')</script>";
} else {
    echo "<script>alert('글을 쓸 권한이 없습니다.. 로그인 해주시기 바랍니다.'); history.back();</script>";
}
?>