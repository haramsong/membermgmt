<?php
include  $_SERVER['DOCUMENT_ROOT']."/db.php";
?>
<!doctype html>
<head>
    <meta charset="UTF-8">
    <title>게시판</title>
    <link rel="stylesheet" href="/css/memo.css">


    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

</head>
<body style="text-align: center;" onload="myFunction()">
<div id="board_write">
    <div id="write_area">
        <form action="write_ok.php" method="post">
            <div id="in_title">
                <h1 style="display: inline-block;">글 쓰기</h1>
                <span onclick="window.close();" style="margin-left: 90px; position:absolute; display: inline-block;background-image: url('/image/exit.png'); background-size: cover; width: 30px; height: 50px;"></span>
            </div>
            <div class="wi_line"></div>
            <div id="in_content">
                <textarea style="width: 300px; height: 30px;" name="title" id="title"></textarea>
            </div>
            <div id="in_content">
                <textarea style="width: 300px; height: 300px;" name="content" id="content"></textarea>
            </div>
            <div class="bt_se">
                <button type="submit" class="btn btn-outline-dark">등록</button>
            </div>
        </form>
    </div>
</div>
</body>
</html>