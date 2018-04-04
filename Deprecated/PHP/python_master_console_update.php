<?php
include_once "conn.php";


 $sql = ("SELECT console_time,console_line FROM python_master_console ORDER BY console_time ASC");
        foreach ($conn->query($sql) as $row) {
        if (strpos($row[1], '##USER_INPUT')===false){
	    	print $row[0] . ' >>> ' . $row[1];
	        print "\n";
	    } else {
			$user_print = str_replace('##USER_INPUT', '', $row[1]);
			print 'root>>>' . $user_print;
	        print "\n";
	    }
    }
?>