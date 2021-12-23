<?php
include  $_SERVER['DOCUMENT_ROOT']."/db.php";
?>
<!doctype html>
<head>
    <meta charset="UTF-8">
    <title>게시판</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="/css/bootstrap.css">
    <link rel="stylesheet" href="/css/style.css">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <script src="/js/bootstrap.js"></script>
</head>
<body>
<div id="container">
    <div id="board_area">
        <div id="title_margin">
            <div id="write_btn">
                <a href="/index.php"><span style="margin-right: 60px;background-size: cover;display: inline-block; background-image: url('/image/exit.png'); width: 50px; height:80px;"></span></a>
            </div>
            <h1>물품 관리</h1>
        </div>
        <div id="content">
        <span class="content-icon" onclick="signin()">
            <div class="manage_icon1"></div>
            <div style="display:block;">상품 서비스 구매/판매</div>
        </span>
            <span class="content-icon">
                <div class="manage_icon2"></div>
                <div style="display:block;">회원권 등록</div>
        </span>
            <span class="content-icon">
            <div class="manage_icon3"></div>
            <div style="display:block;">회원권 일시정지</div>
        </span>
        <span class="content-icon">
            <div class="manage_icon4"></div>
            <div style="display:block;">회원권 양도</div></span>
        </div>
    </div>
</div>
</body>
</html>