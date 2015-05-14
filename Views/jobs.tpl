<!DOCTYPE html>
<html>
<head>
    <title>Jobs</title>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="static/css/bootstrap.min.css">
    <script src="static/js/jquery.min.js"></script>
    <script src="static/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="static/css/jquery.dataTables.min.css">
    <script src="static/js/jquery.dataTables.min.js"></script>
    <script type="text/javascript">
    $(document).ready(function(){
    	$('#jobs').dataTable();
    });
    </script>
</head>
<body>
	<div id="jobsTable" name="jobsTable">
		<table class="table" id="jobs" style="width:100%;height:100%;">
		<thead>
			<tr>
				<th>Job Id</th>
				<th>Tester Name</th>
				<th>Job Details</th>
				<th>TestRunner</th>
				<th>Scheduled on</th>
				<th>Status</th>
			</tr>
		</thead>
		% for job in jobs:
			<tr><td>{{job[0]}}</td><td>{{job[1]}}</td><td>{{job[3]}}</td><td>{{job[4]}}</td><td>{{job[5]}}</td><td>{{job[6]}}</td></tr>
		% end
		</table>
	</div>
</body>
</html>
<style>
body{
	padding-top:10px;
	padding-left: 5px;
	padding-right: 5px;
	height:100%;
}
th{white-space: nowrap;}
</style>
