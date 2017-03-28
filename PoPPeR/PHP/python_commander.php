<?php //include "includes/admin_init.php";
//check apache version
//$apache_version = substr(apache_get_version(), 0, strpos(apache_get_version(), "PHP"));

//check if sql is active and check version
//$active = @mysql_ping() ? "<h3 style='text-align:center;'>" . mysql_get_server_info() . "</h3>" : "<h3 style='text-align:center;color:red;'>Failed</h3>";
//check if dependencies exists
include "conn.php";
//$sth = $conn_sys->prepare("SELECT sys_version FROM version");
//$active = $sth->execute();

?>
      


<div class="container">
<div style="margin-top:20px;">
    <div style="width:80%;margin-left:150px;">
        <h1>Python Commander Dashboard</h1>
    </div>

    <div style="width:80%;margin-left:150px;">
    <hr style="border-color:black;width:100%;">
    <img style="margin: auto;width: 200px;display: block;" id="preloader1" src="preloader.gif">
    <h1 style="margin: auto;width: 500px;display: block;" id="preloader2">Connecting to python handler...</h1>
    <div id="preload">
    
    <div id="load_tweets"> </div>
  
    <br><hr style="border-color:black;width:100%;">
   <div id="load_tweets2"> </div>

    <br><hr style="border-color:black;width:100%;">

      <form action='python_clear_processes.php'>
        <input type='submit' name='delete' value='clear processes' onclick='delete()' />
      </form>

      <form action='python_send_command.php'>
        Basic handler command: &nbsp
        <input style='width:20%;' type='text' name='thread' placeholder="thread">
        <input style='width:40%;' type='text' name='command' placeholder="command">

        <input type='submit' name='delete' value='Send Command' onclick='delete()' />
      </form>

      Master handler console:<br> 
      <textarea id="load_tweets3" style="width:100%;height:200px;" disabled="">Console listener inactive</textarea>
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
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3.0/jquery.min.js"></script>
<script type="text/javascript">
  var auto_refresh = setInterval(
  function ()
  {
  $('#load_tweets').load('python_commander_update.php').fadeIn("slow");
  $('#load_tweets2').load('python_commander_update2.php').fadeIn("slow");
  $('#load_tweets3').load('python_master_console_update.php').fadeIn("slow");
  }, 100); 
  
</script>