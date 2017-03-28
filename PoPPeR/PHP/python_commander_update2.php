<?php
include_once "conn.php";
echo "<table style='width:100%;text-align: center;'>
      <h3 style='display:inline;'>Python Remote Handlers</h3>

      <tr>
        <th style='text-align: center;'>Thread</th>
        <th style='text-align: center;'>Status</th>
        <th style='text-align: center;'>Response (if waiting)</th>
      </tr>";

 $sql = ("SELECT * FROM python_data WHERE process_name LIKE '%python_remote_handler%'");
        foreach ($conn->query($sql) as $row) {
        $var = strtotime($row['process_update']);
        //$var = time() - strtotime($var);
        if((time()-(60)) < $var){
          $response = "<div style='color:darkorange;'>(<60s)</div>";
          if((time()-(20)) < $var){
            $response = "<div style='color:orange;'>(<20s)</div>";
            if((time()-(10)) < $var){
              $response = "<div style='color:green;'>(<10s)</div>";
            }
          }
        } else {
          $response = "<div style='color:red;'>(>60s)</div>";
        }
        echo '<tr><td>' . $row['process_name'] . '</td><td>' . $row['process_status'] . '</td><td>' . $response . '</td></tr>';
        }
  echo "</table>";
    ?>