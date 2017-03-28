<?php
include_once "conn.php";
echo "<table style='width:100%;text-align: center;'>
      <h3 style='display:inline;'>Python Status</h3>

      <tr>
        <th style='text-align: center;'>Module</th>
        <th style='text-align: center;'>Status</th>
        <th style='text-align: center;'>Response</th>
      </tr>";

 $sql = ("SELECT * FROM python_data WHERE process_name NOT LIKE '%python_remote_handler%'");
        foreach ($conn->query($sql) as $row) {
        $var = strtotime($row['process_update']);
        //$var = time() - strtotime($var);
        if((time()-(60)) < $var){
          $response = "<div style='color:darkorange;'>Heavily Delayed (<60s)</div>";
          if((time()-(20)) < $var){
            $response = "<div style='color:orange;'>Delayed (<20s)</div>";
            if((time()-(10)) < $var){
              $response = "<div style='color:green;'>Healthy (<10s)</div>";
            }
          }
        } else {
          $response = "<div style='color:red;'>OFFLINE (>60s)</div>";
        }
        echo '<tr><td>' . $row['process_name'] . '</td><td>' . $row['process_status'] . '</td><td>' . $response . '</td></tr>';
        }
  echo "</table>";
    ?>