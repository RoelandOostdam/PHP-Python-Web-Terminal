<?php
session_start();
$con = mysqli_connect($_SESSION['host'],$_SESSION['user'],$_SESSION['passwd'],"terminal_data");
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
    $command = htmlspecialchars($command, ENT_QUOTES);

    $result = mysqli_query($con,"INSERT INTO terminal_feed (thread_id, feed) VALUES (0, '$command')");
    header('location: index.php');
} elseif($_GET['action']=='refresh_threads'){
    $sql = "SELECT * FROM terminal_threads ORDER BY thread ASC";
    if ($result=mysqli_query($con,$sql)){
        while ($row=mysqli_fetch_row($result)){
            $thread_id = $row[1];
            $thread_status = $row[2];
            $thread_datetime = date_diff(date_create($row[3]), date_create(Date('Y-m-d H:i:s')));
            $interval = $thread_datetime->format('%i%s');
            $interval_s = $thread_datetime->format('%s');

            if($thread_id==0){
                $thread_name = "0: Main";
            } else {
                $thread_name = $thread_id;
            }
            if(substr($thread_status, 0, 4)=='##c:'){
                $class = 'Info';
                $interval = "n/a";
                $thread_status = substr($thread_status, 4);
            } else {
                if($interval<=3){
                    $class = 'Success';
                    $interval = "Realtime (${interval_s}s)";
                }elseif($interval<=10){
                    $class = 'Warning';
                    $interval = "Delayed (${interval_s}s)";
                }elseif($interval<40){
                    $class = 'Warning';
                    $interval = "Unresponsive (${interval_s}s)";
                }elseif($interval<59){
                    $class = 'Danger';
                    $interval = "About to expire (${interval_s}s)";
                }elseif($interval>=59){
                    $sql = "DELETE FROM terminal_threads WHERE thread=".$thread_id;
                    mysqli_query($con,$sql);
                    exit;
                }
            }

            print "<tr class='$class'><td>$thread_name</td><td>$interval</td><td>$thread_status</td></tr>";
        }
    }
}
?>