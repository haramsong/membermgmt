<?php
session_start();
header('Content-Type: text/html; charset=utf-8'); // utf-8인코딩

$db = new mysqli("localhost","root","hrsong502","club_member_mgmt");
$db->set_charset("utf8");

function mq($sql)
{
    global $db;
    return $db->query($sql);
}
?>