<?php
include  $_SERVER['DOCUMENT_ROOT']."/db.php";
?>
<!doctype html>
<head>
    <meta charset="UTF-8">
    <title>게시판</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" href="/css/tablestyle.css">


    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <script src="/js/bootstrap.js"></script>
    <script>
        function write_verify() {
            <?php
            if (isset($_SESSION['id'])) {
                echo "window.open('/write.php', 'member', 'width=495, height=900,top=200,left=500,resizable=no');";
            } else {
                echo "alert('글을 쓸 권한이 없습니다.. 로그인 해주시기 바랍니다.'); history.back();";
            }
            ?>
        }
    </script>
</head>
<body>
<div id="container">
    <div id="board_area">
        <div id="title_margin">
            <h1 style="display: inline-block">공지사항</h1>
            <div style="float:right; display: inline-block;">
            <a href="/index.php"><span style="position: absolute;margin-right: 60px;background-size: cover;display: inline-block; background-image: url('/image/exit.png'); width: 40px; height:65px;"></span></a>
            </div>
            </div>
        <table class="list-table">
            <thead>
            <tr>
                <th width="200">제목</th>
                <th width="80">작성자</th>
                <th width="100">작성일</th>
            </tr>
            </thead>
            <?php
            if(isset($_GET['page'])){
                $page = $_GET['page'];
            }else{
                $page = 1;
            }
            $getsql = mq("select * from notice");
            $row_num = mysqli_num_rows($getsql); //게시판 총 레코드 수
            $list = 15; //한 페이지에 보여줄 개수
            $block_ct = 5; //블록당 보여줄 페이지 개수

            $block_num = ceil($page/$block_ct); // 현재 페이지 블록 구하기
            $block_start = (($block_num - 1) * $block_ct) + 1; // 블록의 시작번호
            $block_end = $block_start + $block_ct - 1; //블록 마지막 번호

            $total_page = ceil($row_num / $list); // 페이징한 페이지 수 구하기
            if($block_end > $total_page) $block_end = $total_page; //만약 블록의 마지박 번호가 페이지수보다 많다면 마지박번호는 페이지 수
            $total_block = ceil($total_page/$block_ct); //블럭 총 개수
            $start_num = ($page-1) * $list; //시작번호 (page-1)에서 $list를 곱한다.

            $sql = mq("select * from notice order by created_time desc limit $start_num, $list");
            while($board = $sql->fetch_array())
            {
                $title=$board["title"];
                if(strlen($title)>30)
                {
                    $title=str_replace($board["title"],mb_substr($board["title"],0,30,"utf-8")."...",$board["title"]);
                }
                ?>
                <tbody>
                <tr>
                    <td width="200" align="left"><a href='/read.php?num=<?php echo $board["num"]; ?>'><?php echo $title; ?></a></td>
                    <td width="80"><?php echo $board['created_by'];?></td>
                    <td width="100"><?php echo $board['created_time'];?></td>
                </tr>
                </tbody>
            <?php } ?>
        </table>
        <div id="page_num">
            <ul>
                <?php
                if($page <= 1)
                { //만약 page가 1보다 크거나 같다면
                    echo "<li class='fo_re'>처음</li>"; //처음이라는 글자에 빨간색 표시
                }else{
                    echo "<li><a href='?page=1'>처음</a></li>"; //알니라면 처음글자에 1번페이지로 갈 수있게 링크
                }
                if($page <= 1)
                { //만약 page가 1보다 크거나 같다면 빈값

                }else{
                    $pre = $page-1; //pre변수에 page-1을 해준다 만약 현재 페이지가 3인데 이전버튼을 누르면 2번페이지로 갈 수 있게 함
//                echo "<li><a href='?page=$pre'>이전</a></li>"; //이전글자에 pre변수를 링크한다. 이러면 이전버튼을 누를때마다 현재 페이지에서 -1하게 된다.
                }
                for($i=$block_start; $i<=$block_end; $i++){
                    //for문 반복문을 사용하여, 초기값을 블록의 시작번호를 조건으로 블록시작번호가 마지박블록보다 작거나 같을 때까지 $i를 반복시킨다
                    if($page == $i){ //만약 page가 $i와 같다면
                        echo "<li class='fo_re'>[$i]</li>"; //현재 페이지에 해당하는 번호에 굵은 빨간색을 적용한다
                    }else{
                        echo "<li><a href='?page=$i'>[$i]</a></li>"; //아니라면 $i
                    }
                }
                if($block_num >= $total_block){ //만약 현재 블록이 블록 총개수보다 크거나 같다면 빈 값
                }else{
                    $next = $page + 1; //next변수에 page + 1을 해준다.
//                echo "<li><a href='?page=$next'>다음</a></li>"; //다음글자에 next변수를 링크한다. 현재 4페이지에 있다면 +1하여 5페이지로 이동하게 된다.
                }
                if($page >= $total_page){ //만약 page가 페이지수보다 크거나 같다면
                    echo "<li class='fo_re'>마지막</li>"; //마지막 글자에 긁은 빨간색을 적용한다.
                }else{
                    echo "<li><a href='?page=$total_page'>마지막</a></li>"; //아니라면 마지막글자에 total_page를 링크한다.
                }
                ?>
            </ul>
        </div>
        <div id="write_btn">
            <button onclick="write_verify();" class="btn btn-outline-dark">글쓰기</button>
        </div>
    </div>
</div>
</body>
</html>