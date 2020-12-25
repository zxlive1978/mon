<?php 
session_start();
if ($_SESSION['start']<>1) {
	header("Location: /index.php");
	exit;
}
?>


<!DOCTYPE html>

<html>

<head>

<meta http-equiv="X-UA-Compatible" content="IE=edge" />

<meta charset="UTF-8">

<link rel="stylesheet" type="text/css" href="jschart5.css">

<!--[if lt IE 9]><script src="/js/excanvas.js"></script><![endif]-->

<style>
   body{ background-color: #000000;    }
</style>


<title></title>

</head>

<body bgcolor="#000000">

<video class='video' src="http://hydrofalll.ddns.net:8090/test2.webm" controls width="100%" autoplay="autoplay">
</video>
<!--
<div id="leg1"  style="font-size:2em">АГКМ630-1 192.168.146.199  </div>
<img src="poz/411_1.jpg" alt="411_1" width="100%" height="800">
<img src="poz/411_2.jpg"  alt="411_2" width="100%" height="800">
<img src="poz/411_3.jpg"  alt="411_3" width="100%" height="800">
<img src="poz/411_4.jpg"  alt="411_4" width="100%" height="800">

-->

</body>

</html>
