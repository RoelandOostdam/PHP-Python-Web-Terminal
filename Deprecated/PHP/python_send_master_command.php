<?php
include_once 'conn.php';
$command = $_GET['command'];
$thread = '0';

$sth = $conn->prepare("INSERT INTO python_remote_handler (thread, process_name) VALUES ('$thread', '$command')");
$sth->execute();

header('location: python_commander.php');

?>