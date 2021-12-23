<script>
    let r == confirm("등록하시겠습니까?");
    if (r == true) {
        alert("등록되었습니다.");
        window.open("/membership_ok.php");
    } else {
        window.close(); window.opener.location.reload();
    }
    </script>