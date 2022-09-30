<?php
	#Коннект к базе
	

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
	$z4_id="mrx";
	$z5_id="mtx";
	$z6_id="sigpoz";
	$z7_id="dvr";
	$z8_id="cam1";
	$z9_id="cam2";
	$z10_id="cam3";
	$z11_id="cam4";
	$z12_id="ub1";
	$z13_id="ub2";
	$z14_id="sbor";
	$z15_id="ub1sig";
	$z16_id="ub1amq";
	$z17_id="ub1amc";
	$z18_id="ub2sig";
	$z19_id="ub2amq";
	$z20_id="ub2amc";
	$z21_id="mlrx";
	$z22_id="mltx";
	$z31_id="luchrx";
	$z32_id="luchtx";
	$xy_value916=array();
	$cur_time=time()-60*60*24*(float)$timeshift;

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	//echo $query;
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
	//echo count($xy_value);
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
	
	#4450	
	$table="p31173139214";
	$x_id="date";
	$y_id="value";
	$z1_id="rx";
	$z2_id="tx";
	$z3_id="ml";
	$z4_id="mrx";
	$z5_id="mtx";
	$z6_id="sigpoz";
	$z7_id="dvr";
	$z8_id="cam1";
	$z9_id="cam2";
	$z10_id="cam3";
	$z11_id="cam4";
	$z12_id="ub1";
	$z13_id="ub2";
	$z14_id="sbor";
	$z15_id="ub1sig";
	$z16_id="ub1amq";
	$z17_id="ub1amc";
	$z18_id="ub2sig";
	$z19_id="ub2amq";
	$z20_id="ub2amc";
	$z21_id="mlrx";
	$z22_id="mltx";
	$z31_id="luchrx";
	$z32_id="luchtx";
	$xy_value4450=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy_value4450,$row);
		}
		
	
	
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value4450);$i++){
		$xy_value4450[$i][0]=1000*$xy_value4450[$i][0]+14400000;
		
	}
	
	
	
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec4450=$row[0];
		}
	
	#631	
	$table="p31173139218";
	$x_id="date";
	$y_id="value";
	$z1_id="rx";
	$z2_id="tx";
	$z3_id="ml";
	$z4_id="mrx";
	$z5_id="mtx";
	$z6_id="sigpoz";
	$z7_id="dvr";
	$z8_id="cam1";
	$z9_id="cam2";
	$z10_id="cam3";
	$z11_id="cam4";
	$z12_id="ub1";
	$z13_id="ub2";
	$z14_id="sbor";
	$z15_id="ub1sig";
	$z16_id="ub1amq";
	$z17_id="ub1amc";
	$z18_id="ub2sig";
	$z19_id="ub2amq";
	$z20_id="ub2amc";
	$z21_id="mlrx";
	$z22_id="mltx";
	$z31_id="luchrx";
	$z32_id="luchtx";
	$xy_value631=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy_value631,$row);
		}
		
	
	
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value631);$i++){
		$xy_value631[$i][0]=1000*$xy_value631[$i][0]+14400000;
		
	}
	
	
	
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec631=$row[0];
		}
		
	#110	
	$table="p19216814697";
	$x_id="date";
	$y_id="value";
	$z1_id="rx";
	$z2_id="tx";
	$z3_id="ml";
	$z4_id="mrx";
	$z5_id="mtx";
	$z6_id="sigpoz";
	$z7_id="dvr";
	$z8_id="cam1";
	$z9_id="cam2";
	$z10_id="cam3";
	$z11_id="cam4";
	$z12_id="ub1";
	$z13_id="ub2";
	$z14_id="sbor";
	$z15_id="ub1sig";
	$z16_id="ub1amq";
	$z17_id="ub1amc";
	$z18_id="ub2sig";
	$z19_id="ub2amq";
	$z20_id="ub2amc";
	$z21_id="mlrx";
	$z22_id="mltx";
	$z31_id="luchrx";
	$z32_id="luchtx";
	$xy_value110=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy_value110,$row);
		}
		
	
	
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value110);$i++){
		$xy_value110[$i][0]=1000*$xy_value110[$i][0]+14400000;
		
	}
	
	
	
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec110=$row[0];
		}
		
		
	#2241	
	$table="p31173187210";
	$x_id="date";
	$y_id="value";
	$z1_id="rx";
	$z2_id="tx";
	$z3_id="ml";
	$z4_id="mrx";
	$z5_id="mtx";
	$z6_id="sigpoz";
	$z7_id="dvr";
	$z8_id="cam1";
	$z9_id="cam2";
	$z10_id="cam3";
	$z11_id="cam4";
	$z12_id="ub1";
	$z13_id="ub2";
	$z14_id="sbor";
	$z15_id="ub1sig";
	$z16_id="ub1amq";
	$z17_id="ub1amc";
	$z18_id="ub2sig";
	$z19_id="ub2amq";
	$z20_id="ub2amc";
	$z21_id="mlrx";
	$z22_id="mltx";
	$z31_id="luchrx";
	$z32_id="luchtx";
	$xy_value2241=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy_value2241,$row);
		}
		
	
	
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value2241);$i++){
		$xy_value2241[$i][0]=1000*$xy_value2241[$i][0]+14400000;
		
	}
	
	
	
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec2241=$row[0];
		}

	#908	
	$table="p31173139222";
	$x_id="date";
	$y_id="value";
	$z1_id="rx";
	$z2_id="tx";
	$z3_id="ml";
	$z4_id="mrx";
	$z5_id="mtx";
	$z6_id="sigpoz";
	$z7_id="dvr";
	$z8_id="cam1";
	$z9_id="cam2";
	$z10_id="cam3";
	$z11_id="cam4";
	$z12_id="ub1";
	$z13_id="ub2";
	$z14_id="sbor";
	$z15_id="ub1sig";
	$z16_id="ub1amq";
	$z17_id="ub1amc";
	$z18_id="ub2sig";
	$z19_id="ub2amq";
	$z20_id="ub2amc";
	$z21_id="mlrx";
	$z22_id="mltx";
	$z31_id="luchrx";
	$z32_id="luchtx";
	$xy_value908=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy_value908,$row);
		}
		
	
	
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value908);$i++){
		$xy_value908[$i][0]=1000*$xy_value908[$i][0]+14400000;
		
	}
	
	
	
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec908=$row[0];
		}
		
	#411	
	$table="p3729814";
	$x_id="date";
	$y_id="value";
	$z1_id="rx";
	$z2_id="tx";
	$z3_id="ml";
	$z4_id="mrx";
	$z5_id="mtx";
	$z6_id="sigpoz";
	$z7_id="dvr";
	$z8_id="cam1";
	$z9_id="cam2";
	$z10_id="cam3";
	$z11_id="cam4";
	$z12_id="ub1";
	$z13_id="ub2";
	$z14_id="sbor";
	$z15_id="ub1sig";
	$z16_id="ub1amq";
	$z17_id="ub1amc";
	$z18_id="ub2sig";
	$z19_id="ub2amq";
	$z20_id="ub2amc";
	$z21_id="mlrx";
	$z22_id="mltx";
	$z31_id="luchrx";
	$z32_id="luchtx";
	$xy_value411=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy_value411,$row);
		}
		
	
	
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value411);$i++){
		$xy_value411[$i][0]=1000*$xy_value411[$i][0]+14400000;
		
	}
	
	
	
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec411=$row[0];
		}
	
	#connect
	$table="pconnect";
	$x_id="date";
	$y_id="p8888";
	$z1_id="p6222055149";
	$z2_id="p8084114180";
	$z3_id="p192168773";
	$z4_id="p31173187210";
	$xy_valueconn=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy_valueconn,$row);
		}
		
	
	
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_valueconn);$i++){
		$xy_valueconn[$i][0]=1000*$xy_valueconn[$i][0]+14400000;
		
	}
	
	
	
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_recconn=$row[0];
		}
	
	#89	
	$table="p192168146161";
	$x_id="date";
	$y_id="value";
	$z1_id="rx";
	$z2_id="tx";
	$z3_id="ml";
	$z4_id="mrx";
	$z5_id="mtx";
	$z6_id="sigpoz";
	$z7_id="dvr";
	$z8_id="cam1";
	$z9_id="cam2";
	$z10_id="cam3";
	$z11_id="cam4";
	$z12_id="ub1";
	$z13_id="ub2";
	$z14_id="sbor";
	$z15_id="ub1sig";
	$z16_id="ub1amq";
	$z17_id="ub1amc";
	$z18_id="ub2sig";
	$z19_id="ub2amq";
	$z20_id="ub2amc";
	$z21_id="mlrx";
	$z22_id="mltx";
	$z31_id="luchrx";
	$z32_id="luchtx";
	$xy_value89=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy_value89,$row);
		}
		
	
	
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value89);$i++){
		$xy_value89[$i][0]=1000*$xy_value89[$i][0]+14400000;
		
	}
	
	
	
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec89=$row[0];
		}		
	
	
	
	#89	
	$table="p192168146161";
	$x_id="date";
	$y_id="value";
	$z1_id="rx";
	$z2_id="tx";
	$z3_id="ml";
	$z4_id="mrx";
	$z5_id="mtx";
	$z6_id="sigpoz";
	$z7_id="dvr";
	$z8_id="cam1";
	$z9_id="cam2";
	$z10_id="cam3";
	$z11_id="cam4";
	$z12_id="ub1";
	$z13_id="ub2";
	$z14_id="sbor";
	$z15_id="ub1sig";
	$z16_id="ub1amq";
	$z17_id="ub1amc";
	$z18_id="ub2sig";
	$z19_id="ub2amq";
	$z20_id="ub2amc";
	$z21_id="mlrx";
	$z22_id="mltx";
	$z31_id="luchrx";
	$z32_id="luchtx";
	$xy_value89=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy_value89,$row);
		}
		
	
	
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value89);$i++){
		$xy_value89[$i][0]=1000*$xy_value89[$i][0]+14400000;
		
	}
	
	
	
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec89=$row[0];
		}
	
	#83	
	$table="p192168146129";
	$x_id="date";
	$y_id="value";
	$z1_id="rx";
	$z2_id="tx";
	$z3_id="ml";
	$z4_id="mrx";
	$z5_id="mtx";
	$z6_id="sigpoz";
	$z7_id="dvr";
	$z8_id="cam1";
	$z9_id="cam2";
	$z10_id="cam3";
	$z11_id="cam4";
	$z12_id="ub1";
	$z13_id="ub2";
	$z14_id="sbor";
	$z15_id="ub1sig";
	$z16_id="ub1amq";
	$z17_id="ub1amc";
	$z18_id="ub2sig";
	$z19_id="ub2amq";
	$z20_id="ub2amc";
	$z21_id="mlrx";
	$z22_id="mltx";
	$z31_id="luchrx";
	$z32_id="luchtx";
	$xy_value83=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy_value83,$row);
		}
		
	
	
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value83);$i++){
		$xy_value83[$i][0]=1000*$xy_value83[$i][0]+14400000;
		
	}
	
	
	
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec83=$row[0];
		}
		
	#401	
	$table="p1921681461";
	$x_id="date";
	$y_id="value";
	$z1_id="rx";
	$z2_id="tx";
	$z3_id="ml";
	$z4_id="mrx";
	$z5_id="mtx";
	$z6_id="sigpoz";
	$z7_id="dvr";
	$z8_id="cam1";
	$z9_id="cam2";
	$z10_id="cam3";
	$z11_id="cam4";
	$z12_id="ub1";
	$z13_id="ub2";
	$z14_id="sbor";
	$z15_id="ub1sig";
	$z16_id="ub1amq";
	$z17_id="ub1amc";
	$z18_id="ub2sig";
	$z19_id="ub2amq";
	$z20_id="ub2amc";
	$z21_id="mlrx";
	$z22_id="mltx";
	$z31_id="luchrx";
	$z32_id="luchtx";
	$xy_value401=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy_value401,$row);
		}
		
	
	
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value401);$i++){
		$xy_value401[$i][0]=1000*$xy_value401[$i][0]+14400000;
		
	}
	
	
	
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec401=$row[0];
		}


#610	
	$table="p1921681471";
	$x_id="date";
	$y_id="value";
	$z1_id="rx";
	$z2_id="tx";
	$z3_id="ml";
	$z4_id="mrx";
	$z5_id="mtx";
	$z6_id="sigpoz";
	$z7_id="dvr";
	$z8_id="cam1";
	$z9_id="cam2";
	$z10_id="cam3";
	$z11_id="cam4";
	$z12_id="ub1";
	$z13_id="ub2";
	$z14_id="sbor";
	$z15_id="ub1sig";
	$z16_id="ub1amq";
	$z17_id="ub1amc";
	$z18_id="ub2sig";
	$z19_id="ub2amq";
	$z20_id="ub2amc";
	$z21_id="mlrx";
	$z22_id="mltx";
	$z31_id="luchrx";
	$z32_id="luchtx";
	$xy_value610=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy_value610,$row);
		}
		
	
	
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value610);$i++){
		$xy_value610[$i][0]=1000*$xy_value610[$i][0]+14400000;
		
	}
	
	
	
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec610=$row[0];
		}
		
#627	
	$table="p19216814733";
	$x_id="date";
	$y_id="value";
	$z1_id="rx";
	$z2_id="tx";
	$z3_id="ml";
	$z4_id="mrx";
	$z5_id="mtx";
	$z6_id="sigpoz";
	$z7_id="dvr";
	$z8_id="cam1";
	$z9_id="cam2";
	$z10_id="cam3";
	$z11_id="cam4";
	$z12_id="ub1";
	$z13_id="ub2";
	$z14_id="sbor";
	$z15_id="ub1sig";
	$z16_id="ub1amq";
	$z17_id="ub1amc";
	$z18_id="ub2sig";
	$z19_id="ub2amq";
	$z20_id="ub2amc";
	$z21_id="mlrx";
	$z22_id="mltx";
	$z31_id="luchrx";
	$z32_id="luchtx";
	$xy_value627=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy_value627,$row);
		}
		
	
	
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value627);$i++){
		$xy_value627[$i][0]=1000*$xy_value627[$i][0]+14400000;
		
	}
	
	
	
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec627=$row[0];
		}



#16	
$table="p19216801";
$x_id="date";
$y_id="value";
$z1_id="rx";
$z2_id="tx";
$z3_id="ml";
$z4_id="mrx";
$z5_id="mtx";
$z6_id="sigpoz";
$z7_id="dvr";
$z8_id="cam1";
$z9_id="cam2";
$z10_id="cam3";
$z11_id="cam4";
$z12_id="ub1";
$z13_id="ub2";
$z14_id="sbor";
$z15_id="ub1sig";
$z16_id="ub1amq";
$z17_id="ub1amc";
$z18_id="ub2sig";
$z19_id="ub2amq";
$z20_id="ub2amc";
$z21_id="mlrx";
$z22_id="mltx";
$z31_id="luchrx";
$z32_id="luchtx";
$xy_value116=array();


$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
//echo $query;
$result=mysqli_query($dbc,$query) or
	die(mysqli_sqlstate($dbc));
//echo mysqli_sqlstate($dbc);
// echo $_POST['email'];
// echo $_POST['pass'];

//Добавление значений в массив
while($row = mysqli_fetch_array ($result)){
	//echo $row[$x_id]." - ".$row[$y_id]."<br />";
	array_push($xy_value116,$row);
	}
	


//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
//echo count($xy_value);
for ($i=0;$i<count($xy_value116);$i++){
	$xy_value116[$i][0]=1000*$xy_value116[$i][0]+14400000;
	
}



$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";

$result=mysqli_query($dbc,$query) or
	die(mysqli_sqlstate($dbc));
while($row = mysqli_fetch_array ($result)){
	//echo $row[$x_id]." - ".$row[$y_id]."<br />";
	$numbs_rec116=$row[0];
	}




#438	
$table="p1921681481";
$x_id="date";
$y_id="value";
$z1_id="rx";
$z2_id="tx";
$z3_id="ml";
$z4_id="mrx";
$z5_id="mtx";
$z6_id="sigpoz";
$z7_id="dvr";
$z8_id="cam1";
$z9_id="cam2";
$z10_id="cam3";
$z11_id="cam4";
$z12_id="ub1";
$z13_id="ub2";
$z14_id="sbor";
$z15_id="ub1sig";
$z16_id="ub1amq";
$z17_id="ub1amc";
$z18_id="ub2sig";
$z19_id="ub2amq";
$z20_id="ub2amc";
$z21_id="mlrx";
$z22_id="mltx";
$z31_id="luchrx";
$z32_id="luchtx";
$xy_value117=array();


$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
//echo $query;
$result=mysqli_query($dbc,$query) or
	die(mysqli_sqlstate($dbc));
//echo mysqli_sqlstate($dbc);
// echo $_POST['email'];
// echo $_POST['pass'];

//Добавление значений в массив
while($row = mysqli_fetch_array ($result)){
	//echo $row[$x_id]." - ".$row[$y_id]."<br />";
	array_push($xy_value117,$row);
	}
	


//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
//echo count($xy_value);
for ($i=0;$i<count($xy_value117);$i++){
	$xy_value117[$i][0]=1000*$xy_value117[$i][0]+14400000;
	
}



$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";

$result=mysqli_query($dbc,$query) or
	die(mysqli_sqlstate($dbc));
while($row = mysqli_fetch_array ($result)){
	//echo $row[$x_id]." - ".$row[$y_id]."<br />";
	$numbs_rec117=$row[0];
	}



#1 Восточ	
$table="p1921681501";
$x_id="date";
$y_id="value";
$z1_id="rx";
$z2_id="tx";
$z3_id="ml";
$z4_id="mrx";
$z5_id="mtx";
$z6_id="sigpoz";
$z7_id="dvr";
$z8_id="cam1";
$z9_id="cam2";
$z10_id="cam3";
$z11_id="cam4";
$z12_id="ub1";
$z13_id="ub2";
$z14_id="sbor";
$z15_id="ub1sig";
$z16_id="ub1amq";
$z17_id="ub1amc";
$z18_id="ub2sig";
$z19_id="ub2amq";
$z20_id="ub2amc";
$z21_id="mlrx";
$z22_id="mltx";
$z31_id="luchrx";
$z32_id="luchtx";
$xy_value118=array();


$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
//echo $query;
$result=mysqli_query($dbc,$query) or
	die(mysqli_sqlstate($dbc));
//echo mysqli_sqlstate($dbc);
// echo $_POST['email'];
// echo $_POST['pass'];

//Добавление значений в массив
while($row = mysqli_fetch_array ($result)){
	//echo $row[$x_id]." - ".$row[$y_id]."<br />";
	array_push($xy_value118,$row);
	}
	


//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
//echo count($xy_value);
for ($i=0;$i<count($xy_value118);$i++){
	$xy_value118[$i][0]=1000*$xy_value118[$i][0]+14400000;
	
}



$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";

$result=mysqli_query($dbc,$query) or
	die(mysqli_sqlstate($dbc));
while($row = mysqli_fetch_array ($result)){
	//echo $row[$x_id]." - ".$row[$y_id]."<br />";
	$numbs_rec118=$row[0];
	}


#544	
$table="p3729899";
$x_id="date";
$y_id="value";
$z1_id="rx";
$z2_id="tx";
$z3_id="ml";
$z4_id="mrx";
$z5_id="mtx";
$z6_id="sigpoz";
$z7_id="dvr";
$z8_id="cam1";
$z9_id="cam2";
$z10_id="cam3";
$z11_id="cam4";
$z12_id="ub1";
$z13_id="ub2";
$z14_id="sbor";
$z15_id="ub1sig";
$z16_id="ub1amq";
$z17_id="ub1amc";
$z18_id="ub2sig";
$z19_id="ub2amq";
$z20_id="ub2amc";
$z21_id="mlrx";
$z22_id="mltx";
$z31_id="luchrx";
$z32_id="luchtx";
$xy_value544=array();


$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id.",".$z22_id.",".$z31_id.",".$z32_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
//echo $query;
$result=mysqli_query($dbc,$query) or
	die(mysqli_sqlstate($dbc));
//echo mysqli_sqlstate($dbc);
// echo $_POST['email'];
// echo $_POST['pass'];

//Добавление значений в массив
while($row = mysqli_fetch_array ($result)){
	//echo $row[$x_id]." - ".$row[$y_id]."<br />";
	array_push($xy_value544,$row);
	}
	


//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
//echo count($xy_value);
for ($i=0;$i<count($xy_value544);$i++){
	$xy_value544[$i][0]=1000*$xy_value544[$i][0]+14400000;
	
}



$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";

$result=mysqli_query($dbc,$query) or
	die(mysqli_sqlstate($dbc));
while($row = mysqli_fetch_array ($result)){
	//echo $row[$x_id]." - ".$row[$y_id]."<br />";
	$numbs_rec544=$row[0];
	}
		
    mysqli_close($dbc);

		
?>