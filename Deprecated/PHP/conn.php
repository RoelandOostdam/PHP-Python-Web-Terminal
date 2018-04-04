<?php

//In case you want to use config files

// $fp = fopen('config/conn_ip', 'r');
// $ip = fread($fp, filesize('config/conn_ip'));

// $fp = fopen('config/conn_user', 'r');
// $user = fread($fp, filesize('config/conn_user'));

// $fp = fopen('config/conn_pass', 'r');
// $pass = fread($fp, filesize('config/conn_pass'));

// $fp = fopen('config/conn_db', 'r');
// $db = fread($fp, filesize('config/conn_db')-1);

$ip = 'localhost';
$user = 'user';
$pass = 'password';
$db = 'python_data';

try {
$conn = new PDO('mysql:host=' . $ip . ';dbname=' . $db, $user, $pass);
} catch (PDOException $e) {
	echo 'Misconfigured database: ' . $e->getMessage();
}
//
?>
