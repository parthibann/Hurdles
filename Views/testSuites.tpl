<!DOCTYPE html>
<html>
<head>
    <title>TestSuites</title>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="static/css/bootstrap-datetimepicker.min.css">
    <link rel="stylesheet" href="static/css/bootstrap.min.css">
    <!--<link rel="stylesheet" href="static/css/bootstrap-select.min.css">-->
    <script src="static/js/jquery.min.js"></script>
    <script src="static/js/bootstrap.min.js"></script>
    <!--<script src="static/js/bootstrap-select.min.js"></script>-->
    <script src="static/js/moment.js"></script>
    <script src="static/js/bootstrap-datetimepicker.min.js"></script>
    <link rel="stylesheet" href="static/css/jquery.dataTables.min.css">
    <script src="static/js/jquery.dataTables.min.js"></script>
    <script type="text/javascript">
    $(document).ready(function(){
    	$('#TestSuites').dataTable();
    	$('.selectAllTestCases').click(function(){
    		$('.chkTest').prop('checked',$(this).is(':checked'));
    	});
    	$('#dateTimePicker').datetimepicker({
                format: 'YYYY-MM-DD HH:mm:ss'
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
			<!--<div class="col-xs-3">
				<label>Mode :<select name="mode" id="mode" class="selectpicker" data-style="btn-warning">
					<option value="Serial">Serial</option>
					<option value="Parallel">Parallel</option>
				</select></label>
			</div>-->
			<div class="col-xs-3">
				<div class='input-group date' id="dateTimePicker">
                    <input id="schedule" name="schedule" type='text' class="form-control" placeholder="Schedule(YYYY-MM-DD HH:MM:SS)" required/>
                    <span id="calenderIcon" class="input-group-addon">
                    	<span class="glyphicon glyphicon-calendar"></span>
                    </span>
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
body{padding-top:10px;}
th{white-space: nowrap;}
#pageDetails{
	padding-left: 5px;
	padding-right: 5px;
	height:100%;
}
</style>