<?php
	include "conn.php";
	$sql = "UPDATE python_config SET response_time=" . $_POST['level'];
	$conn->query($sql);
?>