<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<head>
    <title>PHP/Python Web Terminal</title>
</head>
<body>
<div style="margin-top:20px;width:80%" class="container">
    <h1 style="color:#2c3e50">&nbspPython Commander Dashboard</h1>
    <hr>
    <div class="row">
        <div class="col-md-8">
            <div class="form-group">
                <textarea disabled="" class="form-control" rows="10" id="comment"></textarea>
            </div>
            <form action='python_send_master_command.php'>
                <input class="form-control" type='text' name='command' placeholder="Input">
            </form>
        </div>
        
        <div class="col-md-4">
            <table class="table">
                <thead>
                  <tr>
                    <th>Thread</th>
                    <th>Update</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody>    
                  <tr class="success">
                    <td>1</td>
                    <td>00:55</td>
                    <td>Running function()</td>
                  </tr>
                </tbody>
              </table>
        </div>
    </div>
</div>