<!DOCTYPE html>
<html lang="en">
<head>
    <title>TestSuites</title>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="static/css/jquery.dataTables.min.css">
    <link rel="stylesheet" href="static/css/bootstrap-datetimepicker.min.css">
    <link rel="stylesheet" href="static/css/bootstrap.min.css">
    <script src="static/js/jquery.min.js"></script>
    <script src="static/js/bootstrap.min.js"></script>
    <script src="static/js/moment.js"></script>
    <script src="static/js/bootstrap-datetimepicker.min.js"></script>
    <script src="static/js/jquery.dataTables.min.js"></script>
    <script type="text/javascript">
    $(function(){
        $('#schedule').datetimepicker({
            format: 'yyyy-MM-dd HH:mm:ss'
        });
        $("#clearSchedule").click(function(){
            $("#schedule").val('');
        });
        $('#TestSuites').dataTable();
        $('.selectAllTestCases').click(function(){
            $('.chkTest').prop('checked',$(this).is(':checked'));
        });
    });
    </script>
</head>
<body>
	<div id="pageDetails" name="pageDetails">
	<form method="POST" action="/createJob">
		<div id="TestCaseTable" name="TestCaseTable">
		<table class="table" id="TestSuites" style="width:100%;height:100%;">
			<thead>
				<tr>
				<th><label><input type="checkbox" class="selectAllTestCases" />SelectAll</label></th>
				<th>TestSuite Name</th>
				<th>TestCase Name</th>
				</tr>
			</thead>
			{{!TestCases}}
		</table>
		</div>
		<div class="row">
			<div class="col-xs-3">
			<div class="form-group">
				<div class="input-group date" id="datetimepicker1">
                    <input type="text" id="schedule" name="schedule" class="form-control" placeholder="Schedule test" required/>
                    <span id="clearSchedule" class="input-group-addon">
                    	<span class="glyphicon glyphicon-remove"></span>
                    </span>
                </div>
            </div>
			</div>
			<div class="col-xs-1">
				<button type="submit" class="btn btn-primary">Create Job</button>
			</div>
		</div>
	</form>
	</div>
</body>
</html>
<style>
body{
    padding-top:10px;
}
th{
    white-space: nowrap;
}
#pageDetails{
	padding-left: 5px;
	padding-right: 5px;
    height:100%;
}
</style>