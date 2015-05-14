<html>
<head>
    <title>Hurdles</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="static/css/bootstrap.min.css">
    <link rel="stylesheet" href="static/css/font-awesome.min.css">
    <script src="static/js/jquery.min.js"></script>
    <script src="static/js/bootstrap.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function () {
        $("#apikey").hide();
        $("#Testlink").click(function () {
        $("#apikey").show();
        });
        $("#Hurdles").click(function () {
        $("#apikey").hide();
        });
    });
    </script>
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-md-offset-5 col-md-3">
                <form class="form-login" method="POST" action="/login">
                    <h4><img src="static/images/hurdles.png" height="25" width="25">Hurdles</h4>
                    <input type="text" id="userName" name="userName" class="form-control input-sm chat-input" placeholder="username *" required/>
                    </br>
                    <input type="text" id="testPlan" name="testPlan" class="form-control input-sm chat-input" placeholder="testplan *" required/>
                    </br>
                    <input type="text" id="buildName" name="buildName" class="form-control input-sm chat-input" placeholder="build name *" required/>
                    </br>
                    <label><input type="radio" name="TestRunner" id="Hurdles" value="Hurdles" checked>Hurdles</label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <label><input type="radio" name="TestRunner" id="Testlink" value="Testlink">Testlink</label>
                    </br>
                    <input type="text" id="apikey" name="apikey" class="form-control input-sm chat-input" placeholder="api key *" />
                    </br>
                    <div class="wrapper">
                        <input type="submit" class="btn btn-primary" value="Sign in">
                    </div>
                </form>
            </div>
        </div>
    </div>
</body>
</html>
<style>
body{
    background-color:#3b5998;
    -webkit-font-smoothing: antialiased;
    font: normal 14px Roboto,arial,sans-serif;
}
.container{
    padding: 50px;
    position: fixed;
}
h4{
    border:0 solid #fff;
    border-bottom-width:1px;
    padding-bottom:10px;
    text-align:left;
}
.form-control{
    border-radius: 10px;
}
.wrapper{
    text-align:center;
}
.form-login {
    background-color: #EDEDED;
    padding-top: 10px;
    padding-bottom: 20px;
    padding-left: 20px;
    padding-right: 20px;
    border-radius: 15px;
    border-color:#d2d2d2;
    border-width: 5px;
    box-shadow:0 1px 0 #cfcfcf;
}
</style>
