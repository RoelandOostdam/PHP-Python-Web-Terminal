<?php
require 'conn.php';
  $sth = $conn->prepare("TRUNCATE python_data;");
  $sth->execute();

  header('location: python_commander.php');

?>