<?php //include "includes/admin_init.php";
//check apache version
//$apache_version = substr(apache_get_version(), 0, strpos(apache_get_version(), "PHP"));
session_start();

//check if sql is active and check version
//$active = @mysql_ping() ? "<h3 style='text-align:center;'>" . mysql_get_server_info() . "</h3>" : "<h3 style='text-align:center;color:red;'>Failed</h3>";
//check if dependencies exists
include "conn.php";
//$sth = $conn_sys->prepare("SELECT sys_version FROM version");
//$active = $sth->execute();

?>
<link href="/overcast/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
<link href="https://fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css">

<script src="/overcast/js/jquery.js"></script>
<head>
<title>Python Commander</title>
</head>
<body>
<div class="container">
<div style="margin-top:20px;">
    <div style="width:80%;margin-left:150px;">
        <a href='../'><button>Exit</button></a><h1 style='display:inline;' >&nbspPython Commander Dashboard</h1>
    </div>

    <div style="width:80%;margin-left:150px;">
    <hr style="border-color:black;width:100%;">
    <img style="margin: auto;width: 200px;display: block;" id="preloader1" src="preloader.gif">
    <h1 style="margin: auto;width: 500px;display: block;" id="preloader2">Connecting to python handler...</h1>
    <div id="preload">
    
    <div id="preloader"> </div>
  
    <!-- <br><hr style="border-color:black;width:100%;"> -->
   <div id="preloader2"> </div>

    <br><hr style="border-color:black;width:100%;">

      <form style="display: inline;" action='python_clear_processes.php'>
        <input type='submit' name='delete' value='clear processes' onclick='delete()' />
      </form>


      <?php
  include "ajax.php";
  $sql = "SELECT response_time FROM python_config";
  foreach ($conn->query($sql) as $row) {
    $perf_level = $row['response_time'];
  }
?>
<div style="display: inline;padding:20px;">
  <input style="width:300px;" type="range" id="rangeInput" name="rangeInput" value="<?php echo 1050-$perf_level; ?>" step="50" min="50" max="1000">
  <label id="rangeText" />
</div><br><br>

<script>
  $(function ($) {
      // on page load, set the text of the label based the value of the range
      $('#rangeText').text('Response time (' + <?php echo $perf_level; ?> + 'ms)');

      // setup an event handler to set the text when the range value is dragged (see event for input) or changed (see event for change)
      $('#rangeInput').on('input change', function () {
          $('#rangeText').text('Response time (' + (1050-$(this).val()) + 'ms)');
          update_response_time(1050-$(this).val());
      });

  });
</script>

      <form action='python_send_command.php'>
        Basic handler command: &nbsp
        <input style='width:20%;' type='text' name='thread' placeholder="thread">
        <input style='width:40%;' type='text' name='command' placeholder="command">

        <input type='submit' name='delete' value='Send Command' onclick='delete()' />
      </form>

      Master handler console:<br> 
      <textarea id="preloader3" style="width:100%;height:200px;" disabled="">Console listener inactive</textarea>
      <form action='python_send_master_command.php'>
        <input style='width:60%;' type='text' name='command' placeholder="command">
        <input type='submit' name='delete' value='Send Command' onclick='delete()' />
      </form>
</div>
</div>
</div>
</div>




















<script type="text/javascript">
    function preload(hide=true){
    var el1 = document.getElementById('preload');
    var preloader_gif1 = document.getElementById('preloader1');
    var preloader_text = document.getElementById('preloader2');

    if (hide==true){
    el1.style.visibility = 'hidden';
    preloader_text.style.display = 'visible';
    preloader_gif1.style.display = 'visible';
    }else{
    el1.style.visibility = 'visible';    
    preloader_text.style.display = 'none';
    preloader_gif1.style.display = 'none';
    }}

    preload(true);
    setTimeout(function(){ preload(false); }, 100);
</script>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.3.0/jquery.min.js"></script>
<script type="text/javascript">
  var auto_refresh = setInterval(
  function ()
  {
  $('#preloader').load('python_commander_update.php').fadeIn("slow");
  $('#preloader2').load('python_commander_update2.php').fadeIn("slow");
  $('#preloader3').load('python_master_console_update.php').fadeIn("slow");
  }, <?php echo $perf_level; ?>); 
  
</script>
</body>