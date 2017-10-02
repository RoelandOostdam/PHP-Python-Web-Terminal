<script>
 function update_response_time($perf_level) {
      $.ajax({
        url: 'update_response_time.php',
        type:'POST',
        data:
        {
            level: $perf_level
        }          
    });
 }
</script>