<?php 
session_start();
$confMsg = '';
if ($_SESSION['start']<>1) {
	header("Location: /index.php");
	exit;
}
?>

<?php
	$dbc= mysqli_connect('127.0.0.1', 'goodman', 'NRywfHcXEmzenn7S') or
		die(mysqli_sqlstate($dbc));
	
	$code_page="SET NAMES 'utf8';";
	mysqli_query($dbc,$code_page) or
		die(mysqli_sqlstate($dbc));

	$name_base="pozitron";
	//$table="p372978226";
	$xy_value110d=array();
	//$cur_time=1505176261-6*60*60;
	$timeshift = 4;
	$cur_time=time()-60*60*(float)$timeshift;
	//$table="s110";
	$table=$_GET['well_Name'];
	$start_time = $_GET['start_time'];
	$end_time = $_GET['end_time'];
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
	$z21_id="Vinstr";


	//$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	$query="SELECT * FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$start_time." AND ".$x_id."<".(int)$end_time.";";
	#echo $table;
	$result=mysqli_query($dbc,$query) or die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	//echo $result;
	
	$xy_value110d = array();
	while($row=mysqli_fetch_array($result,MYSQLI_ASSOC)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$cur_rec= array('Vrema' => $row['Vrema'],'Wkp' => $row['Wkp'],'Wdol' => $row['Wdol'],'Mpot' => $row['Mpot'],
		'Npot' => $row['Npot'],'Pbx' => $row['Pbx'],'Qbx' => $row['Qbx'],'Talblok' => $row['Talblok'],
		'Zaboj' => $row['Zaboj'],'Instr' => $row['Instr'],'C1C5' => $row['C1C5'],'C1' => $row['C1'],
		'Xn1' => $row['Xn1'],'Xn2' => $row['Xn2'],'Potok' => $row['Potok'],'Tbix' => $row['Tbix'],
		'V1' => $row['V1'],'V2' => $row['V2'],'V3' => $row['V3'],'V4' => $row['V4'],
		'Vdol' => $row['Vdol'],'Vobj' => $row['Vobj'],'Vinstr' => $row['Vinstr']);
		//$cur_rec['Wkp'] = $row['Wkp'];
		array_push($xy_value110d, $cur_rec);
		}
	mysqli_free_result($result);
	
	echo json_encode($xy_value110d);
	//echo json_encode($ass);
	
	/* $query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec110d=$row[0];
		} */
		
    mysqli_close($dbc);

		
?>