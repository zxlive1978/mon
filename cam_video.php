<?php 
session_start();
if ($_SESSION['start']<>1) {
	header("Location: /index.php");
	exit;
}
$agrv=$_GET['agr'];
?>


<!DOCTYPE html>

<html>

<head>

<meta http-equiv="X-UA-Compatible" content="IE=edge" />

<meta charset="UTF-8">

/* <link href="./jschart5.css" rel="stylesheet" type="text/css"> */

<!--[if lt IE 9]><script src="/js/excanvas.js"></script><![endif]-->
<script type="text/javascript" src="js/jquery-2.0.2.min.js"></script>
<script type="text/javascript" src="js/jquery-migrate-1.2.1.min.js"></script>



<style>
   /* body{ background-color: #000000;    } */
</style>


<title></title>

</head>



<div id="timer" class="hidden" align="center" >
  <p>
<label for="localdate" style="width:100Px;height:60Px;font-size:35px" maxlength="20">НАЧАЛО:</label>
<?php echo "<input type='date' id='localdate' name='date' style='width:300Px;height:50Px;font-size:35px' maxlength='20' value='".date("Y-m-d")."'>"; ?>;
<input type="time" id="localtime" name="time" value="01:02" min="00:00" max="23:58" style="width:140Px;height:50Px;font-size:35px" maxlength="20" />
<button for="localdate" type="submit" onclick="goto()" style="width:180px;height:60px;font-size:35px" maxlength="20">ПЕРЕЙТИ</button>
<button type="submit" onclick="gotonow()" style="width:170Px;height:60Px;font-size:35px" maxlength="20">СЕЙЧАС</button>
  </p>
</div>
<div id="divVideo" align="center">
  <video id="video" controls autoplay="autoplay">
    <source src=""  />
  </video>
</div>
<script type="text/javascript">
<?php echo 'var agrr = '.json_encode($agrv).';' ?>;
</script>
<script type="text/javascript" src="js/cams.js"></script>


</body>

</html>
