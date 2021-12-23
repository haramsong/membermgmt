<?php
include $_SERVER['DOCUMENT_ROOT']."/db.php"; /* db load */
?>
<!doctype html>
<head>
    <meta charset="UTF-8">
    <title>게시판</title>
    <link rel="stylesheet" type="text/css" href="/css/jquery-ui.css" />
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="/css/style.css">


    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

    <script type="text/javascript" src="/js/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="/js/jquery-ui.js"></script>
    <script type="text/javascript" src="/js/common.js"></script>
</head>
<body>
<?php
$bno = $_GET['num']; /* bno함수에 idx값을 받아와 넣음*/
$sql = mq("select * from notice where num='".$bno."'"); /* 받아온 idx값을 선택 */
$board = $sql->fetch_array();
?>
<div id="div-container">
    <div id="board_read">
        <h2><?php echo $board['title']; ?></h2>
        <div id="user_info">
            <span>작성자 : <?php echo $board['created_by']; ?></span><span class="right-float"> 작성일 : <?php echo $board['created_time']; ?></span>
            <div id="bo_line"></div>
        </div>
        <!-- 목록, 수정, 삭제 -->
        <div id="bo_ser">
            <ul>
                <li><a href="/notice.php">* 목록으로 </a></li>
<!--                <li><a href="modify_verify.php?num=--><?php //echo $board['num']; ?><!--">* 수정 </a></li>-->
<!--                <li><a href="delete.php?num=--><?php //echo $board['num']; ?><!--">* 삭제 </a></li>-->
            </ul>
        </div>
        <div id="bo_content">
            <?php echo nl2br("$board[content]"); ?>
        </div>
    </div>
</div>
</body>
</html>
