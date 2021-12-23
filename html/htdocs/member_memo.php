<?php
include $_SERVER['DOCUMENT_ROOT']."/db.php"; /* db load */
?>
<!doctype html>
<head>
    <meta charset="UTF-8">
    <title>게시판</title>
    <link rel="stylesheet" type="text/css" href="/css/jquery-ui.css" />
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="/css/memo.css">
    <script>
        function resizeWindow(win)    {

            var wid = win.document.body.offsetWidth + 30;

            var hei = win.document.body.offsetHeight + 40;        //30 과 40은 넉넉하게 하려는 임의의 값임

            win.resizeTo(wid,hei);

        }
    </script>

    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

    <script type="text/javascript" src="/js/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="/js/jquery-ui.js"></script>
    <script type="text/javascript" src="/js/common.js"></script>
    <?php
    $bno = $_GET['member_id'];
    $sql2 = mq("select * from member where member_id='".$bno."'");
    $board = $sql2->fetch_array();
    ?>

</head>
<body style="text-align: center;" onload="myFunction()">
<script>
    function myFunction() {
        document.getElementById("memo").value = "<?php echo $board['memo']; ?>";
    }
</script>
<div id="board_write">
    <div id="write_area">
        <form action="/memo_ok.php?phone_number=<?php echo $board['phone_number']; ?>" method="post">
        <div id="in_title">
        <h1 style="display: inline-block;"><?php echo $board['name']; ?></h1>
            <span onclick="window.close();" style="margin-left: 90px; position:absolute; display: inline-block;background-image: url('/image/exit.png'); background-size: cover; width: 30px; height: 50px;"></span>
        </div>
    <div class="wi_line"></div>
        <div id="in_content">
        <textarea style="width: 300px; height: 300px;" name="memo" id="memo"></textarea>
        </div>
    <div class="bt_se">
        <button type="submit" class="btn btn-outline-dark">메모</button>
    </div>
    </form>
    </div>
    </div>
</body>
    </html>