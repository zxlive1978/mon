<?php
	#Коннект к базе

	$dbc= mysqli_connect('localhost', 'goodman', 'NRywfHcXEmzenn7S') or
		die(mysqli_sqlstate($dbc));
	
	
	$code_page="SET NAMES 'utf8';";
	mysqli_query($dbc,$code_page) or
		die(mysqli_sqlstate($dbc));

	$name_base="pozitron";
	$table="p372978226";
	$x_id="date";
	$y_id="value";
	$y2_id="value";
	$x_value=array();
	$y_value=array();
	$xy_value=array();
	$xy1_value=array();
	
	$query="SELECT ".$x_id.",".$y_id." FROM ".$name_base.".".$table.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy_value,$row);
		}
		
	$query="SELECT ".$x_id.",".$y2_id." FROM ".$name_base.".".$table.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy1_value,$row);
		}
	// //Печать значений из массива
	// echo count($xy_value);
	// for ($i=0;$i<count($xy_value);$i++){
		// echo $xy_value[$i][0]." - ".$xy_value[$i][1]."<br />";
	// }
	
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value);$i++){
		$xy_value[$i][0]=1000*$xy_value[$i][0]+14400000;
		$xy1_value[$i][0]=1000*$xy1_value[$i][0]+14400000;
	}
	mysql_close()
	
?>