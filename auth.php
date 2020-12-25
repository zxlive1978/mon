<?php

if(isset($_GET['submit1']))
 {
	
    if(empty($_GET['email']))
        $err = 'Не введен Логин';
     
    if(empty($_GET['pass']))
        $err = $err.'Не введен Пароль';
	include 'check_users.php';
	if(!$_SESSION['start']){
		$err='Неверный логин или Пароль!!!';
	} else {
		$timeshift =$_GET['timeshift'];
		//echo $timeshift;
		
		//$err='GOOD';
	}
         
    //Проверяем наличие ошибок и выводим пользователю
    if(count($err) > 0)
        echo $err;
	
	
	}
?>