<!DOCTYPE html>
<html lang="en">
<head>
    <title>Hurdles - Dashboard</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="static/css/bootstrap.min.css">
    <link rel="stylesheet" href="static/css/font-awesome.min.css">
    <script src="static/js/jquery.min.js"></script>
    <script src="static/js/bootstrap.min.js"></script>
</head>
<body>
    <header class="navbar navbar-inverse navbar-fixed-top" role="banner">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">Hurdles</a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav navbar-right">
            <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false" style="font-size:18px;"><i class="fa fa-user"></i>&nbsp;{{username}} <span class="caret"></span></a>
                <ul class="dropdown-menu" role="menu">
                    <li><a href="#"><i class="fa fa-tachometer"></i>&nbsp;Dashboard</a></li>
                    <li><a href="/testSuites" target="frame"><i class="fa fa-pencil-square-o"></i>&nbsp;TestSuites</a></li>
                    <li><a href="/jobs" target="frame"><i class="fa fa-tasks"></i>&nbsp;Jobs</a></li>
                    <li><a href="/results" target="frame"><i class="fa fa-file-text"></i>&nbsp;Result</a></li>
                    <li class="divider"></li>
                    <form method="POST" action="/logout">
                        <button type="submit" class="btn btn-link">
                            <i class="fa fa-sign-out"></i>&nbsp;Logout
                        </button>
                    </form>
                </ul>
            </li>
        </ul>
        </div>
    </header>
    <div id="pageContainer" name="pageContainer">
        <iframe id="frame" name="frame" frameborder="0"></iframe>
    </div>
</body>
</html>
<style type="text/css">
html,body{
    height:100%;
}
.navbar,.navbar-inverse,.navbar-fixed-top{
    background-color:#22537E;
    text-decoration: none;
}
.navbar-inverse .btn-link {
    padding-left: 20px;
    color: #333;
}
.navbar-inverse .btn-link:hover{
    color:#333;
    text-decoration: none;
}
#pageContainer{
    width:100%;
    height:100%;
    padding-top:50px;
}
#frame{
    width:100%;
    height:99.5%;
}
</style>