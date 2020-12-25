
<head><title>__-=M=-__</title>
<!--SSM NATIONAL COMPANIA AND Diman-Soft'94
PRESENTS: THE BEST MONITORING FOREVER-->
<link href="./jschart5.css" rel="stylesheet" type="text/css">
 <!-- <style>
   body {
    height: 200px; /* Высота блока */
    border: 2px solid #000; /* Параметры рамки */
    background: url(back.jpg) 100% 100% no-repeat; /* Добавляем фон */
    background-size: 100% 100% ; /* Масштабируем фон */
   }
  </style> -->
</head>
<?php
	
	ini_set("memory_limit", "512M");
	//Отладка ошибок
	ini_set('display_errors',1);
	error_reporting(E_ALL ^E_NOTICE);
 //Запускаем механизм сессии
	if ( $_SESSION['start'] == false) {
    session_start();
     
    $_SESSION['start'] = false;}
     
    // echo $_SESSION['str'].'<br>';
    // echo '<a href="test2.php">test2.php</a>';
	// <?php
    // /**
    // * Фаил test2.php 
    // * PHP сессия
    // */
     
    // //Выводим данные
    // echo $str;
	
	//include './con_monitor.php';

	
	$name_base="goodman";
	// $table=$_POST['table'];
	// $collid=$_POST['collid'];
	$table="TIME_030";
	$collid="id0";
	// $user=$_POST['user'];
	// $pass=$_POST['pass'];
	

	
	// $query="SELECT ".$collid." FROM ".$name_base.".".$table;
	// $result=mysqli_query($dbc,$query) or
		// die(mysqli_sqlstate($dbc));
	// echo mysqli_sqlstate($dbc);
	// echo $collid.$name_base.$table.$host;
	// while($row =mysqli_fetch_array($result)){
		// echo $row[$collid]."<br />";}
	
	include './auth.php';
	//IP Посетителя!
	//echo $visitor_ip = $_SERVER['REMOTE_ADDR'];
	
	
	if($_SESSION['start']){
		include './graph_js.php';
		include './graph_js.html';
	} else{
		include './auth_form.html';
	}


		
	
	

?>
