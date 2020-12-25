<?php
	$dbc= mysqli_connect('127.0.0.1', 'goodman', 'NRywfHcXEmzenn7S') or
		die(mysqli_sqlstate($dbc));
	
	
	$code_page="SET NAMES 'utf8';";
	mysqli_query($dbc,$code_page) or
		die(mysqli_sqlstate($dbc));

	$name_base="pozitron";
	$table="p372978226";
	$x_id="date";
	$y_id="value";
	$z1_id="rx";
	$z2_id="tx";
	$z3_id="ml";
	$xy_value916=array();
	$cur_time=0;
	$table="s110";
	$x_id="Vrema";
	$y_id="Wkp";
	$z1_id="Wdol";
	$z2_id="Mpot";
	$z3_id="Npot";
	$z4_id="Pbx";
	$z5_id="Qbx";
	$z6_id="Talblok";
	$z7_id="Zaboj";
	$z8_id="Instr";
	$z9_id="C1C5";
	$z10_id="C1";
	$z11_id="Xn1";
	$z12_id="Xn2";
	$z13_id="Potok";
	$z14_id="Tbix";
	$z15_id="V1";
	$z16_id="V2";
	$z17_id="V3";
	$z18_id="V4";
	$z19_id="Vdol";
	$z20_id="Vobj";
	$xy_value110d=array();

	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	$nach = $_GET['name'];
	echo $nach;
	#echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy_value916,$row);
		}
		
	
	
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	echo count($xy_value916);
	for ($i=0;$i<count($xy_value916);$i++){
		$xy_value916[$i][0]=1000*$xy_value916[$i][0]+14400000;
		
	}
	
	
	
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec916=$row[0];
		}
		
    mysqli_close($dbc);

		
?>