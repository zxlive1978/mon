<?php 
	$host1 = $_GET['host'];
	$type1 = $_GET['type'];
	if( ini_get('safe_mode') ){
    // Do it the safe mode way
	}else{
    // Do it the regular way
	//$cmd = '/var/www/html/mon/poz/./camcam.py '.$host1.' '.$type1;
	//$cmd = 'ls -l';
	//$output = shell_exec($cmd);
	system( "/usr/bin/python /var/www/html/mon/poz/camcam.py $host1 $type1");
	//system( "ls -l");
	
	}

?>


<!DOCTYPE html>

<html>

<head>

<meta http-equiv="X-UA-Compatible" content="IE=edge" />

<meta charset="UTF-8">

<link rel="stylesheet" type="text/css"  href="../jschart5.css">

<!--[if lt IE 9]><script src="/js/excanvas.js"></script><![endif]-->




<title></title>

</head>

<body>

<div id="leg1"  style="font-size:2em"></div>
<a href  onclick="javascript:location.reload();"> <img src="../poz/montag.jpg"  width="100%" height="800"></a>
<br><br><br><br>
<div id="timer" class="hidden" align="center" >
<button type="submit"  style="width:200Px;height:100Px;font-size:34px" maxlength="20" onclick="window.location.replace('../index.php?email=VIDEO&pass=Monitoring&timeshift=1&submit1=Войти');">НАЗАД</button>
</div>
</body>

</html>
