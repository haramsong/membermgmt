<?php
include  $_SERVER['DOCUMENT_ROOT']."/db.php";
$sql = mq("select * from manager where id ='admin'");
$board = $sql->fetch_array();
$_SESSION['id'] = $board['id'];
?>
<html>
<head>
    <meta charset="utf-8">
    <title>명지 탁구 클럽</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="css/style.css">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <script src="/js/bootstrap.js"></script>

    <script>
        function signin() {
            window.open("signin.php", "member", "width=495,height=900,top=200,left=500,resizable=no");
        }
    </script>
</head>
<body>
<div id="container">
    <div id="main">
        <div id="helper"></div><div id="line-normal">
            <h1>명 지 탁 구 클 럽</h1>
        </div>
    </div>
    <div id="content">
        <span class="content-icon" onclick="signin()">
            <div class="manage_icon1"></div>
            <div style="display:block;">회원 등록</div>
        </span>
        <a href = "member_check.php"><span class="content-icon">
                <div class="manage_icon2"></div>
                <div style="display:block;">회원 리스트</div>
        </span></a>
        <span class="content-icon" onclick="window.open('/membership.php', 'member', 'width=495, height=500,top=100,left=500,resizable=no')">
        <div class="manage_icon3"></div>
            <div style="display:block;">회원권 등록</div>
        </span>
        <span class="content-icon" onclick="alert('준비중에 있습니다.');">
            <div class="manage_icon4"></div>
            <div style="display:block;">회원권 양도/변경</div></span>
    </div>
</div>
</body>
</html>