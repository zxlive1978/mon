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
	$xy_value916=array();
	$cur_time=time()-60*60*24*(float)$timeshift;

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
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
	$xy_value4450=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
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
	$xy_value631=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
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
	$table="p31173139222";
	$x_id="date";
	$y_id="value";
	$z1_id="rx";
	$z2_id="tx";
	$z3_id="ml";
	$xy_value110=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
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
	$xy_value2241=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
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
	$table="p31173139194";
	$x_id="date";
	$y_id="value";
	$z1_id="rx";
	$z2_id="tx";
	$z3_id="ml";
	$xy_value908=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
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
	$xy_value411=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
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
	$xy_valueconn=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
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
	$xy_value89=array();

	
	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
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

	#110 data	
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
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));

	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		array_push($xy_value110d,$row);
		}
		
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value110d);$i++){
		$xy_value110d[$i][0]=1000*$xy_value110d[$i][0]+14400000;	
	}
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec110d=$row[0];
		}

	#224 data	
	$table="s224";
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
	$xy_value224d=array();

	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));

	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		array_push($xy_value224d,$row);
		}
		
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value224d);$i++){
		$xy_value224d[$i][0]=1000*$xy_value224d[$i][0]+14400000;	
	}
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec224d=$row[0];
		}
		
	#908 data	
	$table="s908";
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
	$xy_value908d=array();

	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));

	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		array_push($xy_value908d,$row);
		}
		
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value908d);$i++){
		$xy_value908d[$i][0]=1000*$xy_value908d[$i][0]+14400000;	
	}
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec908d=$row[0];
		}

	#411 data	
	$table="s411";
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
	$xy_value411d=array();

	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));

	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		array_push($xy_value411d,$row);
		}
		
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value411d);$i++){
		$xy_value411d[$i][0]=1000*$xy_value411d[$i][0]+14400000;	
	}
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec411d=$row[0];
		}
		
	#89 data	
	$table="s89";
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
	$xy_value89d=array();

	$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));

	
	//Добавление значений в массив
	while($row = mysqli_fetch_array ($result)){
		array_push($xy_value89d,$row);
		}
		
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value);
	for ($i=0;$i<count($xy_value89d);$i++){
		$xy_value89d[$i][0]=1000*$xy_value89d[$i][0]+14400000;	
	}
	$query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec89d=$row[0];
		}
		
		
    mysqli_close($dbc);

		
?>