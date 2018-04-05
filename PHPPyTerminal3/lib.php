<?php
$con = mysqli_connect("localhost","oemraw","Ramdew123Curry","terminal_data");
if (mysqli_connect_errno()){
    print "Failed to connect to MySQL: " . mysqli_connect_error();
}

if($_GET['action']=='update_feed'){
    $sql = "SELECT * FROM terminal_feed ORDER BY datetime ASC";
    if ($result=mysqli_query($con,$sql)){
      	while ($row=mysqli_fetch_row($result)){
      		$feed_id = $row[0];
      		$feed_thread = $row[1];
      		$feed_datetime = date("D H:i:s",strtotime($row[2]));
      		$feed_text = $row[3];

      		if(substr($feed_text, 0, 8)=='##input:'){
      			print('User : '.$feed_datetime.' >>'.substr($feed_text, strpos($feed_text, "##input:") + 8));
      		} else {
    			print($feed_thread.' : '.$feed_datetime.' >>'.$feed_text);
      		}
            print "\n";
    	}
    }
    mysqli_close($con);
} elseif($_GET['action']=='send_command'){
    $command = "##input:".$_GET['command'];
    $result = mysqli_query($con,"INSERT INTO terminal_feed (thread_id, feed) VALUES (0, '$command')");
    header('location: index.php');
} elseif($_GET['action']=='refresh_threads'){
    $sql = "SELECT * FROM terminal_threads ORDER BY status_datetime ASC";
    if ($result=mysqli_query($con,$sql)){
        while ($row=mysqli_fetch_row($result)){
            $thread_id = $row[1];
            $thread_status = $row[2];
            $interval = date_diff(date_create($row[3]), date_create(Date('Y-m-d H:i:s.u')));
            $thread_datetime = $interval->format('%i:%S');

            print "<tr class='success'><td>$thread_id</td><td>$thread_datetime</td><td>$thread_status</td></tr>";
        }
    }
}
?>