<?php
session_start();
$lines = file('config.cfg');
$_SESSION['host'] = rtrim(substr($lines[0], strpos($lines[0], "=") + 1));
$_SESSION['user'] = rtrim(substr($lines[1], strpos($lines[1], "=") + 1));
$_SESSION['passwd'] = rtrim(substr($lines[2], strpos($lines[2], "=") + 1));
$_SESSION['client_refresh'] = substr($lines[3], strpos($lines[3], "=") + 1);

?>

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<head>
    <title>PHP/Python Web Terminal</title>
</head>
<body>
<div style="margin-top:20px;width:80%" class="container">
    <h1 style="color:#2c3e50">&nbspPHP/Python Web Terminal</h1>
    <hr>
    <div class="row">
        <div class="col-md-8">
            <div class="form-group">
                <textarea id="terminal" disabled="" class="form-control" rows="20" id="comment"></textarea>
            </div>
            <form action='core.php' method="GET">
                <input hidden name="action" value="send_command">
                <input class="form-control" type='text' name='command' placeholder="Input" autofocus>
                <input hidden type="submit">
            </form>
        </div>
        
        <div class="col-md-4">
            <table class="table">
                <thead>
                  <tr>
                    <th>Thread</th>
                    <th>Ping</th>
                    <th>Message</th>
                  </tr>
                </thead>
                <tbody id="status">
                </tbody>
              </table>
        </div>
    </div>
</div>

<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.3.0/jquery.min.js"></script>
<script type="text/javascript">
    $('#terminal').load('core.php?action=update_feed');
    $('#status').load('core.php?action=refresh_threads');
    var textarea = document.getElementById('terminal');
    textarea.scrollTop = textarea.scrollHeight;
    
    var auto_refresh = setInterval(
    function (){
        $('#terminal').load('core.php?action=update_feed');
        $('#status').load('core.php?action=refresh_threads');
        var textarea = document.getElementById('terminal');
        textarea.scrollTop = textarea.scrollHeight;
    }, <?php echo $_SESSION['client_refresh'] ?>); 
  
</script>