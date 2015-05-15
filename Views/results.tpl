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
				<th>Test Plan</th>
				<th>Build</th>
				<th>Testcase</th>
				<th>Comments</th>
				<th>Status</th>
			</tr>
		</thead>
		% for data in results:
			<tr><td>{{data[1]}}</td><td>{{data[2]}}</td><td>{{data[3]}}</td><td>{{data[4]}}</td><td>{{data[5]}}</td><td>{{data[6]}}</td><td><img src="/static/images/{{data[7]}}.png"></td></tr>
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
